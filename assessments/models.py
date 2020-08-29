from django.db import models
from utils.unit import Unit as Unit_obj
from utils.unit import Assessment as Assessment_obj
from utils.unit import Schedule as Schedule_obj
from utils.unit import Topic as Topic_obj


class DB_Unit(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    has_final = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    # save a python unit object to the database
    def save_from_obj(self, unit_obj):
        self.name = unit_obj.name
        self.code = unit_obj.code
        self.has_final = unit_obj.has_final
        self.active = True
        self.save()

        for assessment_obj in unit_obj.list_of_assessments:
            if DB_Assessment.objects.filter(unit=self, description_title=assessment_obj.description_title).count() > 0:
                assessment_db = DB_Assessment.objects.get(
                    unit=self, description_title=assessment_obj.description_title)
            else:
                assessment_db = DB_Assessment()
            assessment_db.unit = self
            assessment_db.type_str = assessment_obj.type_str
            assessment_db.description_title = assessment_obj.description_title
            assessment_db.description_body = assessment_obj.description_body
            assessment_db.weight = assessment_obj.weight
            assessment_db.due_str = assessment_obj.due_str
            assessment_db.due_date = assessment_obj.due_date
            assessment_db.is_final = assessment_obj.is_final
            assessment_db.length = assessment_obj.length
            assessment_db.active = True
            assessment_db.save()
        for schedule_obj in unit_obj.list_of_schedules:
            if DB_Schedule.objects.filter(unit=self, wk_str=schedule_obj.wk_str).count() > 0:
                schedule_db = DB_Schedule.objects.get(
                    unit=self, wk_str=schedule_obj.wk_str)
            else:
                schedule_db = DB_Schedule()
            schedule_db.unit = self
            schedule_db.wk_str = schedule_obj.wk_str
            schedule_db.active = True
            schedule_db.save()

            for topic_obj in schedule_obj.list_of_topics:
                if DB_Topic.objects.filter(schedule=schedule_db, topic_str=topic_obj.topic_str).count() > 0:
                    topic_db = DB_Topic.objects.get(
                        schedule=schedule_db, topic_str=topic_obj.topic_str)
                else:
                    topic_db = DB_Topic()
                topic_db.schedule = schedule_db
                topic_db.topic_str = topic_obj.topic_str
                topic_db.learning_str = topic_obj.learning_str
                topic_db.active = True
                topic_db.save()

    # returns a python object constructed from the unit database object
    def obj(self):
        unit_obj = Unit_obj()
        unit_obj.name = self.name
        unit_obj.code = self.code
        unit_obj.has_final = self.has_final

        for assessment_db in list(DB_Assessment.objects.filter(unit=self)):
            assessment_obj = Assessment_obj()
            assessment_obj.unit = unit_obj
            assessment_obj.type_str = assessment_db.type_str
            assessment_obj.description_title = assessment_db.description_title
            assessment_obj.description_body = assessment_db.description_body
            assessment_obj.weight = assessment_db.weight
            assessment_obj.due_str = assessment_db.due_str
            assessment_obj.is_final = assessment_db.is_final
            print("Here")
            print(assessment_obj.due_str.lower())
            if ('formal' in assessment_obj.due_str.lower()):
                unit_obj.has_final = True
                assessment_obj.is_final = True
                print("Has a final exam!!!")

            assessment_obj.due_date = assessment_db.due_date
            assessment_obj.length = assessment_db.length
            unit_obj.list_of_assessments.append(assessment_obj)

        for schedule_db in list(DB_Schedule.objects.filter(unit=self)):
            schedule_obj = Schedule_obj()
            schedule_obj.unit = unit_obj
            schedule_obj.wk_str = schedule_db.wk_str
            unit_obj.list_of_schedules.append(schedule_obj)

            for topic_db in list(DB_Topic.objects.filter(schedule=schedule_db)):
                topic_obj = Topic_obj()
                topic_obj.schedule = schedule_obj
                topic_obj.topic_str = topic_db.topic_str
                topic_obj.learning_str = topic_db.learning_str
                schedule_obj.list_of_topics.append(topic_obj)
        return unit_obj


class DB_Assessment(models.Model):
    unit = models.ForeignKey(DB_Unit, on_delete=models.CASCADE)
    type_str = models.CharField(max_length=200)
    description_title = models.CharField(max_length=200)
    description_body = models.CharField(max_length=200, null=True)
    weight = models.CharField(max_length=200)
    due_str = models.CharField(max_length=200)
    due_date = models.CharField(max_length=200, null=True)
    is_final = models.BooleanField(default=False)
    length = models.CharField(max_length=200)
    active = models.BooleanField(default=False)


class DB_Schedule(models.Model):
    unit = models.ForeignKey(DB_Unit, on_delete=models.CASCADE)
    wk_str = models.CharField(max_length=200)
    active = models.BooleanField(default=False)


class DB_Topic(models.Model):
    topic_str = models.CharField(max_length=200)
    learning_str = models.CharField(max_length=200)
    schedule = models.ForeignKey(DB_Schedule, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
