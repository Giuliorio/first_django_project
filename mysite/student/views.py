from django.http import HttpResponse

# Create your views here.

data = {
    "Name": "Giulio Riondino",
    "Track": "Backend(Python)",
    "Message": "Hi mentor, you are doing a great job"
}

def index(request):
    return HttpResponse(data.items())