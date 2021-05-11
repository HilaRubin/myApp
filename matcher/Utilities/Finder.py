from _heapq import heappush, heappop
from matcher.models import Candidate, Job


def candidateFinderBySkill(job_pk, size=2):
    job_title = Job.objects.get(pk=job_pk)
    required_skills = [skill for skill in job_title.skills.all()]
    candidates = Candidate.objects.filter(title=job_title)
    required_dict = {required_skills[i]: 1 for i in range(0, len(required_skills))}

    h = []
    for candidate in candidates:
        heappush(h, (candidateMathcing(candidate, required_dict), candidate))
        if len(h) > size:
            heappop(h)
    h_list = []
    while len(h) > 0:
        h_list.append(heappop(h))
    return h_list


def candidateMathcing(candidate, requirements):
    candi_skills = [val for val in candidate.skills.all()]
    candidate_grade = 0
    for skill in candi_skills:
        if skill in requirements:
            candidate_grade += 1
    return candidate_grade
