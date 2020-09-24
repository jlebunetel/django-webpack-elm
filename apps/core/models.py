"""
Implementing a UUID Pseudo Primary Key:

Avoid using the pk reference for model lookups,
because this will point to pkid rather than id.

So instead of:
    page = Page.objects.get(pk=page_id)
You'll now need to do:
    page = Page.objects.get(id=page_id)

It's important to note that all ForeignKey functionality will remain unchanged.

ModelViewSet implementations require one simple tweak to tell them to reference
your new id Pseudo-PK field instead of the pkid Primary Key on lookups.

Here's your tweak, implemented in a new base ViewSet for you to extend:

class UUIDModelViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'

https://www.stevenmoseley.com/blog/tech/uuid-primary-keys-django-rest-framework-2-steps
"""

import uuid
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class UUIDModel(models.Model):
    # id = models.AutoField(primary_key=True) <- default Primary Key
    pkid = models.BigAutoField(_("primary key"), primary_key=True, editable=False)
    id = models.UUIDField(
        _("UUID pseudo primary key"), default=uuid.uuid4, editable=False, unique=True
    )

    class Meta:
        abstract = True
