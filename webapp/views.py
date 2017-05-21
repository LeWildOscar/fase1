
from django.shortcuts import render


from webapp.models import Play
from webapp.models import Stats
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def home(request):

    query_results = Play.objects.all()
    query_results2 = Stats.objects.all()

    return render(request, 'index.html', context={'query_results': query_results, 'query_results2':query_results2})


def upload(request):
    if request.method=='POST':
        if request.POST['type'] == 'play':
            play = Play()
            play.author = request.POST['author']
            play.character = request.POST['character']
            play.video = request.POST['video']
            play.save()

        return HttpResponseRedirect("/")
    else:
        return render(request, 'upload.html')
