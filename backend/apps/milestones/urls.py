from django.urls import path
from .views import MilestoneView

urlpatterns = [
    path('', MilestoneView.as_view(), name='milestone_view')
]