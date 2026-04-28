from commonasm.backends import compile_program
from commonasm.parser import parse


def test_compiles_hello_to_x86_64_nasm():
    program = parse(
        '.data\nmsg: string "Hi\\n"\n.text\nglobal _start\n_start:\nsyscall write, 1, msg, 3\n'
    )

    output = compile_program(program, "x86_64-nasm")

    assert "global _start" in output
    assert "mov rax, 1" in output
    assert "mov rsi, msg" in output
    assert "syscall" in output


def test_compiles_hello_to_riscv64_gnu():
    program = parse(
        '.data\nmsg: string "Hi\\n"\n.text\nglobal _start\n_start:\nsyscall write, 1, msg, 3\n'
    )

    output = compile_program(program, "riscv64-gnu")

    assert ".globl _start" in output
    assert "li a7, 64" in output
    assert "la a1, msg" in output
    assert "ecall" in output

