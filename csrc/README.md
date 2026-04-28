# commonasmc

`commonasmc.c` is the C AOT compiler for CommonASM.

Build:

```powershell
gcc csrc/commonasmc.c -o build/commonasmc.exe
```

Use:

```powershell
build/commonasmc.exe examples/hello.cas --target x86_64-nasm -o build/hello_from_c.asm
build/commonasmc.exe examples/hello.cas --target riscv64-gnu -o build/hello_from_c.s
```

This is the primary compiler implementation. It stays dependency-free so it can be used as
the bootstrap compiler for the self-hosting compiler.
