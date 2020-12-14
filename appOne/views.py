from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def analyze(request):

    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    removespace = request.POST.get('removespace','off')
    capitalize = request.POST.get('capitalize','off')
    charcount = request.POST.get('charcount','off')

    if removepunc == 'on':
        marks = '''!@#$%^&*<>?'''
        analyzed = ""
        for char in djtext:
            if char not in marks:
                analyzed += char
        params = {"action":"Removed Punctuations","resultant_text":analyzed}
        return render(request,'resultant.html',params)
    elif removespace == 'on':
        import re
        line = djtext
        resultant = re.sub(' +'," ",line)
        params = {"action": "Removed Spaces", "resultant_text": resultant}
        return render(request, 'resultant.html', params)
    elif capitalize == 'on':
        line = djtext
        analyzed=''
        for c in line:
            analyzed +=c.capitalize()
        '''analyzed = line.capitalize()'''
        params = {"action": "Capitalize the String", "resultant_text": analyzed}
        return render(request, 'resultant.html', params)
    elif charcount == 'on':
        line = djtext
        count = 0
        for c in line:
            count+=1
        analyzed=f"Total number of characters are {count}"
        params = {"action": "Character Count", "resultant_text": analyzed}
        return render(request, 'resultant.html', params)


'''def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse('Remove Punctuation')

def removespace(request):
    return HttpResponse('Remove Space.')

def capitalize(request):
    return HttpResponse('Capitalize First Character..')

def charcount(request):
    return HttpResponse('Character Count..')'''


