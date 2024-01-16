from django.http import HttpResponse
from django.shortcuts import render, redirect

from .froms import MovieForm
from.models import   Movie
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})
def addmovie(request):
    if request.method =='POST':
        name=request.POST.get('name',)
        year=request.POST.get('year',)
        language=request.POST.get('language',)
        genre=request.POST.get('genre',)
        img=request.FILES.get('img',)
        desc=request.POST.get('desc',)
        cast1=request.POST.get('cast1',)
        cast2=request.POST.get('cast2',)
        m=Movie(name=name,year=year,language=language,genre=genre,img=img,desc=desc,cast1=cast1,cast2=cast2)
        m.save()
        return redirect('/')
    return render(request,'add.html')
def update(request, id):
    movie = Movie.objects.get(id=id)

    # Manually set initial data for the form fields
    initial_data = {
        'name': movie.name,
        'language':movie.language,
        'genre':movie.genre,
        'year':movie.year,
        'img':movie.img,
        'desc':movie.desc,
        'cast1':movie.cast1,
        'cast2':movie.cast2,
    }

    form = MovieForm(instance=movie,initial=initial_data,)
    if request.method == 'POST':
        form = MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'movie': movie, 'form': form})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')