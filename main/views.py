from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname': 'BeSeller',
        'name': 'Fern Khairunnisha Adelia Aufar',
        'class': 'PBP B',
    }

    return render(request, "main.html", context)