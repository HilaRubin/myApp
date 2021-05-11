from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    skills = models.ManyToManyField("Skill")

    def __str__(self):
        return self.title


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill, null=True, blank=True)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return other

    def __ge__(self, other):
        return other