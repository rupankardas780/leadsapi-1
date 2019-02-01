from enumchoicefield.admin import EnumListFilter
from rest_framework import serializers
from restapi.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        list_filter = [
            ('location_type', EnumListFilter),('status', EnumListFilter)
        ]