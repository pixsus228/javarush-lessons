print("Завантажено __init__")

from .email import send_email
from .sms import send_sms

PHONE_NUMBER = "0681234432"

__all__ = ["send_email", "send_sms", "PHONE_NUMBER"]

# __version__ = "1.0.0"