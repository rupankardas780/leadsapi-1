from enum import Enum


class LocationType(Enum):
    Country = "Country"
    City = "City"
    Zip = "Zip"


class LeadStatus(Enum):
    Created = "Created"
    Contacted = "Contacted"
    Converted = "Converted"
