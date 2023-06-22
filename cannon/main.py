"""Main module for the console script."""
import sys
import logging
from typing import List

from cliff.app import App
from cliff.commandmanager import CommandManager
from pbr.version import VersionInfo


class CannonApp(App):
    """The cannon app."""

    def __init__(self: App):
        """Initialize the App class."""
        super().__init__(
            description="Canonical OpenStack Validation Suite",
            command_manager=CommandManager("cannon.cli"),
            version=VersionInfo("cannon").version_string(),
            deferred_help=True,
        )

    def configure_logging(self):
        super().configure_logging()
        logging.getLogger("").handlers[0].setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s %(name)s - %(message)s")
        )
        return


def main(argv: List[str] = sys.argv[1:]) -> int:  # pylint: disable=dangerous-default-value
    """Run the application."""
    myapp = CannonApp()
    return myapp.run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
