from django.shortcuts import render
from django.http import Http404
from .models import Board

# Create your views here.


def board_list(request):
    boards = Board.objects.all().order_by('-id')

    return render(request, 'board/board_list.html', {'boards': boards})


def board_detail(request, pk):
    try:
        board = Board.objects.get(id=pk)
    except Board.DoesNotExist:
        raise Http404('게시물을 찾을 수 없습니다.')

    return render(request, 'board/board_detail.html', {'board': board})