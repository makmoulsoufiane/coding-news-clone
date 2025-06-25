from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def userprofile(request, username):
    user = get_object_or_404(User, username=username)

    number_of_votes = 0

    for story in user.stories.all():
        number_of_votes = number_of_votes + (story.number_of_votes - 1)

    return render(request, 'userprofile/userprofile.html', {'user': user, 'number_of_votes': number_of_votes})
