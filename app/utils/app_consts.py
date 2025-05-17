class DataBaseSchemas:
    MASTER = 'master'
    


class AppFields:
    SCHEMA = 'schema'



class DataBaseTables:
    USERS = 'users'
    FAMILY_FUND_ORM = 'family_fund'


class HTTPStatusCodes:
    def __init__(self) -> None:
        """
        """
        pass

    SUCCESS = 200
    ERROR = 400
    INFO = 600
    WARNING = 500



class Messages:
    PAYLOAD_VALIDATION_ERROR = 'Payload has errors.'
    INVALID_CREDENTIALS = 'Invalid credentials'
    RATE_LIMIT_ERROR_MSG = "Rate limit exceeded. Please try again later."
    VALIDATION_ERROR_MSG = "Data validation error: "

    # User Messages
    EMAIL_ALREADY_REGISTERED = 'email already registerd : '


class QueryParams:
    # API Query Params
    RTA_AGENT_CODE_KEY = "RTA_Agent_Code"
    RTA_AGENT_CODE_VALUE = "CAMS"
    MUTUAL_FUND_FAMILY_KEY = "Mutual_Fund_Family"
