from django.urls import path

from . import views


app_name = "animals"

urlpatterns = [
    path('animals/', views.AnimalView.as_view()),
    path('animals/<int:pk>', views.AnimalView.as_view()),

    path('families/', views.FamilyView.as_view()),

    path('move-types/', views.MoveTypeView.as_view()),

    path('protection-statuses/', views.ProtectionStatusView.as_view())
    
]