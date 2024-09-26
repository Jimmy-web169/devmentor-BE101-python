# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from notification import Telegram
from user import User, Student
from event import  RegisterEvent,CourseBookingEvent,CourseCancelEvent


def main():
    # create user
    user = User(id="A0001", email="jimmy@example.com", phone="0912345678", prefers_language="zh-TW")
    register_event = RegisterEvent(user)
    register_event.add_channel(Telegram()).notify()

    jonny = Student(id="A0001", email="jimmy@example.com", phone="0912345678", prefers_language="zh-TW")
    booking_event = CourseBookingEvent(jonny)
    booking_event.notify()

    cancel_event = CourseCancelEvent(jonny)
    cancel_event.notify()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
