import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import StoryForm
from .models import Story
# Create your views here.
def frontpage(request):
    date_form = datetime.datetime.now() - datetime.timedelta(days=1)

    stories = Story.objects.filter(created_at__gte=date_form).order_by('-number_of_votes')[0:30]
    return render(request, 'story/frontpage.html', {'stories': stories})


def newest(request):
    stories = Story.objects.all()[0:200]
    return render(request, 'story/newest.html', {'stories': stories})

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
