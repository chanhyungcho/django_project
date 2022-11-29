from django.db import models

class SUser(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    point = models.IntegerField()

    class Meta:
        db_table = "s_users"

    def __str__(self):
        return f'{self.pk}{self.email}{self.nickname}{self.password}{self.point}'

class Delivery(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    username = models.TextField()
    address = models.TextField()
    detail_address = models.TextField()
    phone = models.IntegerField()

    class Meta:
        db_table = "Delivery"

    def __str__(self):
        return f'{self.pk}{self.username}{self.address}{self.detail_address}{self.phone}'

class Category(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    name = models.TextField()

    class Meta:
        db_table = "Category"

    def __str__(self):
        return f'{self.pk}{self.name}'

class Product(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    name = models.TextField()
    price = models.IntegerField()
    image_url = models.TextField()


    class Meta:
        db_table = "Product"

    def __str__(self):
        return f'{self.pk}{self.name}{self.price}{self.image_url}'

class Cart(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)


    class Meta:
        db_table = "Cart"

    def __str__(self):
        return f'{self.pk}'

class Order(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    created_at = models.TextField()


    class Meta:
        db_table = "Order"

    def __str__(self):
        return f'{self.pk}{self.created_at}'
