from django.utils.cache import patch_vary_headers
from django_mobile import get_flavour, _set_request_header


class FetchFromCacheFlavourMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _set_request_header(request, get_flavour(request))
        response = self.get_response(request)
        return response


class UpdateCacheFlavourMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        patch_vary_headers(response, ["X-Flavour"])
        return response
