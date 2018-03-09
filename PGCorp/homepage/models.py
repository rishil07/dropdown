from django.db import models


class Flat(models.Model):
    image = models.FileField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    building_details = models.TextField(max_length=2000)  # Text space for owner to put details T
    rooms_available = models.CharField(max_length=50)
    about_owner = models.CharField(max_length=2000)
    nom = models.IntegerField()  # Numbers of members
    owner_name = models.CharField(max_length=50)
    owner_contact = models.CharField(max_length=10)
    address = models.CharField(max_length=250)

    def __str__(self):
        return 'Name : '+str(self.owner_name)+'\nAddress : '+str(self.address)

