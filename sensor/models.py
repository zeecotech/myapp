from django.db import models

# Create your models here.

from django.core.exceptions import ValidationError

class sensorinputModel(models.Model):
    stinput = models.CharField(max_length=100)

    def clean(self):
        ''' Checks if user input is valid or not. '''
        if self.stinput:
            try:
                new = int(self.stinput)
                if not (0 <= new <= 100):
                    raise ValidationError("Input value should be between 0 and 100")
            except ValueError:
                raise ValidationError("Invalid input. Input should be an integer.")
        else:
            raise ValidationError("No user input provided")

        # If everything is fine, return cleaned data
        return super().clean()
