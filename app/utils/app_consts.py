class DataBaseSchemas:
    MASTER = 'master'
    


class AppFields:
    SCHEMA = 'schema'



class DataBaseTables:
    USERS = 'users'



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


    # User Messages
    EMAIL_ALREADY_REGISTERED = 'email already registerd : '
