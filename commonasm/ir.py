from dataclasses import dataclass, field


@dataclass(frozen=True)
class DataString:
    name: str
    value: str


@dataclass(frozen=True)
class Label:
    name: str


@dataclass(frozen=True)
class Global:
    name: str


@dataclass(frozen=True)
class Instruction:
    op: str
    args: list[str]
    line: int


TextItem = Label | Global | Instruction


@dataclass
class Program:
    data: list[DataString] = field(default_factory=list)
    text: list[TextItem] = field(default_factory=list)

