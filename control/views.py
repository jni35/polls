from django.shortcuts import render

def index(request):
    return render(request, 'control/index.html')

def register(request):
    if request.method == "POST":
        userid = request.POST['userid']
        return render(request, 'control/reg_result.html', {'userid':userid})
        # html로 렌더링할때 딕셔너리구조로 자료를 보냄
    else:   # GET 이면
        return render(request, 'control/register.html')

