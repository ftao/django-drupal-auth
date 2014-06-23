from django.contrib import auth
from django.core.exceptions import ImproperlyConfigured

class DrupalSessionMiddleware(object):
    '''
    Middleware that read session id from cookie 
    and try to authenticate it against drupal database
    '''

    def process_request(self, request):
        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "The Django remote user auth middleware requires the"
                " authentication middleware to be installed.  Edit your"
                " MIDDLEWARE_CLASSES setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the RemoteUserMiddleware class.")

        sid = self._extract_session_id(request)
        user = None
        if sid is not None:
            user = auth.authenticate(sid=sid)

        if user is not None:
            if request.user.is_authenticated():
                if request.user.get_username() == user.get_username():
                    return 
            request.user = user
            #auth.login(request, user)
                
    def clean_username(self, username, request):
        """
        Allows the backend to clean the username, if the backend defines a
        clean_username method.
        """
        backend_str = request.session[auth.BACKEND_SESSION_KEY]
        backend = auth.load_backend(backend_str)
        try:
            username = backend.clean_username(username)
        except AttributeError:  # Backend has no clean_username method.
            pass
        return username

    def _extract_session_id(self, request):
        '''
        >>> d = DrupalSessionMiddleware()
        >>> d._extract_session_id('SESS75e1089b8fd262b6ac9d999204d69588=er01up52cbggcrlh26u3s8o3h0; has_js=1;')
        'er01up52cbggcrlh26u3s8o3h0'
        '''
        raw_cookie = request.META.get("HTTP_COOKIE",'')
        for item in raw_cookie.split(';'):
            parts = item.split('=', 1)
            if len(parts) <= 1:
                continue
            if parts[0].startswith('SESS'):
                return parts[1]
        return None
