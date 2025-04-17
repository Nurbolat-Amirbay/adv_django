from django.urls import path
from . import views

urlpatterns = [
    path('resumes/', views.ResumeListView.as_view(), name='resume-list'),
    path('resumes/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
    path('resumes/upload/', views.ResumeUploadView.as_view(), name='resume-upload'),
    path('resumes/<int:pk>/analysis/', views.ResumeAnalysisView.as_view(), name='resume-analysis'),
    path('resumes/<int:pk>/feedback/', views.ResumeFeedbackView.as_view(), name='resume-feedback'),
    path('skills/', views.SkillListView.as_view(), name='skill-list'),
    path('resumes/<int:resume_id>/experiences/', views.ExperienceListView.as_view(), name='experience-list'),
    path('resumes/<int:resume_id>/educations/', views.EducationListView.as_view(), name='education-list'),
] 