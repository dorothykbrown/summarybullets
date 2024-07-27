from django.db import models

class Text(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField

    def __str__(self):
        return self.name + ' ' + self.__class__

class Summary(models.Model):
    name = models.CharField(max_length=50)
    original_text = models.ForeignKey("Text", on_delete=models.CASCADE)
    summary = models.TextField

    def __str__(self):
        return self.name + ' ' + self.__class__

class BulletPoint(models.Model):
    name = models.CharField(max_length=50)
    original_text = models.ForeignKey("Text", on_delete=models.CASCADE)
    bullet_points = models.JSONField

    def __str__(self):
        return self.name + ' ' + self.__class__