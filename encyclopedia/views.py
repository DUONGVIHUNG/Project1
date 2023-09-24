from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

from markdown2 import Markdown

import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    markdowner = Markdown()
    if util.get_entry(name)==None:
        return render(request,"encyclopedia/errorPage.html")
    return render(request, "encyclopedia/entry.html",{
        "name": name,
        "content": markdowner.convert(util.get_entry(name))

    }) 

def query(request):
    listOfEntries = util.list_entries()
    results = []

    for page in listOfEntries:
        if request.GET["q"].upper() == page.upper():
            print(page)
            return entry(request,request.GET["q"])
        elif request.GET["q"].upper() in page.upper():
            print(page)
            results.append(page)
    return render(request,"encyclopedia/searchResults.html",{
                "results" : results          
    })
    # return entry(request,request.GET["q"])


def createpage(request):
    return render(request, "encyclopedia/create.html")

def save(request):
    print(request.POST)
    title = request.POST["title"]
    content=request.POST["context"]
    pages = []
    for page in util.list_entries():
        pages.append(page.upper())
    if title.upper() in pages and request.POST["state"] == "created":
        return render(request,"encyclopedia/saveError.html")
    elif not title.upper() in pages or request.POST["state"] == "edit": 
        util.save_entry(title, content)
        return entry(request,request.POST["title"])
    
def edit(request):
    title = request.POST["title"]
    context = util.get_entry(title)
    return render(request, "encyclopedia/edit.html",{
        "content" : context,
        "title" : title
    })

def randomness(request):
    listOfEntries = util.list_entries()
    randomIndex = random.randint(0, len(listOfEntries)-1)
    return entry(request,listOfEntries[randomIndex])