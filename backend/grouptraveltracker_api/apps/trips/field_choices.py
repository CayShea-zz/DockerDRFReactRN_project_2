from ..extensions.choices import ChoicesMeta

class TripClassification(metaclass=ChoicesMeta):
    WORK = "work"
    PLEASURE = "pleasure"
    BOTH = "both"