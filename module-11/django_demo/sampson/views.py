from django.http import HttpResponse


def index(request):
    return HttpResponse("Dholariya says Hello!")
