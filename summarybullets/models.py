from django.db import models

class Summary(models.Model):
    name = models.CharField(max_length=50)
    original_text = models.TextField(null=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return self.name + ' ' +  type(self).__name__

class BulletPoint(models.Model):
    name = models.CharField(max_length=50)
    original_text = models.TextField(null=True)
    bullet_points = models.JSONField(null=True)

    def __str__(self):
        return self.name + ' ' +  type(self).__name__