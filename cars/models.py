from django.db import models

class User(models.Model):
    email=models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    #to save the data
    def register(self):
        self.save()
    
    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email= email)
        except:
            return False

    def isExists(self):
        if User.objects.filter(email = self.email):
            return True

        return False
class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    services = models.ManyToManyField(Service)
    total_price = models.IntegerField(default=0)
    address = models.TextField(default='')
    service_names = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.service_names)
    
class Order(models.Model):
    services = models.ManyToManyField(Service)
    total_price = models.IntegerField(default=0)
    address = models.TextField(default='')
    service_names = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)


