from django.contrib import admin

# Register your models here.
from myapp.models import Profile, Item, Order, OrderItem, Payment

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)

class OrderItemTableAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0

class PaymentTableAdmin(admin.TabularInline):
    model = Payment
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','profile','created','total_price','total_payment')
    inlines = [OrderItemTableAdmin, PaymentTableAdmin]
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ('id','order', 'quantity','item','subtotal')
    list_editable = ('item','quantity')
    list_filter = ('order',)
admin.site.register(OrderItem, OrderItemAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ('id','order', 'created','amount')
admin.site.register(Payment, PaymentAdmin)
