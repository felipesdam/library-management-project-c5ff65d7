from pathlib import Path

import environ


BASE_DIR = Path(__file__).resolve().parents[2]
env = environ.Env()
env.read_env(BASE_DIR / '.env', overwrite=True)


def get_env_variable(name, default=None, cast=None):
    return env.get_value(name, default=default, cast=cast)


def get_database_config(name='DATABASE_URL', default=None):
    return env.db_url(name, default=default)
