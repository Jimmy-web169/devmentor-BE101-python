# UserEventManager manage user's event
from user import User,Student
from eventhandler import EventHandler


class UserEventManager:
    def __init__(self, user: User):
        self.user = user

    def handle_event(self, event_method):
        event = event_method()
        event_handler = EventHandler(event, self.user)
        handled_event = event_handler.handle_event()
        handled_event.notify()
    

    def user_register(self):
        self.handle_event(self.user.register)
        self.user = Student(self.user.id, self.user.email, self.user.phone, self.user.prefers_language)


    def book_course(self):
        self.handle_event(self.user.course_booking)

    def cancel_course(self):
        self.handle_event(self.user.course_cancel)