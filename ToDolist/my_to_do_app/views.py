from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# index 페이지로 돌아가기 위한 reverse를 임포트 합니다
from django.urls import reverse

# Create your views here.
def index( request ):
    # DB의 내용을 브라우저에 전달하기 위한 코드를 추가/
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo( request ):
# 사용자가 입력한 할 일을 잘 받아 오는지 확인
# 입력값 전달은 POST 방식으로, 'todoContent'변수를 통해서 전달이 될겁니다.

# 사용자가 입력한 할 일을 잘 받아 오는지 확인
# 입력값 전달은 POST 방식으로, 'todoContent' 변수를 통해서 전달이 될겁니다. 
#  user_input_str = request.POST['todoContent']
#  return HttpResponse(f'사용자가 입력한 값: {user_input_str}')
    user_input_str = request.POST['todoContent']
# models.py 에서 정의된 클래스를 이용해서 전달받은 값을 DB에 저장 합니다.
    new_todo = Todo( content = user_input_str)
    new_todo.save()
    
    return HttpResponseRedirect(reverse('index'))