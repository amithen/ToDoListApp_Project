from django.urls import path
from . import views
app_name = 'todo'
urlpatterns = [
    path('', views.todohome,name='home'),
    path('delete/<str:id>/',views.deleteview,name='delete'),
    path('update/<str:id>/',views.updateview,name='update'),
]
