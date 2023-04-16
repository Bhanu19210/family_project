from django.db import models

# Create your models here.
gender = (
     ('M','Male'),
     ('F','Female')
)
slug = (
      ('appala-naidu','appalanaidu'),
      ('brother-2','brother2'),
      ('pothala-1','pothala1'),
      ('venalapalem-2','sister2')
)

Gen_code = ((1,'one'),
            (2,'Two'),
            (3,'Three'),
            (4,'Three')


            )

class Genration_01(models.Model):
     title = models.CharField(max_length=200,null=True)
     name = models.CharField(max_length=100)
     gender = models.CharField(max_length=10,choices=gender)
     main_dp = models.ImageField(upload_to='dp',blank=True)
     partner = models.CharField(max_length=100, null=True , blank=True)
     partner_dp = models.ImageField(upload_to='dp',blank=True)
     slug = models.SlugField(max_length = 20,choices=slug)

     def __str__(self):
        return str(self.name)


class Genration_02(models.Model):
     parent = models.ForeignKey(Genration_01, on_delete=models.CASCADE)
     title_name = models.CharField(max_length=200,null=True)
     name = models.CharField(max_length=100)
     main_dp = models.ImageField(upload_to='dp',blank=True)
     partner = models.CharField(max_length=100, null=True , blank=True)  
     partner_dp = models.ImageField(upload_to='dp',blank=True)
     gen_code = models.IntegerField(choices=Gen_code)
     gender = models.CharField(max_length=10,choices=gender)
     whatsapp_no = models.BigIntegerField(null = True , blank= True)
     phone_no = models.BigIntegerField(null = True , blank= True)
     email = models.EmailField(null=True,blank=True)
     d_no = models.CharField(max_length=10,null=True)
     street = models.CharField(max_length=40)
     mandal = models.CharField(max_length=100)
     pin_code = models.CharField(max_length=100)
     district = models.CharField(max_length=100)
     co_state = models.CharField(max_length=100)
     parent_slug = models.SlugField(max_length = 20,choices=slug)
     slug = models.SlugField(default="",null=True) 
        
        
     def __str__(self):
                return str(self.name)
          

class Genration_03(models.Model):
     parent = models.ForeignKey(Genration_02, on_delete=models.CASCADE)
     title_name = models.CharField(max_length=200,null=True)
     name = models.CharField(max_length=100)
     main_dp = models.ImageField(upload_to='dp',blank=True)
     partner = models.CharField(max_length=100, null=True , blank=True)  
     partner_dp = models.ImageField(upload_to='dp',blank=True)
     gen_code = models.IntegerField(choices=Gen_code)
     gender = models.CharField(max_length=10,choices=gender)
     whatsapp_no = models.BigIntegerField(null = True , blank= True)
     phone_no = models.BigIntegerField(null = True , blank= True)
     email = models.EmailField(null=True,blank=True)
     d_no = models.CharField(max_length=10,null=True)
     street = models.CharField(max_length=40)
     mandal = models.CharField(max_length=100)
     pin_code = models.CharField(max_length=100)
     district = models.CharField(max_length=100)
     co_state = models.CharField(max_length=100)
     parent_slug = models.SlugField(max_length = 20,choices=slug)
     slug = models.SlugField(default="",null=True) 
        
        
     def __str__(self):
                return str(self.name)
     
class Genration_04(models.Model):
     parent = models.ForeignKey(Genration_03, on_delete=models.CASCADE)
     title_name = models.CharField(max_length=200,null=True,blank=True)
     name = models.CharField(max_length=100)
     main_dp = models.ImageField(upload_to='dp',blank=True)
     partner = models.CharField(max_length=100, null=True , blank=True)  
     partner_dp = models.ImageField(upload_to='dp',blank=True)
     gen_code = models.IntegerField(choices=Gen_code)
     gender = models.CharField(max_length=10,choices=gender)
     whatsapp_no = models.BigIntegerField(null = True , blank= True)
     phone_no = models.BigIntegerField(null = True , blank= True)
     email = models.EmailField(null=True,blank=True)
     d_no = models.CharField(max_length=10,null=True,blank=True)
     street = models.CharField(max_length=40,blank=True)
     mandal = models.CharField(max_length=100,blank=True)
     pin_code = models.CharField(max_length=100,blank=True)
     district = models.CharField(max_length=100,blank=True)
     co_state = models.CharField(max_length=100,blank=True)
     parent_slug = models.SlugField(max_length = 20,choices=slug)
     slug = models.SlugField(default="",null=True) 
        
        
     def __str__(self):
                return str(self.name)







class Author(models.Model):
    name = models.CharField(max_length=40)
    book = models.ManyToManyField('Book')

class Book(models.Model):
     name = models.CharField(max_length=40)