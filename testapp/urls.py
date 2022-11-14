from django.urls import path
from.import views
urlpatterns = [
     path('', views.fun, name='fun'),
     path('fun1', views.fun1, name='fun1'),
     path('add', views.addition, name='add'),
     path('details/<int:id>/',views.details,name='details')

]
