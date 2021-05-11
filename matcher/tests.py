from django.test import TestCase
from django.utils import timezone
from matcher.models import Skill, Job, Candidate
from matcher.Utilities.Finder import candidateFinderBySkill


def create_skill(title):
    return Skill.objects.create(title=title)


def create_candidte(pk, name, title, skills):
    candidate = Candidate.objects.create(pk=pk, name=name, title=title)
    for skill in skills:
        candidate.skills.add(skill)
    return candidate


def create_job(pk, title, skills):
    job = Job.objects.create(pk=pk, title=title, pub_date=timezone.now())
    for skill in skills:
        job.skills.add(skill)
    return job


class FinderModelTests(TestCase):

    def setUp(self):
        skill1 = create_skill("a")
        skill2 = create_skill("b")
        skill3 = create_skill("c")
        skill4 = create_skill("d")
        create_job(1, "aa", [skill1, skill2])
        create_job(2, "aa", [skill4])
        create_job(3, "bb", [skill4])
        create_job(4, "cc", [skill1, skill2, skill3, skill4])
        create_candidte(1, "name1", "aa", [skill1, skill2])
        create_candidte(2, "name2", "aa", [skill1])
        create_candidte(3, "name3", "aa", [skill2])
        create_candidte(4, "name4", "aa", [skill3])
        create_candidte(5, "name1c", "cc", [skill1, skill2, skill3])
        create_candidte(6, "name2c", "cc", [skill1, skill3, skill4])
        create_candidte(7, "name3c", "cc", [skill2, skill3])
        create_candidte(8, "name4c", "cc", [skill3])

    def test_CandidateFinder_PerfectMatch(self):
        job_pk = Job.objects.get(pk=1).pk
        candidate = Candidate.objects.get(pk=1)
        self.assertEqual(candidateFinderBySkill(job_pk, 1), [(2, candidate)])

    def test_CandidateFinder_no_match_title(self):
        job_pk = Job.objects.get(pk=3).pk
        self.assertEqual(candidateFinderBySkill(job_pk, 1), [])

    def test_CandidateFinder_no_match_skills(self):
        job_pk = Job.objects.get(pk=2).pk
        self.assertEqual(candidateFinderBySkill(job_pk, 1)[0][0], 0)

    def test_CandidateFinder_n_most_fits(self):
        job_pk = Job.objects.get(pk=4).pk
        n = 3
        candidate5 = Candidate.objects.get(pk=5)
        candidate6 = Candidate.objects.get(pk=6)
        candidate7 = Candidate.objects.get(pk=7)
        self.assertEqual(candidateFinderBySkill(job_pk, n), [(2, candidate7), (3, candidate6), (3, candidate5)])