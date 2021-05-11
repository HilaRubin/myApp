from django.shortcuts import render
from django.views.generic import ListView, DetailView
from matcher.Utilities.Finder import candidateFinderBySkill
from matcher.models import Job


class job_index(ListView):
    model = Job
    context_object_name = 'job_list'
    queryset = Job.objects.order_by('-pub_date')
    template_name = 'matcher/HomePage.html'


class job_detail(DetailView):
    model = Job
    template_name = 'matcher/job_detail.html'
    context_object_name = 'job_details'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in skills required
        context['skills'] = ', '.join([s.title for s in context['job_details'].skills.all()])
        return context


class candidate_display():
    def __init__(self, candi_pk, candi_name, candi_skills, candi_grade):
        self.c_pk = candi_pk
        self.c_name = candi_name
        self.c_skills = candi_skills
        self.c_grade = candi_grade


def candidate_results(request, pk):
    if request.method == "POST":
        job = Job.objects.get(pk=pk)
        skills = [s.title for s in job.skills.all()]
        candidates = candidateFinderBySkill(pk, 3)
        candidates_details = []
        for candi in reversed(candidates):
            candidates_details.append(
                candidate_display(candi[1].pk, candi[1].name, ', '.join([s.title for s in candi[1].skills.all()]),
                                  candi[0]))
    return render(request, 'matcher/candidate_results.html', {
        'job': job,
        'skills': skills,
        'candidates_details': candidates_details
    })
