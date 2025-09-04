from django.http import HttpResponsePermanentRedirect

class RedirectToCanonicalHostMiddleware:
    """
    Redirect www.example.com -> example.com (canonical)
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        # if not host.startswith("www."):
        #     return HttpResponsePermanentRedirect(f"{request.scheme}://www.{host}{request.get_full_path()}")

        if host.startswith("www."):
            new_host = host[4:]  # strip www
            return HttpResponsePermanentRedirect(f"{request.scheme}://{new_host}{request.get_full_path()}")
        return self.get_response(request)
