from pathlib import Path

from hunspell2.cli_runner import CLIRunner
from hunspell2.cli_utils import run_process_with_stdin


class HunSpell:
    def __init__(self, dic_path: str | Path) -> None:
        if isinstance(dic_path, str):
            dic_path = Path(dic_path)

        assert dic_path.suffix == ".dic", "expected '.dic' file"
        dic_path = dic_path.expanduser()
        assert dic_path.absolute().exists(), f"{dic_path} does not exist"

        self.dic_path = dic_path
        self.command = [
            "hunspell",
            "-d",
            str(dic_path.absolute().parent / dic_path.stem),
        ]
        self.cli = CLIRunner(self.command)
        self.cli.await_message()

    def raw(self, word: str):
        return self.cli.await_reply(word)

    def spell(self, word: str):
        ans = self.raw(word)
        return ans[0][0] in ["*", "+"]

    def suggest(self, word: str):
        ans = self.raw(word)[0].strip()
        if ans[0] != "&":
            return []

        return ans[ans.find(":") + 1 :].split(", ")

    def stem(self, word: str) -> list[str]:
        stdout, stderr = run_process_with_stdin(self.command + ["-s"], word)
        if stderr:
            raise OSError(stderr)

        lines = [line.split() for line in stdout.strip().splitlines()]
        return [line[1] for line in lines if len(line) == 2]

    def analyze(self, word: str) -> list[list[str]]:
        stdout, stderr = run_process_with_stdin(self.command + ["-m"], word)
        if stderr:
            raise OSError(stderr)

        morph = [line.split()[1:] for line in stdout.strip().splitlines()]
        return [s for s in morph if s]

    def close(self):
        self.cli.kill()
