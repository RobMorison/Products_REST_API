from django.db import models

# Create your models here.

class Product(models.Model): #inherit from imported Model class
    # This creates the columns in our table, each line is a column in a table, every variable equals a seperate column
    title = models.CharField(max_length=255) # Have to define max length in CharField
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2) # Decimal field need length for both digits and decimal places
    inventory_quantity = models.IntegerField() #do not need to define places for integer HAVE TO HAVE PARENTHESIS

    # Have to create datbase in MySQL prior to makeing migrations
    # Run python manage.py makemigrations app name in this case it would be python manage.py makemigrations products
    # 'No installed app with label' error have to add new app in project settings under installed apps
    # Once added to setting run python manage.py migrate