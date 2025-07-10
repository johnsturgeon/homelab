"""Configuration file"""

import os
from dataclasses import dataclass

from app.services.op_secrets import get_secret


# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
@dataclass
class Config:
    """Base configuration class"""

    # pylint: disable=invalid-name
    HOMELAB_API_AUTH_TOKEN: str = os.getenv("HOMELAB_API_AUTH_TOKEN")
    ONEPASSWORD_SERVICE_TOKEN: str = os.getenv("ONEPASSWORD_SERVICE_TOKEN")
    ANSIBLE_PUBLIC_KEY: str = None
    ROOT_PASSWORD: str = None
    TIDAL_ACCESS_TOKEN: str = None
    TIDAL_REFRESH_TOKEN: str = None

    async def load_secrets(self):
        """Loads the secrets from 1password"""
        secret_keys = [
            "ANSIBLE_PUBLIC_KEY",
            "ROOT_PASSWORD",
            "TIDAL_ACCESS_TOKEN",
            "TIDAL_REFRESH_TOKEN",
        ]

        for key in secret_keys:
            setattr(self, key, await get_secret(self.ONEPASSWORD_SERVICE_TOKEN, key))


global_config = Config()
