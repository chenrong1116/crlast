from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,HttpResponse
import requests
from lxml import etree
from movie.models import Movie,Jd

# Create your views here.


def pachong():
    top250 = []
    for j in range(0, 226, 25):
        url = 'https://movie.douban.com/top250?start=' + str(j)
        res = requests.get(url)
        tree = etree.HTML(res.text)

        for i in range(1, 26):
            movie = []
            movie += tree.xpath('//*[@id="content"]/div/div[1]/ol/li[' + str(i) +']/div/div[1]/em/text()')
            movie += tree.xpath('//*[@id="content"]/div/div[1]/ol/li[' + str(i) + ']/div/div[2]/div[1]/a/span[1]/text()')
            movie += tree.xpath('//*[@id="content"]/div/div[1]/ol/li[' + str(i)+']/div/div[2]/div[2]/p[1]/text()')
            top250.append(movie)
    return top250

def pachong2(pachong):
    top250 = pachong()
    save_list = []
    for i in top250:
        save_list.append(Movie(uid=i[0],name=i[1],info=i[2]))
    if Movie.objects.count()==0:
        Movie.objects.bulk_create(save_list)

def pachong3(request):
    pachong2(pachong)
    return HttpResponse('ok')


def movie(request):
    movie = Movie.objects.all()
    data ={
        'movie':movie
    }
    return render(request,'movie.html',context=data)



def jd(request):
    jd = Jd.objects.all()
    data ={
        'jd':jd
    }
    return render(request,'jd.html',context=data)