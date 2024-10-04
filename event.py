from abc import ABC, abstractmethod
from notification import Notification, Email, SMS, Telegram
from user import User

EventMap = {"Register":{"zh-TW":"註冊成功","en_us":"Registration Successful"},
    "CourseBookingEvent":{"zh-TW":"學生預約課程成功","en_us":"Course Booking Successful"},
    "CourseCancelEvent":{"zh-TW":"學生取消課程","en_us":"Course Cancellation"},"HappyNewYearEvent":{"zh-TW":"新年快樂","en_us":"Happy New Year"}}




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
    user : User
    content: dict
    channels : list[Notification]
    def __init__(self, user: User, content: dict,channels: list[Notification]):
        self.user = user
        self.content =   content
        self.channels = channels

    def add_channel(self, notification: Notification):
        self.channels.append(notification)
        return self

    def notify(self):
        message = self.content.get(self.user.prefers_language, "Notification")
        for channel in self.channels:
            channel.send_message(message, self.user)

# RegisterEvent
class RegisterEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user, content=EventMap['Register'],channels = [Email(), SMS()])

# CourseBookingEvent
class CourseBookingEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user,content=EventMap['CourseBookingEvent'],channels = [Email(), Telegram()])

# CourseCancelEvent
class CourseCancelEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user,content=EventMap['CourseCancelEvent'], channels = [Email(), Telegram()])

# HappyNewYear
class HappyNewYearEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user,content=EventMap['HappyNewYearEvent'], channels = [Email(), Telegram(), SMS()])
