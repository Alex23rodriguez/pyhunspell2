from hunspell2.cli_utils import await_message, send_message, start_process


class CLIRunner:
    def __init__(self, command: list[str]) -> None:
        self.command = command
        self.restart()

    def await_message(self, timeout=1):
        # if self.process.poll() is not None:
        # raise ValueError("Process is dead")

        return await_message(self.stdout_queue, self.stderr_queue, timeout)

    def send_message(self, msg: str, newline=True):
        # if self.process.poll() is not None:
        # raise ValueError("Process is dead")

        send_message(self.process, msg, newline)

    def await_reply(self, msg: str, newline=True, timeout=1):
        self.send_message(msg, newline)
        return self.await_message(timeout)

    def restart(self):
        process, stdout_queue, stderr_queue = start_process(self.command)

        self.process = process
        self.stdout_queue = stdout_queue
        self.stderr_queue = stderr_queue

    def poll(self):
        return self.process.poll()

    def kill(self):
        self.process.kill()
