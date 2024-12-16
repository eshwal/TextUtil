from django.shortcuts import render
from django.http import HttpResponse


import string

# Create your views here.


def index(request):
    return render(request,'textUtilApp\index.html')


def analyze(request):
    text = request.POST.get("text",'default')
    print(request.POST.getlist("selectoption"))
    optionlist = request.POST.getlist("selectoption",[])
    print(optionlist)
    count = 0
    
    if text =="":
        return HttpResponse("Text should not be blank!!")

    if optionlist == []:
        return HttpResponse("Select any option to perform any operation!!")


    for i in optionlist:
        if i == 'removepunc':
            puncString = string.punctuation
            analyzedtext = ''
            for  i in text:
                if i not in puncString:
                    analyzedtext += i
            text = analyzedtext

        if i == 'convertcapital':
            uppertext = text.upper()
            text = uppertext

        if i == 'convertlower':
            lowertext = text.lower()
            text = lowertext

        if i == 'charcount':
            count = len(text)
            count = count

    if count !=0:
        return render(request,'textUtilApp/analyse.html',{'text':text,'count':count})
    return render(request,'textUtilApp/analyse.html',{'text':text})
    


