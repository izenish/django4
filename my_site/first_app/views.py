import imp
from unittest import result
from django.http import HttpResponseNotFound,Http404, HttpResponseRedirect
from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse
articles={
    'sports':'sports page',
    'finance':'finance page',
    'politics':'politics page',

}

# Create your views here.
def news_view(request,topic):
    try:
        result=articles[topic]
        return HttpResponse(articles[topic])
    except:
        # result='No page for that topic'
        # return HttpResponseNotFound(result)
        raise Http404("404 Generic Error")

def num_page_view(request,num_page):
    topic_list=list(articles.keys())
    topic=topic_list[num_page]
    webpage=reverse('topic-page',args=[topic])
    return HttpResponseRedirect(webpage)



def finance_view(request):
    return HttpResponse("Finance View")