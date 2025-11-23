from datetime import datetime
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        # Allow access only between 6AM and 9PM
        if current_hour < 6 or current_hour >= 21:
            return HttpResponseForbidden("Access to chat is restricted during these hours.")
        return self.get_response(request)

