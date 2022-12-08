"""
Reset the development environment
"""
from __future__ import annotations

import pprint
from functools import cache
from pathlib import Path
from typing import Any, Optional, TypeVar

from django.apps import AppConfig as _AppConfig
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand

AppConfig = TypeVar("AppConfig", bound=_AppConfig)

User = get_user_model()

MIGRATION_SCRIPTS_KEEP: set[Path] = set()


@cache
def get_local_apps() -> tuple[AppConfig, ...]:
    """
    get all applications in the project of Theogony
    :return:
    :rtype: tuple[AppConfig, ...]
    """
    return tuple(
        app_config
        for app_config in apps.app_configs.values()
        if Path(app_config.path).is_relative_to(settings.BASE_DIR)
    )


class Command(BaseCommand):
    """
    Reset the development environment
    """

    help = "Reset the development environment"

    def remove_database(self) -> Command:
        """
        remove existed databases
        :return:
        :rtype: Command
        """
        self.stdout.write(
            self.style.NOTICE(
                f"The databases found in settings:\n"
                f"{pprint.pformat(settings.DATABASES)}"
            )
        )
        database: dict[str, Any]
        for database in settings.DATABASES.values():
            if (
                database["ENGINE"] == "django.db.backends.sqlite3"
                and database["NAME"].is_file()
            ):
                database["NAME"].unlink()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Remove existed sqlite3 database: {database['NAME']}"
                    )
                )
                continue
            raise TypeError("Database Type is not able to remove")
        return self

    def remove_migration_scripts(self) -> Command:
        """
        remove existed migration scripts
        :return:
        :rtype: Command
        """
        for app in get_local_apps():
            removed_scripts: list[str] = []
            for script in filter(
                lambda x: x not in MIGRATION_SCRIPTS_KEEP, app.migration_scripts
            ):
                removed_scripts.append(str(script))
                script.unlink()

            self.stdout.write(
                self.style.SUCCESS(
                    f"The migration scripts of the local app [{app.name}] are "
                    f"removed:\n"
                    f"{pprint.pformat(removed_scripts)}"
                )
            )
        return self

    def create_migration_scripts(self) -> Command:
        """
        run command makemigrations
        :return:
        :rtype: Command
        """
        self.stdout.write(self.style.NOTICE("Run command makemigrations"))
        call_command("makemigrations")
        for app in get_local_apps():
            scripts = tuple(
                str(x)
                for x in set(app.migration_scripts).difference(MIGRATION_SCRIPTS_KEEP)
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"The migration scripts of the local app [{app.name}] are "
                    f"created:\n"
                    f"{pprint.pformat(scripts)}"
                )
            )
        return self

    def migrate(self) -> Command:
        """
        run command migrate against each database
        :return:
        :rtype: Command
        """
        for database in settings.DATABASES:
            self.stdout.write(
                self.style.NOTICE(f"Run command migrate against database [{database}]")
            )
            call_command("migrate", f"--database={database}")
        return self

    def load_fixtures(self) -> Command:
        """
        load fixtures
        :return:
        :rtype: Command
        """
        for app in get_local_apps():
            self.stdout.write(
                self.style.NOTICE(
                    f"The fixtures of the local app [{app.name}] are found:\n"
                    f"{pprint.pformat(tuple(str(x) for x in app.fixtures))}"
                )
            )

            self.stdout.write(self.style.NOTICE("Start to load fixtures."))

            for i, fixture in enumerate(app.fixtures, start=1):
                call_command("loaddata", fixture)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"[{i}/{len(app.fixtures)}] "
                        f"Fixture is successfully loaded: {fixture}"
                    )
                )

        return self

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        """

        :param args:
        :type args: Any
        :param options:
        :type options: Any
        :return:
        :rtype: Optional[str]
        """
        self.stdout.write(
            self.style.NOTICE(
                "This command is going to reset the development environment"
            )
        )

        if not settings.DEBUG:
            self.stderr.write(
                self.style.ERROR("This command only works with DEBUG mode.")
            )

        self.remove_database().remove_migration_scripts().create_migration_scripts().migrate()
