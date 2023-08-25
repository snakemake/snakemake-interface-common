from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Self, Set


class ParseChoicesType(Enum):
    SET = 0
    LIST = 1


class SettingsEnumBase(ABC):
    @classmethod
    def choices(cls) -> List[str]:
        return sorted(item.item_to_choice() for item in cls)

    @classmethod
    def all(cls) -> Set[Self]:
        return {item for item in cls}

    def parse_choices_list(self, choices: str) -> List[Self]:
        return self._parse_choices_into(choices, list)

    def parse_choices_set(self, choices: str) -> Set[Self]:
        return self._parse_choices_into(choices, set)

    @classmethod
    def _parse_choices_into(cls, choices: str, container: List | Set) -> List[Self]:
        return container(cls.parse_choice(choice) for choice in choices)

    @classmethod
    def parse_choice(cls, choice: str) -> Self:
        return choice.replace("-", "_").upper()

    def item_to_choice(self) -> str:
        return self.name.replace("_", "-").lower()

    def __str__(self):
        return self.item_to_choice()

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def value(self) -> str:
        ...