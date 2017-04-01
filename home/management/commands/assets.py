import os
import subprocess as sp

from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('command', nargs='?', default='css')

    def handle(self, *args, **options):
        installed_app_paths = [a.path for a in apps.app_configs.values()]

        local_paths = [p for p in installed_app_paths
                       if 'site-packages' not in p]

        gulp_env = dict(os.environ)
        gulp_env['APP_PATHS'] = ':'.join(local_paths)
        sp.run(['gulp', options['command']], env=gulp_env)
