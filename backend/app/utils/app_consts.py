class DataBaseSchemas:
    MASTER = 'master'
    


class AppFields:
    SCHEMA = 'schema'
    ACCESS_TOKEN = 'access_token'
    EMAIL = 'email'



class DataBaseTables:
    USERS = 'users'
    FAMILY_FUND_ORM = 'family_fund'
    NavCacheORM = 'nav_cache'

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
    INVALID_TOKEN = 'Invalid or expired token'
    NAV_SCHEDULER_STARTED = "NAV scheduler started."
    NAV_SCHEDULER_CANCELLED = "NAV scheduler cancelled gracefully."
    # User Messages
    EMAIL_ALREADY_REGISTERED = 'email already registerd : '


class QueryParams:
    # API Query Params
    RTA_AGENT_CODE_KEY = "RTA_Agent_Code"
    RTA_AGENT_CODE_VALUE = "CAMS"
    MUTUAL_FUND_FAMILY_KEY = "Mutual_Fund_Family"


class Schedulers:
    MUTUAL_FUND_FAMILIES = ['HDFC Mutual Fund', 'SBI Mutual Fund']