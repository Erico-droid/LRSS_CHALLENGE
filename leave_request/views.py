from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import LeaveRequest
from django.urls import reverse_lazy
from .forms import LeaveRequestForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leave_requests'] = LeaveRequest.objects.all()
        return context


class LeaveRequestCreateView(CreateView):
    model = LeaveRequest
    template_name = "create.html"
    form_class = LeaveRequestForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)


class LeaveRequestUpdateView(UpdateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = "update.html"  
    success_url = reverse_lazy('home')