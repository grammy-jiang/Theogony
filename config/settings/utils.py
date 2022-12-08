"""
The utilities for settings of this project
"""
from pathlib import Path

import environ

BASE_DIR = Path(__file__).parent.parent.parent

environ.Env.read_env(BASE_DIR / ".env")
env = environ.Env()
