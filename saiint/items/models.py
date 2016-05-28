from django.db import models

# Create your models here.
class ItemCategory (models.Model):
    furniture_type = models.CharField(max_length = 250) #Plastic, Wooden, Steel
    # furniture_for = models.CharField(max_length = 250) #Living room, Bedroom, DiningHall, StudyRoom

    def __str__(self):
        return self.furniture_type
        # return "Furniture is for " + self.furniture_for + " and is " + self.furniture_type

class ItemName (models.Model):
    itemcategory = models.ForeignKey(ItemCategory, on_delete = models.CASCADE)
    item_name = models.CharField(max_length = 250)
    item_price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return self.item_name + ' - ' + str(self.itemcategory)
