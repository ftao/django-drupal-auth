from .models import Sessions, Users

class DrupalSessionBackend(object):
    """
    This backend is to be used in conjunction with the ``DrupalSessionMiddleware``
    found in the middleware module of this package, and is used when the server
    is handling authentication outside of Django.

    By default, the ``authenticate`` method creates ``User`` objects for
    usernames that don't already exist in the database.  Subclasses can disable
    this behavior by setting the ``create_unknown_user`` attribute to
    ``False``.
    """

    # Create a User object if not already in the database?
    create_unknown_user = True

    def authenticate(self, sid):
        """
        This method lookup user from drupal ``sessions`` and ``users`` table by `sid`,
        return the user if found, return None otherwise 

        $user = db_fetch_object(db_query("SELECT u.*, s.* FROM {users} u INNER JOIN {sessions} s ON u.uid = s.uid WHERE s.sid = '%s, $key)

        """
        if not sid:
            return

        try:
            session = Sessions.objects.get(sid=sid)
            user = Users.objects.get(uid=session.uid)
            return user
        except (Sessions.DoesNotExist, Users.DoesNotExist):
            return

    def clean_username(self, username):
        """
        Performs any cleaning on the "username" prior to using it to get or
        create the user object.  Returns the cleaned username.

        By default, returns the username unchanged.
        """
        return username

    def configure_user(self, user):
        """
        Configures a user after creation and returns the updated user.

        By default, returns the user unmodified.
        """
        return user
