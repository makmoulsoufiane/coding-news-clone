from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import StoryForm
from .models import Story
# Create your views here.
def frontpage(request):
    return render(request, 'story/frontpage.html')



@login_required
def submit(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)

        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()

            return redirect('frontpage')  # Redirect to the frontpage after submission
    else:
        form = StoryForm()

    return render(request, 'story/submit.html', {'form': form})
