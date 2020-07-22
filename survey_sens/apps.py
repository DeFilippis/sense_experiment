from django.apps import AppConfig
from django.conf import settings


class SensConfig(AppConfig):
    name = 'survey_sens'
    verbose_name = "Sense Suryve"

    def ready(self):
        t = settings.TEMPLATES[0]
        t['OPTIONS']['builtins'] = [
            'otree.templatetags.otree',
            'django.templatetags.i18n'
        ]

        print("AAAA", settings.TEMPLATES)
