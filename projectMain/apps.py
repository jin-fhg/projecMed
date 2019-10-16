from django.apps import AppConfig


class ProjectmainConfig(AppConfig):
    name = 'projectMain'

    def ready(self):
        import projectMain.signals


