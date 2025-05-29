import enum
from app.helper.constants.mfb_constants import TransactionTypeConstants

class TransactionType(enum.Enum):
    BUY = TransactionTypeConstants.BUY
    SELL = TransactionTypeConstants.SELL