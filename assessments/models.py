from django.db import models


class DB_Unit(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    has_final = models.BooleanField()


class DB_Assessment(models.Model):
    unit = models.ForeignKey(DB_Unit, on_delete=models.CASCADE)
    type_str = models.CharField(max_length=200)
    description_title = models.CharField(max_length=200)
    description_body = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    due_str = models.CharField(max_length=200)
    due_date = models.CharField(max_length=200)
    is_final = models.BooleanField()
    length = models.CharField(max_length=200)


class DB_Schedule(models.Model):
    wk_str = models.CharField(max_length=200)


class DB_Topic(models.Model):
    topic_str = models.CharField(max_length=200)
    learning_str = models.CharField(max_length=200)
    schedule = models.ForeignKey(DB_Schedule, on_delete=models.CASCADE)
