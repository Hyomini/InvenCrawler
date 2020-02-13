from django.urls import path
from parsed_data import views


urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('members/<int:pk>', views.MemberDetailView.as_view(), name='member-detail'),
]