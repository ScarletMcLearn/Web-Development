from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'piglatin/index.html', context={})

def translate(request):
    # return render(request, 'piglatin/translate.html', context={})
    original = request.GET['originaltext']

    translation = ''

    for word in original.lower().split():
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            translation += word
            translation += 'yay '
        else:
            translation += word[1:]
            translation += word[0]
            translation += 'ay '

    return HttpResponse(translation)