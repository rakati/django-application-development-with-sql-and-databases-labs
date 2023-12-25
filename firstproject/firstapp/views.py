'''First app views'''
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Home page for firstapp"""
    # create a simple html page as a string
    template = "<html>" \
        "This is my first view" \
        "</html>"
    # return the template as content argument in HTTP response
    return HttpResponse(content=template)
