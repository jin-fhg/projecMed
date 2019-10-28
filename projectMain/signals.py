from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Account, AccountType

@receiver(post_save, sender=User)
def create_profile(sender, instance, created ,**kwargs):
	if created:
		AccountType.objects.create(user=instance)
		instance.accounttype.access = 1
		Account.objects.create(userName=instance)
		
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.accounttype.save()
	instance.account.save()