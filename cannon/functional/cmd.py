"""The command module of functional validation subsystem."""
import logging
from argparse import ArgumentParser, Namespace
from typing import Any

from cliff.command import Command


class Run(Command):
    """Command functional run."""

    logger = logging.getLogger(__name__)

    def get_parser(self: Command, prog_name: Any) -> ArgumentParser:
        parser = super().get_parser(prog_name)
        parser.add_argument("scenario", help="Validation scenario", choices=["minimal"])
        return parser

    def take_action(self: Command, parsed_args: Namespace) -> None:
        self.logger.info("Run called with: [%s]", parsed_args.scenario)
