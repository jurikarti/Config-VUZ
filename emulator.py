import os
import shlex
import sys

from core_emulator import Emulator

def main():
    emu = Emulator()
    emu.run_repl()


if __name__ == '__main__':
    main()
