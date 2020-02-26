from django.db import models


class Domain(models.Model):
    domain_name = models.CharField(max_length=253)
    title = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='domains', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
