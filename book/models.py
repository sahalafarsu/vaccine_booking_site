# from django.db import models
#
# # Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='district'
        verbose_name_plural='districts'

    def get_url(self):
        return reverse('centers_by_district',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Center(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('centDistdetail',args=[self.district.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='center'
        verbose_name_plural='centers'

    def __str__(self):
            return '{}'.format(self.name)

class People(models.Model):
    boolChoice = (
        ("M", "Male"), ("F", "Female")
    )
    first_name=models.CharField(max_length=250,unique=True)
    last_name = models.CharField(max_length=250, unique=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=boolChoice)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    house_name = models.CharField(max_length=250, unique=True)
    city = models.CharField(max_length=250, unique=True)
    district = models.CharField(max_length=250, unique=True)
    pincode = models.CharField(max_length=6, unique=True)


    def __str__(self):
            return '{}'.format(self.first_name)