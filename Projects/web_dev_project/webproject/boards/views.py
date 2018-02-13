from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Board, Topic, Post
from datetime import datetime

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    #do something
    board = get_object_or_404(Board,pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        time = datetime.now()
        user = User.objects.first() # to do : get the logged in user
        user_topic = Topic.objects.create(subject=subject,last_update=time,board=board,starter=user)
        post = Post.objects.create(message=message,topics=user_topic,created_by=user)

        return redirect('board_topics', pk=board.pk) # to do: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})
