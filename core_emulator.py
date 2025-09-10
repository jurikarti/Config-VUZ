import os
import shlex
import sys

class Emulator:
    def __init__(self):
        self.cwd = "/"                          # Виртуальная текущая директория
        self.history = []                       # Буфер истории
        self.vfs_name = "VFS"

    def expand_vars(self, text: str) -> str:    # Парсер путей у ОС
        try:
            return os.path.expandvars(text)
        except Exception:
            return text

    def parse_line(self, line: str):            # Раскрытие команд из ввода
        line = line.strip()
        if not line:
            return None, []
        line = self.expand_vars(line)
        try:
            tokens = shlex.split(line)
        except ValueError as e:
            print(f"Ошибка разбора команды: {e}")
            return None, []
        return tokens[0], tokens[1:]

    def run_command(self, cmd, args):
        if cmd == 'exit':
            print('exit')
            raise SystemExit(0) 
        elif cmd == 'ls':
            print(f"ls вызван с аргументами: {args}")
        elif cmd == 'cd':
            print(f"cd вызван с аргументами: {args}")
            if len(args) == 1:
                target = os.path.expanduser(self.expand_vars(args[0]))
                if target.startswith('/'):
                    self.cwd = os.path.normpath(target)
                else:
                    self.cwd = os.path.normpath(os.path.join(self.cwd, target))
                print(f"(виртуальная cwd теперь: {self.cwd})")

        elif cmd == 'help':
            self.print_help()

        elif cmd == 'history':
            for i, h in enumerate(self.history[-50:], start=1):
                print(f"{i}: {h}")
        else:
            print(f"Неизвестная команда: {cmd}")

    def print_help(self):
        print("Поддерживаемые команды:")
        print("  ls [args]      - выводит имя и аргументы")
        print("  cd [dir]       - выводит имя и аргументы и меняет виртуальный cwd")
        print("  history        - вывести историю команд")
        print("  exit            - выйти из эмулятора")
        print("  help            - справка")

    def prompt(self):
        return f"{self.vfs_name}:{self.cwd}$ "

    def repl_once(self, line):
        cmd, args = self.parse_line(line)
        if cmd is None:
            return
        self.history.append(line)
        self.run_command(cmd, args)

    def run_repl(self):
        try:
            while True:
                try:
                    line = input(self.prompt())
                except EOFError:
                    print()
                    break
                if not line.strip():
                    continue
                self.repl_once(line)
        except SystemExit:
            pass
