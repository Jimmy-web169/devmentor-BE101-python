from abc import ABC, abstractmethod
from user import User
# Notification Interface
class Notification(ABC):

    @abstractmethod
    def send_message(self, message: str, user: User):
        """
        Every notification should have a send_message method
        """
        pass
# Email Notification
class Email(Notification):
    def send_message(self, message: str, user: User):
        print(f"Sending Email to {user.email}: {message}")

# SMS Notification
class SMS(Notification):
    def send_message(self, message: str, user: User):
        print(f"Sending SMS to {user.phone}: {message}")
        
class Telegram(Notification):
    def send_message(self, message: str, user: User):
        print(f"Sending Telegram message to {user.id}: {message}")
      
class Line(Notification):
    def send_message(self, message: str, user: User):
        print(f"Sending Line message to {user.id}: {message}")
   