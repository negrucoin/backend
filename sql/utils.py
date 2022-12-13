from contextlib import closing

import psycopg2
from django.conf import settings
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def get_connection_params(db_name: str) -> dict:
    return {
        'database': db_name,
        'user': settings.DATABASES['default']['USER'],
        'password': settings.DATABASES['default']['PASSWORD'],
        'host': settings.DATABASES['default']['HOST'],
        'port': settings.DATABASES['default']['PORT'],
    }


def run_sql(sql: str, connection_params: dict, autocommit: bool = True) -> None:
    with closing(psycopg2.connect(**connection_params)) as conn:
        if autocommit:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = conn.cursor()
        cur.execute(sql)

        if not autocommit:
            conn.commit()


def drop_database(db_name: str, connection_params: dict) -> None:
    run_sql(f"DROP DATABASE IF EXISTS {db_name}", connection_params)


def create_database(db_name: str, connection_params: dict) -> None:
    run_sql(f"CREATE DATABASE {db_name}", connection_params)


def restore_database(dump_path: str, connection_params: dict) -> None:
    with open(dump_path, 'r', encoding='utf-8') as stream:
        run_sql(stream.read(), connection_params, autocommit=False)
