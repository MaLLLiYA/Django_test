from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'


class Bookinfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'
        # verbose_name = '书籍管理'


class Peopleinfo(models.Model):
    # ordered dict
    GENDER_CHOICE = (
        (0, 'female'),
        (1, 'male')
    )
    name = models.CharField(max_length=20, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0)
    description = models.CharField(max_length=100)
    is_delete = models.BooleanField()
    book = models.ForeignKey(Bookinfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'peopleinfo'
