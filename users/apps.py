from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

#method of the users app config to perform initialization task which is registering signals 
    def ready(self):
        import users.signals
