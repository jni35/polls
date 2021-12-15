from django.urls import path
#네임 스페이스
from control import views

app_name = 'control'  #app_name변수에 poll앱 저장

urlpatterns = [
    path('', views.index, name='index'),    # 127.0.0.1:8000/poll/
    path('register/', views.register, name='register')
]