from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('token/access/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('notes/', views.NotesListView.as_view()),
    path('notes/<int:pk>/', views.NotesDetailView.as_view()),
]
