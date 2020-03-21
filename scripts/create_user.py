from cms.models import User, AppUser, Site
from django.db import transaction

def run():
    with transaction.atomic():
        user,created = User.objects.get_or_create(
            username='admin',
            email='admin@sample.com',
        )
        user.set_password('admin')
        user.save()
        AppUser.objects.update_or_create(user=user, permission_level='ADMIN')

        user,created = User.objects.get_or_create(
            username='siteadmin',
            email='siteadmin@sample.com',
        )
        user.set_password('admin')
        user.save()
        site = Site(id=1)
        AppUser.objects.update_or_create(user=user, permission_level='SITEADMIN', site=site)
