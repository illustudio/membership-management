from django.shortcuts import render


def index(request):
    context = {'text': "text string"}
    return render(request, 'membership/index.html', context)
