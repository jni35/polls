from django.http import HttpResponse
from django.shortcuts import render
from poll.models import Question

#인덱스페이지
def index(request):
    # db에 있는 모든 데이터 조회하기(select)
    question_list = Question.objects.all()
    return render(request, 'poll/index.html', {'question_list':question_list})
    #return HttpResponse("Welcome~ 환영합니다!!")

#상세페이지
def detail(request, question_id):
    # 해당 id(순번)로 자료 조회(select)
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/detail.html', {'question':question})

#투표하기
def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    # 선택 자료 넘겨 받음
    try:
        choice_id = request.POST['choice']
        sel_choice = question.choice_set.get(id=choice_id)
    except:
        return render(request, 'poll/detail.html', {'question':question, 'error':'선택을 확인해 주세요.'})
    else:
        sel_choice.votes = sel_choice.votes + 1
        sel_choice.save()   # db에 저장
        return render(request, 'poll/vote_result.html', {'question':question})