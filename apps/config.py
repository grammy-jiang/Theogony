"""Enhanced AppConfig"""
import logging
from pathlib import Path

from django.apps import AppConfig as _AppConfig

logger = logging.getLogger("django")


class AppConfig(_AppConfig):
    """Enhanced AppConfig"""

    @property
    def migration_scripts(self) -> tuple[Path, ...]:
        """
        get the migration scripts of the application
        :return:
        :rtype: tuple[Path, ...]
        """
        try:
            return tuple(
                sorted(
                    script
                    for script in (Path(self.path) / "migrations").iterdir()
                    if script.is_file()
                    and script.stem != "__init__"
                    and script.suffix == ".py"
                )
            )
        except FileNotFoundError as exc:
            logger.exception(exc)
            return ()

    @property
    def fixture_files(self) -> tuple[Path, ...]:
        """
        get the fixture files of the application
        :return:
        :rtype: tuple[Path, ...]
        """
        try:
            return tuple(
                sorted(
                    file
                    for file in (Path(self.path) / "fixtures").iterdir()
                    if file.is_file() and file.suffix in {".yaml", ".yml"}
                )
            )
        except FileNotFoundError as exc:
            logger.exception(exc)
            return ()
