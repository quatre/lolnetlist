from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from email.utils import formataddr

# Create your models here.


class Confirmation(models.Model):
    from_address = models.EmailField()
    request_date = models.DateTimeField(auto_now_add=True)
    expected_secret = models.CharField(max_length=50)
    pending_message_id = models.CharField(max_length=200)
    list_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.from_address


class UserState(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    state_key = models.CharField(max_length=512)
    from_address = models.EmailField()
    state = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s:%s (%s)" % (self.state_key, self.from_address, self.state)


class Domain(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=512)
    owners = models.ManyToManyField(User)

    class Meta:
        permissions = (
            ("can_manage_subscriptions", "Can manage subscriptions"),
            ("can_manage_lists", "Can manage lists"),
            )

    def __unicode__(self):
        return self.name


class MailingList(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    archive_url = models.CharField(max_length=512)
    archive_queue = models.CharField(max_length=512)
    name = models.CharField(max_length=512)
    similarity_pri = models.CharField(max_length=50)
    similarity_sec = models.CharField(max_length=50, null=True)
    owners = models.ManyToManyField(User)
    domain = models.ForeignKey(Domain)

    class Meta:
        permissions = (
                ("can_manage_subscriptions", "Can manage subscriptions"),
                ("can_manage_lists", "Can manage lists"),
                )

    def __unicode__(self):
        return self.name


class Subscription(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    subscriber_address = models.EmailField()
    subscriber_name = models.CharField(max_length=200)
    mailing_list = models.ForeignKey(MailingList)
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return '"%s" <%s>' % (self.subscriber_name, self.subscriber_address)

    def subscriber_full_address(self):
        return formataddr((self.subscriber_name, self.subscriber_address))
