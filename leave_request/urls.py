from django.urls import path
from .views import HomeView, LeaveRequestCreateView, LeaveRequestUpdateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("leave/create/", LeaveRequestCreateView.as_view(), name="leave-create"),
    path("leave/update/<int:pk>/", LeaveRequestUpdateView.as_view(), name="leave-update"),
]
