import argparse
from pathlib import Path

from .backends import CompileError, compile_program
from .parser import ParseError, parse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="commonasm")
    parser.add_argument("input", type=Path)
    parser.add_argument("--target", required=True, choices=["x86_64-nasm", "riscv64-gnu"])
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)

    try:
        source = args.input.read_text(encoding="utf-8")
        program = parse(source)
        output = compile_program(program, args.target)
    except (OSError, ParseError, CompileError) as exc:
        parser.exit(1, f"commonasm: error: {exc}\n")

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0

