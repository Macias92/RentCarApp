from RentCar import settings
from rentcar_app.models import Profile
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def add_to_default_group(sender=User, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        group = Group.objects.get(name='client')
        user.groups.add(group)


post_save.connect(add_to_default_group, sender=settings.AUTH_USER_MODEL)
