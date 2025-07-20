from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )


class MovementType(BaseModel):
    name = models.CharField()
    description = models.TextField()


class Movement(BaseModel):
    BALANCES = (("input", "Input"), ("expense", "Expense"))
    name = models.CharField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    movement_type = models.ForeignKey(to=MovementType, on_delete=models.CASCADE)
    balance = models.CharField(choices=BALANCES)
    date = models.DateTimeField(auto_now_add=True)
