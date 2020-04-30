from django.shortcuts import render
from django.http import HttpResponse

def Form(request):
    return render(request, "dropbox/form.html", {})

def Upload(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f, na):
            with open('D:/code/dropbox/media/' + na , 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x, x.name)
    return HttpResponse("파일 업로드 완료 ~!")
