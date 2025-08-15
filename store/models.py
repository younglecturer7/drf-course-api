from django.db import models
from django.utils.translation import gettext_lazy as _


## create promotion model
class Promotion(models.Model):
    # Promotion model fields
    description = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # admin interface representation
    def __str__(self):
        return f"{self.description} - {self.discount}% off"
    

## Create product model
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)
    Collection = models.ForeignKey('Collection', on_delete=models.PROTECT, related_name='products')
    promotion = models.ManyToManyField(Promotion, blank=True, related_name='promotion_products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


## Create customer model
class Customer(models.Model):
    # Membership choices for customers
    class MembershipChoices(models.TextChoices):
        BRONZE = "BR", _("Bronze")
        SILVER = "SI", _("Silver")
        GOLD = "GO", _("Gold")

    # Customer model fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    MembershipChoices = models.CharField(
        max_length=2,
        choices=MembershipChoices.choices,
        default=MembershipChoices.BRONZE,
    )

    # admin interface representation
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


## Create order model
class Order(models.Model):
    # Order status choices
    class PaymentStatus(models.TextChoices):
        PENDING = "P", _("Pending")
        COMPLETED = "C", _("Completed")
        FAILED = "F", _("Failed")

    # Order model fields
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')

    # admin interface representation
    def __str__(self):
        return f"Order {self.id} - {self.get_payment_status_display()} at {self.placed_at}" 


## Create address model
class Address(models.Model):
    # Address model fields
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    #customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='address', primary_key=True) # one-to-one relationship with Customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses') # one-to-many relationship with Customer
 

    # admin interface representation
    def __str__(self):
        return f"{self.street}, {self.city} - {self.customer.first_name} {self.customer.last_name}"
    

## Create collection model
class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

## Create orderitem model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in Order {self.order.id}"
    

## Create cart model
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.customer.first_name} {self.customer.last_name} created at {self.created_at}"
    

## Create cartitem model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in Cart {self.cart.id}"
    


