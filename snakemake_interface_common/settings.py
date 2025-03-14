from __future__ import annotations

from abc import abstractmethod
from enum import Enum
from typing import Callable, FrozenSet, Iterable, List, Set, TypeVar, cast

TSettingsEnumBase = TypeVar("TSettingsEnumBase", bound="SettingsEnumBase")

TContainer = TypeVar("TContainer")


class SettingsEnumBase(Enum):
    """A base enumeration class for settings with utility methods for choice handling.

    Base enumeration class that extends Enum to provide common functionality for
    settings enumerations, including methods to parse and format choices.

    Methods
    -------
    choices() : List[str]
        Returns a sorted list of all enum choices in lowercase with hyphens.
    all() : FrozenSet[TSettingsEnumBase]
        Returns a frozenset of all enum members except those marked to skip.
    parse_choices_list(choices: List[str]) : List[TSettingsEnumBase]
        Converts a list of string choices into enum members.
    parse_choices_set(choices: List[str]) : Set[TSettingsEnumBase]
        Converts a list of string choices into a set of enum members.
    parse_choice(choice: str) : TSettingsEnumBase
        Converts a single string choice into an enum member.
    skip_for_all() : FrozenSet[TSettingsEnumBase]
        Abstract method to define members to exclude from all().
    item_to_choice() : str
        Converts an enum member name to lowercase with hyphens.

    Notes
    -----
    The class handles conversion between:
    - Internal representation: UPPERCASE with underscores (e.g., "SOME_SETTING")
    - External representation: lowercase with hyphens (e.g., "some-setting")

    Examples
    --------
    >>> class MySettings(SettingsEnumBase):
    ...     SETTING_ONE = "value1"
    ...     SETTING_TWO = "value2"
    ...
    ...     def skip_for_all(cls):
    ...         return frozenset([cls.SETTING_TWO])
    """

    @classmethod
    def choices(cls) -> List[str]:
        return sorted(item.item_to_choice() for item in cls)

    @classmethod
    def all(cls) -> FrozenSet[TSettingsEnumBase]:
        skip: FrozenSet[TSettingsEnumBase] = cls.skip_for_all()
        return frozenset(
            cast(TSettingsEnumBase, item) for item in cls if item not in skip
        )

    @classmethod
    def parse_choices_list(cls, choices: List[str]) -> List[TSettingsEnumBase]:
        return cls._parse_choices_into(choices, list)

    @classmethod
    def parse_choices_set(cls, choices: List[str]) -> Set[TSettingsEnumBase]:
        return cls._parse_choices_into(choices, set)

    @classmethod
    def _parse_choices_into(
        cls,
        choices: List[str],
        container: Callable[[Iterable[TSettingsEnumBase]], TContainer],
    ) -> TContainer:
        return container(
            cast(TSettingsEnumBase, cls.parse_choice(choice)) for choice in choices
        )

    @classmethod
    def parse_choice(cls, choice: str) -> SettingsEnumBase:
        return cls[choice.replace("-", "_").upper()]

    @classmethod
    @abstractmethod
    def skip_for_all(cls) -> FrozenSet[TSettingsEnumBase]:
        return frozenset()

    def item_to_choice(self) -> str:
        return self.name.replace("_", "-").lower()

    def __str__(self):
        return self.item_to_choice()
