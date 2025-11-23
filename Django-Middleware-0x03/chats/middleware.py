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

