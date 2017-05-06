# from django.shortcuts import render

# from django.http import HttpResponse

from .models import Album

# from django.template import loader

from django.shortcuts import render

from django.http import Http404



# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {'all_albums' : all_albums,}
    # html = ''
    # for album in all_albums:
    #     url = '/music/' + str(album.id) + '/'
    #     html += '<a href="' + url + ' ">' + album.album_title + '</a><br>'
    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    # return HttpResponse('<h2>Details for album ID: ' + str(album_id) + ' </h2?')
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Ablum does not exist! :< ")

    return render(request, 'music/detail.html', {'album': album,})
