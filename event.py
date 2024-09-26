from abc import ABC, abstractmethod
from notification import Notification, Email, SMS, Telegram
from user import User

EventMap = {"Register":{"zh-TW":"註冊成功","en_us":"Registration Successful"},
    "CourseBookingEvent":{"zh-TW":"學生預約課程成功","en_us":"Course Booking Successful"},
    "CourseCancelEvent":{"zh-TW":"學生取消課程","en_us":"Course Cancellation"}}




# Event Interface
class Event(ABC):
    @abstractmethod
    def add_channel(self, notification: Notification):
        """
        Every event should have an add_channel method
        """
        pass

    @abstractmethod
    def notify(self):
        """
        Every event should have a notify method
        """
        pass

class BaseEvent(Event):
    #Type hints
    user : str
    channels : list[Notification]
    def __init__(self, user: User, channels: list[Notification]):
        self.user = user
        self.channels = channels

    def add_channel(self, notification: Notification):
        self.channels.append(notification)

    def notify(self):
        message = self.content.get(self.user.prefers_language, "Notification")
        for channel in self.channels:
            channel.send_message(message, self.user)

# RegisterEvent
class RegisterEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user, channels = [Email(), SMS()])
        self.content = EventMap['Register']

# CourseBookingEvent
class CourseBookingEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user,channels = [Email(), Telegram()])
        self.content = EventMap['CourseBookingEvent']

# CourseCancelEvent
class CourseCancelEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user, channels = [Email(), Telegram()])
        self.content = EventMap['CourseCancelEvent']
