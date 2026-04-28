# Security Policy

## Supported versions

CommonASM is early-stage public domain software. There are no stable production
release branches yet. Security fixes are handled on the default branch.

| Version | Supported |
| --- | --- |
| `main` | Yes |
| older commits | No |

## Reporting a vulnerability

If GitHub private vulnerability reporting is enabled for this repository, use it
for sensitive reports.

If private reporting is not available, open a GitHub issue with a short summary
and avoid posting exploit details, secrets, private data, or weaponized samples.
Maintainers can then choose a safer follow-up channel.

Useful report details:

- Affected file, command, target, or input example.
- Expected behavior and actual behavior.
- Whether the issue can cause code execution, file overwrite, information leak,
  denial of service, or incorrect generated assembly.
- The operating system and compiler used for testing.

## Security scope

In scope:

- Crashes or memory safety bugs in `csrc/commonasmc.c`.
- Unsafe output path handling.
- Diagnostics or generated files that expose unintended local data.
- Compiler behavior that can unexpectedly overwrite files.

Out of scope:

- The fact that generated assembly can be dangerous when assembled and run.
- Bugs in third-party assemblers, linkers, or operating systems.
- Experimental pseudo targets not being executable machine code.
