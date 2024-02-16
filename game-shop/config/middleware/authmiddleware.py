from django.http import HttpResponseRedirect, HttpResponse
from config.settings import LOGIN_URL


class AuthRequiredMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        if request.method == 'POST' or request.method == 'PATCH':
            if not request.user.is_authenticated:
                if not 'http://127.0.0.1:8000/accounts' in request.build_absolute_uri(): 
                    
                    return HttpResponseRedirect(LOGIN_URL) and HttpResponse('must be authorization')

        return response
