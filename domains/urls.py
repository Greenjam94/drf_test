from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from domains import views

urlpatterns = [
    path('domains/', views.domain_list),
    path('domains/<int:pk>/', views.domain_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
