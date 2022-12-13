import pytest
from django.conf import settings
from django.core.management import call_command
from django.db import connections

from sql.utils import restore_database, drop_database, get_connection_params, create_database


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    """Init test database after the pytest session will start."""

    # We cant drop database on which connected, so, we use additional db.
    template_name = 'template1'
    db_name = 'test'
    dump_path = 'sql/test_db.sql'
    settings.DATABASES['default']['NAME'] = db_name

    try:
        drop_database(db_name, get_connection_params(template_name))
        create_database(db_name, get_connection_params(template_name))
        restore_database(dump_path, get_connection_params(db_name))

        with django_db_blocker.unblock():
            call_command('migrate', verbosity=1)

        yield
    finally:
        for c in connections.all():
            c.close()

        drop_database(db_name, get_connection_params(template_name))
