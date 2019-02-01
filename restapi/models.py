from django.db import models
from restapi.enums import LocationType, LeadStatus


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    first_name = models.CharField(max_length=64, blank=False, null=False, )
    last_name = models.CharField(max_length=64, blank=False, null=False, )
    mobile = models.CharField(max_length=13, blank=False, null=False, )
    email = models.CharField(max_length=128, blank=False, null=False, )
    location_type = models.CharField(max_length=10,
                                     choices=[(tag, tag.value) for tag in LocationType])
    location_string = models.CharField(max_length=64)
    status = models.CharField(max_length=10,
                                     choices=[(tag, tag.value) for tag in LocationType], default=LeadStatus.Created)
    communication = models.CharField(max_length=512)
    tags = models.CharField(max_length=512) # Comma List
