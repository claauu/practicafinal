#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import random
import json
from script_manager import script_response


def main():
    """ Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PracticaFinal.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def get_scarlet_renponse(mensaje):
    
    return script_response(mensaje)

                

if __name__ == '__main__':
    main()
