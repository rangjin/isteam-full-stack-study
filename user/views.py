from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .forms import RegisterForm

# Create your views here.


def index(request):
    # return HttpResponse("Hello World!!!!!!!!")
    return render(request, 'index.html')


def register(request):
    # POST(사용자가 정보를 입력했을 때)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # 유효성 검사 성공(문제 없음)시
        if form.is_valid():
            user = User(
                name=form.data.get('name'), 
                email=form.data.get('email'), 
                password=form.data.get('password')
            )

            user.save()

            return redirect('/')
        # 유효성 검사 실패시
        else:
            # render 함수를 통해 뷰와 템플릿을 연결하고 템플릿에 정보를 넘겨줄 수 있음
            return render(request, "register.html", {'form': form})
    # GET(사용자가 처음 들어와 아직 정보를 입력하기 전)
    else:
        form = RegisterForm()
        return render(request, "register.html", {'form': form})