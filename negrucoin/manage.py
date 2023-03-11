#!/usr/bin/env python
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent


def main():
    """Run administrative tasks."""
    load_dotenv(BASE_DIR / 'config/.env')
    os.environ.setdefault('ENVIRONMENT', 'dev')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    try:
        # pylint: disable=import-outside-toplevel
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
