from django.conf import settings
APP_NAME = 'drupalauth'
DB_NAME = getattr(settings, 'DRUPAL_AUTH_DB_NAME', 'drupal')

class DrupalRouter(object):
    """A router to control all database operations on models in
    the drupalauth application"""

    def db_for_read(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        if model._meta.app_label == APP_NAME:
            return DB_NAME
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        if model._meta.app_label == APP_NAME:
            return DB_NAME
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in myapp is involved"
        return None
        #return obj1._meta.app_label == obj2._meta.app_label

    def allow_syncdb(self, db, model):
        "Make sure the this app only appears on the right db"
        if db == DB_NAME:
            return model._meta.app_label == APP_NAME
        elif model._meta.app_label == APP_NAME:
            return False
        return None
