import ast
import re

from .ir import DataString, Global, Instruction, Label, Program


_DATA_STRING_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*):\s*string\s+(".*")$')
_LABEL_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):$")


class ParseError(Exception):
    pass


def parse(source: str) -> Program:
    program = Program()
    section: str | None = None

    for line_no, raw_line in enumerate(source.splitlines(), start=1):
        line = _strip_comment(raw_line).strip()
        if not line:
            continue

        if line in {".data", ".text"}:
            section = line[1:]
            continue

        if section is None:
            raise ParseError(f"line {line_no}: expected .data or .text before code")

        if section == "data":
            program.data.append(_parse_data(line, line_no))
        else:
            item = _parse_text(line, line_no)
            program.text.append(item)

    return program


def _strip_comment(line: str) -> str:
    in_string = False
    escaped = False
    for index, char in enumerate(line):
        if escaped:
            escaped = False
            continue
        if char == "\\" and in_string:
            escaped = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if not in_string and char in {";", "#"}:
            return line[:index]
    return line


def _parse_data(line: str, line_no: int) -> DataString:
    match = _DATA_STRING_RE.match(line)
    if not match:
        raise ParseError(f"line {line_no}: expected data like: name: string \"text\"")
    name, raw_value = match.groups()
    try:
        value = ast.literal_eval(raw_value)
    except (SyntaxError, ValueError) as exc:
        raise ParseError(f"line {line_no}: invalid string literal") from exc
    if not isinstance(value, str):
        raise ParseError(f"line {line_no}: string data must be a string literal")
    return DataString(name=name, value=value)


def _parse_text(line: str, line_no: int) -> Label | Global | Instruction:
    label = _LABEL_RE.match(line)
    if label:
        return Label(label.group(1))

    if line.startswith("global "):
        name = line.removeprefix("global ").strip()
        if not name:
            raise ParseError(f"line {line_no}: global needs a symbol name")
        return Global(name)

    if " " in line:
        op, arg_text = line.split(None, 1)
        args = [part.strip() for part in arg_text.split(",") if part.strip()]
    else:
        op, args = line, []
    return Instruction(op=op, args=args, line=line_no)

