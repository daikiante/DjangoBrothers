from django.db import models

# 人
class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# チーム
class Team(models.Model):
    name = models.CharField(max_length=50)
    member = models.ManyToManyField(
        "Person",
        through="PersonTeam"
        )

    def __str__(self):
        return self.name

# 人とチームの中間テーブル
class PersonTeam(models.Model):
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    joined_date = models.DateField(auto_now=True)
    reason = models.CharField(max_length=50)


'----Foreign Key----'


class Friends(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Message(models.Model):
    froma = models.ForeignKey("Friends", related_name='froma', null=True, blank=True, on_delete=models.CASCADE)
    toa = models.ForeignKey("Friends", related_name='toa', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()