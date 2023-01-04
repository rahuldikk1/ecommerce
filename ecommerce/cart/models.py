from shop.models import  Product
from django.db import models

class Cart(models.Model):
    DoesNotExist=None
    cart_id=models.CharField(max_length=250,blank=True)
    date_add=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date_add']
    def __str__(self):
        return '{}'.format(self.cart_id)

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='CartItem'
    def sub_total(self):
        return '{}'.format(self.product.price*self.quantity)

    def __str__(self):
        return self.product



