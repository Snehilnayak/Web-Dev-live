from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Customer

# the customer_profile is a view so whenever when we type in 
def customer_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='customers')
		instance.groups.add(group)
        # here instance is user attribute of customer model. 
		Customer.objects.create(
			user=instance,
			name=instance.username,
			)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)