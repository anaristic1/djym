"""djym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('', views.home, name='home'),
    path('exercises/', views.all_exercises, name='all_exercises'),
    path('exercises/<str:workout_type>', views.all_exercises, name='all_exercises'),
    path('exercise/<int:exercise_pk>', views.view_exercise, name='view_exercise'),
    path('exercise/<int:exercise_pk>/delete', views.delete_exercise, name='delete_exercise'),

    path('workouts/', views.all_user_workouts, name='all_workouts'),
    path('workouts/<int:workout_pk>', views.view_workout, name='view_workout'),
]
