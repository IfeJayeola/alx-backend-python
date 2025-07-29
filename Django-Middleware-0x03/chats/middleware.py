from datetime import datetime
import time
from django.http import HttpResponse


class RequestLoggingMiddleware:
    """ Middleware to log requests with user information. """
    def __init__(self, get_response):
        """ Middleware to log requests with user information. """
        self.get_response = get_response

    def __call__(self, request):
        """ Middleware to log requests with user information. """
        #f"{datetime.now()} - User: {user} - Path: {request.path}“
        user = request.user if request.user.is_authenticated else "Anonymous"

        with open("request_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} - User: {user} - Path: {request.path}")
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    """ Middleware to restrict access to certain hours of the day. """
    def __init__(self, get_response):
        """ Middleware to restrict access to certain hours of the day. """
        self.get_response = get_response

    def __call__(self, request):
        """ Middleware to restrict access to certain hours of the day. """
        current_time = datetime.now().time()
        start_time = datetime.strptime("21:00", "%H:%M").time()
        end_time = datetime.strptime("18:00", "%H:%M").time()
        if not (start_time <= current_time <= end_time):
            return HttpResponse("Forbidden", status=403)
        response = self.get_response(request)
        return response


class OffensiveLanguageMiddleware:
    """ Middleware to filter offensive language in POST requests. """
    def __init__(self, get_response):
        """ Middleware to filter offensive language in POST requests. """
        self.get_response = get_response
        self.ip_list = {}

    def __call__(self, request):
        """ Middleware to restrict access based on IP address and request rate limiting. """
        if request.method == "POST":
            ip_address = request.META.get("REMOTE_ADDR")
            if ip_address not in self.ip_list:
                self.ip_list[ip_address] = []
            self.ip_list[ip_address].append(ip_address)
            current_time = time.time()

            self.ip_list[ip_address] = [
                timestamp for timestamp in self.ip_list[ip_address]
                if current_time - timestamp <= 60
            ]
            if len(self.ip_list[ip_address]) >= 5:
                return HttpResponse("Too many requests", status=429)
            self.ip_list[ip_address].append(current_time)
        response = self.get_response(request)
        return response


class RolepermissionMiddleware:
    """Middleware to restrict access based on user role."""
    def __init__(self, get_response):
        # Initialize the middleware with the get_response callable
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and has the correct role
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role != "admin":
                return HttpResponse("Forbidden", status=403)
        response = self.get_response(request)
        return response


