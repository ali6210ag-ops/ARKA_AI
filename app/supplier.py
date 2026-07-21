from dataclasses import dataclass


@dataclass
class Supplier:
    id: int
    company_name: str
    contact_person: str
    phone: str
    email: str
    city: str
    country: str
    website: str = ""