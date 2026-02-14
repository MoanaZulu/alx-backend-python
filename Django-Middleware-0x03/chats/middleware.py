from django.http import HttpResponseForbidden

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only allow admins or moderators
        if request.user.is_authenticated:
            if not (request.user.is_staff or getattr(request.user, 'role', '') == 'moderator'):
                return HttpResponseForbidden("You do not have permission to access this resource.")
        else:
            return HttpResponseForbidden("You must be logged in to access this resource.")

        response = self.get_response(request)
        return response









from datetime import datetime
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current hour (24-hour format)
        current_hour = datetime.now().hour

        # Restrict access outside 6AM–9PM
        if current_hour < 6 or current_hour >= 21:
            return HttpResponseForbidden("Access to messaging app is restricted during these hours.")

        response = self.get_response(request)
        return response






'chats.middleware.RequestLoggingMiddleware',






import logging
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logger to write to requests.log
        logging.basicConfig(
            filename="requests.log",
            level=logging.INFO,
            format="%(message)s"
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response






from datetime import datetime, timedelta
from django.http import HttpResponseForbidden

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to track requests per IP
        self.ip_requests = {}

    def __call__(self, request):
        # Only enforce limit on POST requests (chat messages)
        if request.method == "POST":
            ip = self.get_client_ip(request)
            now = datetime.now()

            # Initialize tracking for this IP if not present
            if ip not in self.ip_requests:
                self.ip_requests[ip] = []

            # Remove requests older than 1 minute
            self.ip_requests[ip] = [
                ts for ts in self.ip_requests[ip] if now - ts < timedelta(minutes=1)
            ]

            # Check if limit exceeded
            if len(self.ip_requests[ip]) >= 5:
                return HttpResponseForbidden("Message limit exceeded. Try again later.")

            # Record this request timestamp
            self.ip_requests[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Helper to extract client IP address"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")

