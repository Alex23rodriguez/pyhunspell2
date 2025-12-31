import queue
import subprocess
import threading
from time import time


def run_process_with_stdin(command: list[str], stdin: str) -> tuple[str, str]:
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdout, stderr = process.communicate(stdin)
    return stdout, stderr


def _enqueue_output(pipe, q):
    for line in iter(pipe.readline, ""):
        q.put(line)
    pipe.close()


def start_process(command: list[str]):
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    # Queues to hold stdout/stderr lines
    stdout_queue = queue.Queue()
    stderr_queue = queue.Queue()

    # Start threads to read stdout and stderr
    threading.Thread(
        target=_enqueue_output, args=(process.stdout, stdout_queue), daemon=True
    ).start()
    threading.Thread(
        target=_enqueue_output, args=(process.stderr, stderr_queue), daemon=True
    ).start()

    return process, stdout_queue, stderr_queue


def read_queue(queue) -> list[str]:
    lines = []
    while not queue.empty():
        lines.append(queue.get_nowait())
    return lines


def send_message(process, msg: str, newline=True):
    process.stdin.write(msg + ("\n" if newline else ""))
    process.stdin.flush()


def await_message(stdout_queue, stderr_queue, timeout=1):
    timeout_start = time()
    while time() < timeout_start + timeout:
        if not stderr_queue.empty():
            raise OSError("\n".join(read_queue(stderr_queue)))

        if not stdout_queue.empty():
            return read_queue(stdout_queue)

    raise TimeoutError()
