from django.urls import path

from . import views

urlpatterns = {
    path('',views.members, name='members-home'),
    path('details/<int:id>', views.details, name="member-detail")
}