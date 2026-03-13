from abc import ABC, abstractmethod
from typing import Optional


class RuleCacheInterface(ABC):
    @property
    @abstractmethod
    def output(self) -> bool: ...

    @property
    @abstractmethod
    def omit_software(self) -> bool: ...

    @property
    @abstractmethod
    def omit_storage_content(self) -> bool: ...

    @abstractmethod
    async def exists(self, job) -> bool: ...

    @abstractmethod
    async def fetch(self, job): ...

    @abstractmethod
    async def store(self, job): ...


class RuleInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def lineno(self) -> int: ...

    @property
    @abstractmethod
    def snakefile(self) -> str: ...

    @property
    @abstractmethod
    def cache(self) -> Optional[RuleCacheInterface]: ...
