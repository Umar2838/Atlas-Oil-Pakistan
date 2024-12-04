from django.db import models

class SubmittedCode(models.Model):
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.code
