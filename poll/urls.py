from django.urls import path
from poll import views
#네임 스페이스
app_name = 'poll'  #app_name변수에 poll앱 저장

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000/poll/
    path('<int:question_id>/', views.detail, name='detail'),
]