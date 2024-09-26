from abc import ABC, abstractmethod
from notification import Notification, Email, SMS, Telegram
from user import User

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
    def __init__(self, user: User, content: dict, default_channels: list):
        self.user = user
        self.content = content
        self.channels = default_channels

    def add_channel(self, notification: Notification):
        self.channels.append(notification)

    def notify(self):
        message = self.content.get(self.user.prefers_language, "Notification")
        for channel in self.channels:
            channel.send_message(message, self.user)

# RegisterEvent
class RegisterEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user, {"zh-TW": "註冊成功", "en-US": "Registration Successful"}, [Email(), SMS()])

# CourseBookingEvent
class CourseBookingEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user, {"zh-TW": "學生預約課程成功", "en-US": "Course Booking Successful"}, [Email(), Telegram()])

# CourseCancelEvent
class CourseCancelEvent(BaseEvent):
    def __init__(self, user: User):
        super().__init__(user, {"zh-TW": "學生取消課程", "en-US": "Course Cancellation"}, [Email(), Telegram()])
