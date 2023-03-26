from typing import List
from datetime import datetime


class ExistingFinancing:
    name: str
    balance: int
    unknown: bool

    def __init__(self, name: str, balance: int, unknown: bool) -> None:
        self.name = name
        self.balance = balance
        self.unknown = unknown


class ApplicationInfo:
    product_requested: str
    amount_requested: int
    use_of_proceeds: str
    existing_financing: List[ExistingFinancing]

    def __init__(self, product_requested: str, amount_requested: int, use_of_proceeds: str, existing_financing: List[ExistingFinancing]) -> None:
        self.product_requested = product_requested
        self.amount_requested = amount_requested
        self.use_of_proceeds = use_of_proceeds
        self.existing_financing = existing_financing


class BusinessContact:
    phone: str
    fax: str
    email: str
    website: str

    def __init__(self, phone: str, fax: str, email: str, website: str) -> None:
        self.phone = phone
        self.fax = fax
        self.email = email
        self.website = website


class Address:
    address: str
    city: str
    state: str
    postal_code: int

    def __init__(self, address: str, city: str, state: str, postal_code: int) -> None:
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code


class BusinessLocation:
    address: List[Address]

    def __init__(self, address: List[Address]) -> None:
        self.address = address


class BusinessOverview:
    dba: str
    legal_name: str
    state_of_incorporation: str
    date_established: datetime
    date_current_ownership: datetime
    revenue: int
    deposit_amt: int
    naics: int
    federal_id: int

    def __init__(self, dba: str, legal_name: str, state_of_incorporation: str, date_established: datetime, date_current_ownership: datetime, revenue: int, deposit_amt: int, naics: int, federal_id: int) -> None:
        self.dba = dba
        self.legal_name = legal_name
        self.state_of_incorporation = state_of_incorporation
        self.date_established = date_established
        self.date_current_ownership = date_current_ownership
        self.revenue = revenue
        self.deposit_amt = deposit_amt
        self.naics = naics
        self.federal_id = federal_id


class BusinessProfile:
    ownership: str
    business_type: str

    def __init__(self, ownership: str, business_type: str) -> None:
        self.ownership = ownership
        self.business_type = business_type


class File:
    name: str
    url: str
    type: str

    def __init__(self, name: str, url: str, type: str) -> None:
        self.name = name
        self.url = url
        self.type = type


class Principal:
    name_last: str
    name_first: str
    name_middle: str
    percent_ownership: int
    ssn: int
    address: Address
    dob: datetime

    def __init__(self, name_last: str, name_first: str, name_middle: str, percent_ownership: int, ssn: int, address: Address, dob: datetime) -> None:
        self.name_last = name_last
        self.name_first = name_first
        self.name_middle = name_middle
        self.percent_ownership = percent_ownership
        self.ssn = ssn
        self.address = address
        self.dob = dob


class Welcome:
    business_overview: BusinessOverview
    business_location: BusinessLocation
    business_contact: BusinessContact
    business_profile: BusinessProfile
    principals: List[Principal]
    application_info: ApplicationInfo
    files: List[File]

    def __init__(self, business_overview: BusinessOverview, business_location: BusinessLocation, business_contact: BusinessContact, business_profile: BusinessProfile, principals: List[Principal], application_info: ApplicationInfo, files: List[File]) -> None:
        self.business_overview = business_overview
        self.business_location = business_location
        self.business_contact = business_contact
        self.business_profile = business_profile
        self.principals = principals
        self.application_info = application_info
        self.files = files
