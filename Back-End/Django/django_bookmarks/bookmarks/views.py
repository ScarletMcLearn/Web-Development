from django.shortcuts import render

# Create your views here.

"""
from django.http import HttpResponse
def main_page(request):
 output = '''
 <html>
 <head><title>%s</title></head>
 <body>
 <h1>%s</h1><p>%s</p>
 </body>
 </html>
 ''' % (
 'Django Bookmarks',
 'Welcome to Django Bookmarks',
 'Where you can store and share bookmarks!'
 )
 return HttpResponse(output)
"""

from django.http import HttpResponse

def main_page(request):
    output = '''
    <html>
        <head>
            <title>%s</p>
        </head>
        <body>
            <h1>%s</h1> <p>%s</p>
        </body>
    </html>
    ''' % ("Django Bookmarks", "Welcome To Django Bookmarks", "Where you can store and share bookmarks!")
    return HttpResponse(output)