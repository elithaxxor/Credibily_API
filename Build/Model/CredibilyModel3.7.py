# 03/26/.2022
### DATAMODEL BUILD FOR PYTHON 3.7
# CURRENT BUILD IS CONFIGED TO 3.6
# @dataclass
# class ExistingFinancing:
#     name: str
#     balance: int
#     unknown: bool
#
#
# @dataclass
# class ApplicationInfo:
#     product_requested: str
#     amount_requested: int
#     use_of_proceeds: str
#     existing_financing: List[ExistingFinancing]
#
#
# @dataclass
# class BusinessContact:
#     phone: str
#     fax: str
#     email: str
#     website: str
#
#
# @dataclass
# class Address:
#     address: str
#     city: str
#     state: str
#     postal_code: int
#
#
# @dataclass
# class BusinessLocation:
#     address: List[Address]
#
#
# @dataclass
# class BusinessOverview:
#     dba: str
#     legal_name: str
#     state_of_incorporation: str
#     date_established: datetime
#     date_current_ownership: datetime
#     revenue: int
#     deposit_amt: int
#     naics: int
#     federal_id: int
#
#
# @dataclass
# class BusinessProfile:
#     ownership: str
#     business_type: str
#
#
# @dataclass
# class File:
#     name: str
#     url: str
#     type: str
#
#
# @dataclass
# class Principal:
#     name_last: str
#     name_first: str
#     name_middle: str
#     percent_ownership: int
#     ssn: int
#     address: Address
#     dob: datetime
#
#
# @dataclass
# class Welcome:
#     business_overview: BusinessOverview
#     business_location: BusinessLocation
#     business_contact: BusinessContact
#     business_profile: BusinessProfile
#     principals: List[Principal]
#     application_info: ApplicationInfo
#     files: List[File]
