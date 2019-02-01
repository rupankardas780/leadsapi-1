from enumchoicefield import ChoiceEnum


class LocationType(ChoiceEnum):
    Country = "Country"
    City = "City"
    Zip = "Zip"


class LeadStatus(ChoiceEnum):
    Created = "Created"
    Contacted = "Contacted"
    Converted = "Converted"

