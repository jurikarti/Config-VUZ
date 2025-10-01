import argparse
import sys
from core_emulator import Emulator

def main():
    parser = argparse.ArgumentParser(description="Эмулятор командной оболочки")
    parser.add_argument("--vfs", type=str, help="Путь к физическому расположению VFS", required=True)
    parser.add_argument("--script", type=str, help="Путь к стартовому скрипту", required=False)

    args = parser.parse_args()

    # Отладочный вывод
    print("----------Отладочный вывод параметров-----------")
    print(f"VFS path   : {args.vfs}")
    print(f"Script path: {args.script if args.script else 'не задан'}")
    print("------------------------------------------------")

    emu = Emulator(vfs_path=args.vfs)

    if args.script:
        emu.run_script(args.script)

    emu.run_repl()

if __name__ == '__main__':
    main()

# python emulator.py --vfs /home/user/vfs --script test.sh
