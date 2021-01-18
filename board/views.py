from django.shortcuts import render, redirect
from django.http import Http404
from user.models import User
from .models import Board, Comment
from .forms import BoardForm, CommentForm

# Create your views here.


def board_list(request):
    boards = Board.objects.all().order_by('-id')

    return render(request, 'board/board_list.html', {'boards': boards})


def board_detail(request, pk):
    try:
        board = Board.objects.get(id=pk)
    except Board.DoesNotExist:
        raise Http404('게시물을 찾을 수 없습니다.')

    comments = Comment.objects.filter(board=board)

    if request.method == 'POST':
        if not request.session.get('user'):
            return redirect('/user/login')

        form = CommentForm(request.POST)

        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(id=user_id)

            comment = Comment(
                contents=form.data.get('contents'),
                writer=user, 
                board=board
            )

            comment.save()
    else:
        form = CommentForm()

    return render(request, 'board/board_detail.html', {'board': board, 'comments': comments, 'form': form})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login')

    if request.method == 'POST':
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(id=user_id)

            board = Board(
                title=form.data.get('title'),
                contents=form.data.get('contents'),
                writer=user
            )

            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board/board_write.html', {'form': form})
