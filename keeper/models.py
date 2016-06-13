from django.db import models


class Keeper(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    content_type = models.CharField(
        max_length=255, null=True, blank=True, choices=(
            ('application/json', 'application/json'),
            ('text/html', 'text/html'),
            ('text/plain', 'text/plain'),
            ('application/octet-stream', 'application/octet-stream'),
        )
    )

    data = models.TextField(max_length=1024 * 20, null=True, blank=True)
    read_token = models.CharField(max_length=16, null=True, blank=True)
    write_token = models.CharField(max_length=16, null=True, blank=True)
    charset = models.CharField(max_length=16, null=True, blank=True)
    reason = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
