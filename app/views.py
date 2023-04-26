from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *

def insert_topic(request):

    if request.method=='POST':
        topic=request.POST.get('tn')
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('data submited successfully')

    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['n']
        url=request.POST['u']

        T=Topic.objects.get(topic_name=tn)

        WO=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        WO.save()
        return HttpResponse('data submited successfully')


    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    LAO=Webpage.objects.all()
    d={'access':LAO}

    if request.method=='POST':
        name=request.POST.get('n')
        author=request.POST.get('a')
        date=request.POST.get('d')

        WO=Webpage.objects.get(name=name)

        AO=Accessrecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('ccess Record Data submited successfully')

    return render(request,'insert_accessrecord.html',d)





def retrive_topic(request):

    LTO=Topic.objects.all()
    d={'topic':LTO}

    if request.method=='POST':
        tn=request.POST.getlist('tn')
        topicquary=Topic.objects.none()

        for i in  tn:
            topicquary=topicquary|Topic.objects.filter(topic_name=i)
        tdn={'topic':topicquary}
        return render(request,'display_topic.html',tdn)
    
    return render(request,'retrive_topic.html',d)

def retrive_topic_checkbox(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}

    return render(request,'retrive_topic_checkbox.html',d)


def retrive_topic_radio(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}
    
    return render(request,'retrive_topic_radio.html',d)





def retrive_webpage(request):
    LWO=Webpage.objects.all()
    d={'webe':LWO}

    if request.method=='POST':
        webobj=request.POST.getlist('tn')
        
        webquary=Webpage.objects.none()

        for i in webobj:
            webquary=webquary|Webpage.objects.filter(name=i)

        d1={'topic':webquary}
        return render(request,'display_webpage.html',d1)

    return render(request,'retrive_webpage.html',d)



def retrive_webpage_checkbox(request):
    WO=Webpage.objects.all()
    d={'web':WO}

    return render(request,'retrive_webpage_checkbox.html',d)

def retrive_webpage_radio(request):
    WO=Webpage.objects.all()
    d={'web':WO}

    return render(request,'retrive_webpage_radio.html',d)







def retrive_accessrecord(request):
    LAO=Accessrecord.objects.all()
    d={'access':LAO}

    if request.method=='POST':
        
        name=request.POST.getlist('n')
        accessquary=Accessrecord.objects.none()

        for i in name:
            accessquary=accessquary|Accessrecord.objects.filter(author=i)
        
        d={'access':accessquary}
        return render(request,'display_accesrecord.html',d)


    return render(request,'retrive_accessrecord.html',d)


def retrive_accessrecord_checkbox(request):
    LOA=Accessrecord.objects.all()
    d={'access':LOA}

    return render(request,'retrive_accessrecord_checkbox.html',d)

def retrive_accessrecord_radio(request):
    LOA=Accessrecord.objects.all()
    d={'access':LOA}

    return render(request,'retrive_accessrecord_radio.html',d)



def update_topic(request):

    if request.method=='POST':
        topic=request.POST.get('tn')
        up_topic=request.POST.get('upd')
        TO=Topic.objects.update_or_create(topic_name=up_topic)
        
        return HttpResponse('data updated successfully')

    return render(request,'update_topic.html')

def update_webpage(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['n']
        url=request.POST['u']

        T=Topic.objects.get(topic_name=tn)

        WO=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        WO.save()
        return HttpResponse('Webpage data updated successfully')


    return render(request,'update_webpage.html',d)



def insert_accessrecord(request):
    LAO=Webpage.objects.all()
    d={'access':LAO}

    if request.method=='POST':
        name=request.POST.get('n')
        author=request.POST.get('a')
        date=request.POST.get('d')

        WO=Webpage.objects.get(name=name)

        AO=Accessrecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('ccess Record Data submited successfully')

    return render(request,'insert_accessrecord.html',d)

