from django.urls import path
from .views import job_index, job_detail, candidate_results


urlpatterns = [
    path("", job_index.as_view(), name="HomePage"),
    path("<int:pk>/", job_detail.as_view(), name="job_detail"),
    path("candidate_results/<int:pk>/", candidate_results, name="candidate_results"),
]