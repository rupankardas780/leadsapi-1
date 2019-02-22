from django.db import models
from restapi.enums import LocationType, LeadStatus
from enumchoicefield import EnumChoiceField


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        abstract = True


class Lead(BaseModel):
    first_name = models.CharField(max_length=64, blank=False, null=False, )
    last_name = models.CharField(max_length=64, blank=False, null=False, )
    mobile = models.CharField(max_length=13, blank=False, null=False, )
    email = models.CharField(max_length=128, blank=False, null=False,unique=True)
    location_type = EnumChoiceField(LocationType, default=LocationType.Country)
    location_string = models.CharField(max_length=64)
    status = EnumChoiceField(LeadStatus, default=LeadStatus.Created)
    communication = models.CharField(max_length=512,null=True)
    tags = models.CharField(max_length=512, null=True) # Comma List
