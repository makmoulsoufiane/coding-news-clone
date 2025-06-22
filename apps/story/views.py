from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import StoryForm
from .models import Story
# Create your views here.
def frontpage(request):
    return render(request, 'story/frontpage.html')



@login_required
def submit(request):
        form = StoryForm(request.POST)

        return render(request, 'story/submit.html', {'form': form})
