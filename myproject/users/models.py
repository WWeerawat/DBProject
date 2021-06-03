from django.db import models
from restaurants.models import Restaurant

# Create your models here.
class Role(models.Model):
    roleID = models.CharField(max_length=1, primary_key=True)
    roleName = models.CharField(max_length=10)

    class Meta:
        db_table = "role"

    def __str__(self):
        return self.roleID


class Member(models.Model):
    def genID():
        n = Member.objects.count()
        if n == None:
            return "M001"
        else:
            return "M" + str(n).zfill(3)

    memberID = models.CharField(max_length=10, default=genID, primary_key=True)
    roleID = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)
    resID = models.ForeignKey(
        Restaurant, null=True, blank=True, on_delete=models.SET_NULL
    )
    userName = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    fName = models.CharField(max_length=30)
    mName = models.CharField(max_length=30, blank=True)
    lName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    dob = models.DateField()
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    picture = models.URLField(max_length=200, blank=True)

    class Meta:
        db_table = "member"

    def __str__(self):
        return self.memberID

    def fullName(self):
        return self.fName + " " + self.lName

    def fullPhone(self):
        return self.tel[0:3] + "-" + self.tel[3:6] + "-" + self.tel[6:10]
