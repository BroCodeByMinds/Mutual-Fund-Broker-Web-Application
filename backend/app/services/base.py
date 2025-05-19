from backend.app.utils.app_consts import Messages
from backend.app.utils.response_builder import ResponseBuilder


class Base:
    def __init__(self) -> None:
        """
        """
        self.resp_builder = ResponseBuilder()
        
    
    def validate_json_payload_schema(self, validator, data):
        try:
            res = validator(**data)
            return res, True
        except Exception as e:
            return self.resp_builder.build_warn_response(msg=Messages.PAYLOAD_VALIDATION_ERROR, data=str(e)), False
        