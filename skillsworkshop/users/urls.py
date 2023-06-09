from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


# from this directory import ALL Views and not one by one

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customuser-list'),
    # url / user / user id number
    path('<int:pk>/', views.CustomUserDetail.as_view(),
         name='customuser-detail-update'),
    path('session/', views.CustomUserSessionView.as_view(),
         name='customuser-session-view'),
    path('mentor-list/', views.MentorListView.as_view(),
         name='mentor-list'),
        path('mentee-list/', views.MenteeListView.as_view(),
         name='mentee-list'),
    # path('register', views.CustomUserRegisterAPIView.as_view(),
    #      name='customuser-register')

]
