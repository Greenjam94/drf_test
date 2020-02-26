from django.db import models


class Server(models.Model):
    hostname = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='servers', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
