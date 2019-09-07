from django.shortcuts import render

from .models import Job

def home_view(request):
    asdf = Job.objects.all()
    return render(request, 'jobs/home.html', {'asdfjobs':asdf})