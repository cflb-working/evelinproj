from django.db import models

# Create your models here.
class Annotation(models.Model):
    annotation = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.annotation}"

class Address(models.Model):

    TYPE_ADDRESS = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('destination', 'Destination'),
    ]

    typeAddress = models.CharField(choices=TYPE_ADDRESS, max_length=50) 
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    annotation = models.ForeignKey('Annotation', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.neighborhood}, {self.zipCode}, {self.city}, {self.state}, {self.country}"


class Client(models.Model):
    name = models.CharField(max_length=50)
    companyAddress = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='companyAddress')
    shippingAddress = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='shippingAddress')
    residentialAddress = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='residentialAddress', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    

