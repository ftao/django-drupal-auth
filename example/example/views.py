import json
from django.http import HttpResponse


def home(request):
    template = '''
    <head>
    <script type="text/javascript">
    function login() {
        //open javascript console , input 
        document.cookie = 'SESSanything=0cpm8ujaehqptpp2tikm4g07s3'
        window.location.reload();
    }

    function logout(){
       document.cookie = 'SESSanything=0cpm8ujaehqptpp2tikm4g07s3;expires=Thu, 01 Jan 1970 00:00:00 GMT';
       window.location.reload();
    }
    
    </script>
    </head>
    <body>
        <pre>%s</pre>
        <button onclick="login()">login</button>
        <button onclick="logout()">logout</button>
    </body>

    '''
    header = dict([(k, v) for k, v in request.META.items() if type(v) in (str, int, float, unicode)])
    info = {
        'cookie' : header.get('HTTP_COOKIE'),
        'is_authenticated' : request.user.is_authenticated(),
    }
    if request.user.is_authenticated():
        info['username'] = request.user.get_username()
    return HttpResponse(template % json.dumps(info, indent=2))

