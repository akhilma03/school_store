from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class Department(models.Model):
    
    Name = models.CharField(max_length=100)
    is_active= models.BooleanField(default=True)
    
    def __str__(self) :
        return self.Name
    
class Course(models.Model):
    Name=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    is_active= models.BooleanField(default=True)
    def __str__(self) :
        return self.Name    
    
class NewEntery(models.Model):
    name = models.CharField(max_length=100)
    dob= models.DateField()
    age =models.IntegerField()
    gender=models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address =models.TextField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    course =  models.ForeignKey(Course,on_delete=models.CASCADE,null=True) 
    choice=(('Enquiry','Enquiry'),('Place_Order','Place_Order'),('Return','Return'))
    purpose=models.CharField(max_length=100,choices=choice)
    choicem=(('NoteBook','NoteBook'),('Exam_Paper','Exam_Paper'),('Pen','Pen'),('Drafter','Drafter'),('Pencil','Pencil'))
    materials=MultiSelectField(choices=choicem,max_choices=5,
                                 max_length=15)
    def __str__(self) :
        return self.name