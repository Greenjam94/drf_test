from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from servers import views

urlpatterns = [
    path('servers/', views.ServerList.as_view()),
    path('servers/<int:pk>/', views.ServerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
