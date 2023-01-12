from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, F

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    email = models.EmailField()
    def __str__(self):
        return "%s"%(self.user)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('update_profile_signal: create a profile')

class Product(models.Model):
    UNIT_NAME_CHOICE = [ ("ลูก","ลูก"), ("กก.","กิโลกรัม"), ("ชิ้น","ชิ้น") ]
    title = models.CharField(max_length=100)
    unit = models.CharField(max_length=5, choices=UNIT_NAME_CHOICE, default="ชิ้น")
    unit_price = models.DecimalField(max_digits=5, decimal_places=2) #999.99
    #image = models.ImageField(upload_to='myimages') #from week05
    #description = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return "%s(%s/%s)"%(self.title, self.unit_price, self.unit)

class Order(models.Model):
    profile = models.ForeignKey( Profile, on_delete=models.CASCADE)
    created = models.DateTimeField()
    @property
    
    def total_price(self):
        return OrderItem.objects.filter(order=self).aggregate(total=Sum(F('quantity')*F('product__unit_price')))['total']

    def total_payment(self):
        return Payment.objects.filter(order=self).aggregate(total=Sum('amount'))['total']

    def __str__(self):
        return "order_id:%s profile:%s"%(self.id,self.profile)

class OrderItem(models.Model):
    order = models.ForeignKey( Order, on_delete=models.CASCADE)
    product = models.ForeignKey( Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    @property
    def subtotal(self):
        return self.quantity * self.product.unit_price

    def __str__(self):
        return "order_id:%s, user:%s, %s * %s"%(self.order.id, self.order.profile.user, self.quantity, self.product)

class Payment(models.Model):
    order = models.ForeignKey( 'Order', on_delete=models.CASCADE)
    created = models.DateTimeField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "id:%s, user:%s, amount:%s"%(self.id, self.order.profile.user, self.amount)