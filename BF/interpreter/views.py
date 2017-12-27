from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def functionName( req ):
    return HttpResponse( '<h3>This is Interpreter Page</h3>' )

def navTest(req):
    return render(req,'nav.html')
