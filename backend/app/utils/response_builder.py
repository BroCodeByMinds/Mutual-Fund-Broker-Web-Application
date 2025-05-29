from app.utils.app_consts import HTTPStatusCodes
from app.utils.singleton import Singleton


class ResponseBuilder(metaclass=Singleton):

    
    def __init__(self) -> None:
        super().__init__()

    def build_success_response(self, data=None):
        return self.__build_response(HTTPStatusCodes.SUCCESS, data=data)
    

    def __build_response(self, status_code, message=None, data=None):
        return {
                "status_code": status_code,
                "message": message,
                "data": data
            }

    def build_warn_response(self, msg=None, data=None):
        return self.__build_response(HTTPStatusCodes.WARNING, message=msg, data=data)
    

    def build_error_response(self, msg=None, data=None):
        return self.__build_response(HTTPStatusCodes.ERROR, message=msg, data=data)