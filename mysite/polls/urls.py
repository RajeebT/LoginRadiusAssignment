from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'polls'
urlpatterns = [

    path('',views.indexView,name="home"),
    path('dashboard',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView, name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout_url"),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    ]

    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/






