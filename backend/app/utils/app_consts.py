class DataBaseSchemas:
    MASTER = 'master'
    PORTFOLIO = 'portfolio'
    


class AppFields:
    SCHEMA = 'schema'
    ACCESS_TOKEN = 'access_token'
    EMAIL = 'email'
    DATE_FORMAT = "%Y-%m-%d"


class DataBaseTables:
    USERS = 'users'
    FAMILY_FUND_ORM = 'family_fund'
    NAV_CACHE_ORM = 'nav_cache'
    PORTFOLIO_ITEMS = 'fortfolio_items'
    TRANSACTIONS = 'transactions'


class ForeignKeys:
    SCHEMA_CODE = 'scheme_code'
    PORTFOLIO_ITEM_ID = 'portfolio_item_id'


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
    SCHEME_NOT_FOUND = 'Scheme not found'
    PURCHASE_TRANSACTION_FAILED = "Purchase transaction unsuccessful"
    

class QueryParams:
    # API Query Params
    RTA_AGENT_CODE_KEY = "RTA_Agent_Code"
    RTA_AGENT_CODE_VALUE = "CAMS"
    MUTUAL_FUND_FAMILY_KEY = "Mutual_Fund_Family"


class Schedulers:
    MUTUAL_FUND_FAMILIES = ['HDFC Mutual Fund', 'SBI Mutual Fund']