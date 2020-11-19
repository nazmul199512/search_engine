from django.db import models
from django.contrib.auth.models import User


class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=10)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} -> {}'.format(self.user.username, self.keyword[:30])

    class Meta:
        verbose_name_plural = 'search histories'
