'''First app views'''
from django.http import HttpResponse
from datetime import date


# Create your views here.


def index(request):
    """Home page for firstapp"""
    # create a simple html page as a string
    template = "<html>" \
        "This is my first view" \
        "</html>"
    # return the template as content argument in HTTP response
    return HttpResponse(content=template)


def get_date(request):
    '''Simple page returning current date'''
    today = date.today()
    template = "<html>" \
        f"Today's date is {today}" \
        "</html>"
    return HttpResponse(content=template)
