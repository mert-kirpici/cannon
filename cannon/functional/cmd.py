"""The command module of functional validation subsystem."""
import logging
import subprocess
from argparse import ArgumentParser, Namespace
from configparser import ConfigParser
from typing import Any

from cannon import TEMPEST_WORKSPACE, TEMPEST_CONF

from cliff.command import Command


class Run(Command):
    """Command functional run."""

    logger = logging.getLogger(__name__)

    def get_parser(self: Command, prog_name: Any) -> ArgumentParser:
        parser = super().get_parser(prog_name)
        parser.add_argument("profile", help="Validation profile", choices=["network"])
        return parser

    def take_action(self: Command, parsed_args: Namespace) -> None:
        TEMPEST_WORKSPACE.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            f"tempest init {TEMPEST_WORKSPACE}".split(),
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        tempest_config = ConfigParser()
        tempest_config.read(TEMPEST_CONF)
        tempest_config.update(
            {
                "auth": {
                    "admin_username": "admin",
                    "admin_password": "openstack",
                    "admin_domain_name": "admin_domain",
                    "admin_user_domain_name": "admin_domain"
                },
                "identity": {
                    "uri_v3": "https://10.5.0.169:5000/v3"
                },
                "service_available": {
                    "neutron": "true"
                }
            }
        )
        with open(TEMPEST_CONF, "w") as f:
            tempest_config.write(f)

        with subprocess.Popen(
            "stestr run --serial --color tempest.api.network.test_networks.NetworksTest",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=TEMPEST_WORKSPACE,
            text=True
        ) as process:
            for line in process.stdout:
                self.logger.info(line.strip())
