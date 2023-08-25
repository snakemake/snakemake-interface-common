__author__ = "Johannes Köster"
__copyright__ = "Copyright 2023, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from pathlib import Path
import textwrap
from typing import Optional

from snakemake_interface_common.rules import RuleInterface


class ApiError(Exception):
    pass


class WorkflowError(Exception):
    @staticmethod
    def format_arg(arg):
        if isinstance(arg, str):
            return arg
        elif isinstance(arg, WorkflowError):
            spec = ""
            if arg.rule is not None:
                spec += f"rule {arg.rule.name}"
            if arg.snakefile is not None:
                if spec:
                    spec += ", "
                spec += f"line {arg.lineno}, {arg.snakefile}"

            if spec:
                spec = f" ({spec})"

            return "{}{}:\n{}".format(
                arg.__class__.__name__, spec, textwrap.indent(str(arg), "    ")
            )
        else:
            return f"{arg.__class__.__name__}: {arg}"

    def __init__(self, *args, lineno: Optional[int]=None, snakefile: Optional[Path]=None, rule: Optional[RuleInterface]=None):
        super().__init__("\n".join(self.format_arg(arg) for arg in args))
        if rule is not None:
            self.lineno = rule.lineno
            self.snakefile = rule.snakefile
        else:
            self.lineno = lineno
            self.snakefile = snakefile
        self.rule = rule
