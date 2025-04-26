from django.db import models

class Input(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)
    field3 = models.CharField(max_length=255)
    field4 = models.CharField(max_length=255)
    field5 = models.DecimalField(max_digits=20, decimal_places=2)
    refkey1 = models.CharField(max_length=255)
    refkey2 = models.CharField(max_length=255)

class Reference(models.Model):
    refkey1 = models.CharField(max_length=255)
    refdata1 = models.CharField(max_length=255)
    refkey2 = models.CharField(max_length=255)
    refdata2 = models.CharField(max_length=255)
    refdata3 = models.CharField(max_length=255)
    refdata4 = models.DecimalField(max_digits=20, decimal_places=2)

class Output(models.Model):
    outfield1 = models.CharField(max_length=255)
    outfield2 = models.CharField(max_length=255)
    outfield3 = models.CharField(max_length=255)
    outfield4 = models.CharField(max_length=255)
    outfield5 = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.outfield1


