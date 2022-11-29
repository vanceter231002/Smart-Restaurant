from django.db import models,IntegrityError

class Category(models.Model):
    name=models.CharField(max_length=100)
    rank=models.PositiveIntegerField(default=0)
    def save(self,*args,**kwargs):
        if self.rank==0:
            self.rank=max([item.rank for item in Item.objects.all()])+1
        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.name}"
        
class Item(models.Model):
    name=models.CharField(max_length=100)
    image_link=models.CharField(max_length=1000)
    price=models.PositiveIntegerField(default=0)
    is_non_veg=models.BooleanField(default=False)
    contains_egg=models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    rank=models.PositiveIntegerField(default=0)
    def save(self,*args,**kwargs):
        if self.rank==0:
            self.rank=max([item.rank for item in Item.objects.all()])+1
        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    table_no=models.PositiveIntegerField()
    total_price=models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if list(self.itemquantity_set.all()):
            self.total_price=sum([x.price for x in self.itemquantity_set.all()])
        super().save(*args, **kwargs)

class ItemQuantity(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.name}_{self.quantity}"
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        self.price=self.item.price*self.quantity       
        super().save(*args, **kwargs)

    
