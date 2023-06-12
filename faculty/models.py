from django.db import models

# Create your models here.


class Streams(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
        
class Faculty(models.Model):
    First_name = models.CharField(max_length=500)
    Last_name = models.CharField(max_length=500)
    Employee_id = models.CharField(max_length=500)
    Employee_designation = models.CharField(max_length=500)
    Employee_qualification= models.CharField(max_length=500)
    Employee_department= models.ForeignKey(Department, on_delete=models.DO_NOTHING,unique=False)
    Employee_experience= models.CharField(max_length=500)
    Employee_phoneno = models.CharField(max_length=500)
    Employee_email = models.EmailField(max_length=500)

    def __str__(self):
        return self.First_name


class Student(models.Model):
    First_name = models.CharField(max_length=500)
    Last_name = models.CharField(max_length=500)
    Student_id = models.CharField(max_length=500)
    Student_course = models.CharField(max_length=500)
    Student_sem = models.CharField(max_length=500)
    Join_year = models.DateField()
    Pass_year = models.DateField()
    Student_phoneno = models.CharField(max_length=500)
    Student_email = models.EmailField(max_length=500)

    def __str__(self):
        return self.First_name


class Domain(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Projects(models.Model):
    Title = models.CharField(max_length=500)
    Domain = models.ForeignKey(Domain, on_delete=models.DO_NOTHING,unique=False)
    TechTechnology = models.CharField(max_length=500)
    Github = models.CharField(max_length=500)
    Documentation = models.FileField(upload_to='projects/pdf')
    PPt = models.FileField(upload_to='projects/ppt')
    Guide = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING,unique=False)


    def __str__(self):
        return self.Title


class InventoryCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class InventorySubCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class InventoryStatus(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    category = models.ForeignKey(InventoryCategory, on_delete=models.DO_NOTHING,unique=False)
    subcategory = models.ForeignKey(InventorySubCategory, on_delete=models.DO_NOTHING,unique=False)
    stream = models.ForeignKey(Streams, on_delete=models.DO_NOTHING,unique=False)
    sem = models.IntegerField(default=1)
    quantity = models.IntegerField()
    distributed = models.IntegerField()
    date = models.DateField()
    status = models.ForeignKey(InventoryStatus, on_delete=models.DO_NOTHING,unique=False)
    def __str__(self):
        return str(self.id)





