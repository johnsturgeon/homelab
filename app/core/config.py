"""Configuration file"""

import os
from dataclasses import dataclass


# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
@dataclass
class Config:
    """Base configuration class"""

    # pylint: disable=invalid-name
    FERNET_KEY: str

    @classmethod
    def get_config(cls):
        """Factory method for returning the correct config"""
        config = cls(
            FERNET_KEY=os.getenv("FERNET_KEY"),
        )
        return config
