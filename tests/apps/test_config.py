import logging
from pathlib import Path
from tempfile import TemporaryDirectory

from django.test import SimpleTestCase

from apps import AppConfig


class Stub:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class AppConfigTests(SimpleTestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.temp_directory = TemporaryDirectory()

        self.path_temp_directory = Path(self.temp_directory.name)

        self.migrations = self.path_temp_directory / "migrations"
        self.migrations.mkdir()
        self.migration_scripts = tuple(
            self.migrations / script for script in ("0000_scripts.py", "0001_script.py")
        )
        for script in self.migration_scripts:
            script.touch()

        self.fixtures = self.path_temp_directory / "fixtures"
        self.fixtures.mkdir()
        self.fixture_files = tuple(
            self.fixtures / script
            for script in ("0000_fixture.yaml", "0001_fixture.yaml")
        )
        for script in self.fixture_files:
            script.touch()

    def tearDown(self) -> None:
        del self.fixture_files
        del self.fixtures
        del self.migration_scripts
        del self.migrations
        del self.path_temp_directory
        self.temp_directory.cleanup()

    def test_migration_scripts(self):
        class MyAppConfig(AppConfig):
            path = self.temp_directory.name

        app_config = MyAppConfig("test", Stub())

        self.assertSequenceEqual(app_config.migration_scripts, self.migration_scripts)

    def test_migration_scripts_exception(self):
        class MyAppConfig(AppConfig):
            path = "a path not exist"

        app_config = MyAppConfig("test", Stub())

        with self.assertLogs("django", level=logging.INFO) as cm:
            migration_scripts = app_config.migration_scripts
        self.assertSequenceEqual(migration_scripts, ())

    def test_fixture_files(self):
        class MyAppConfig(AppConfig):
            path = self.temp_directory.name

        app_config = MyAppConfig("test", Stub())

        self.assertSequenceEqual(app_config.fixture_files, self.fixture_files)

    def test_fixture_files_exception(self):
        class MyAppConfig(AppConfig):
            path = "a path not exist"

        app_config = MyAppConfig("test", Stub())

        with self.assertLogs("django", level=logging.INFO) as cm:
            fixture_files = app_config.fixture_files
        self.assertSequenceEqual(fixture_files, ())
