# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from notification import Telegram,Line
from user import User, Student
from event import  RegisterEvent,CourseBookingEvent,CourseCancelEvent,HappyNewYearEvent


def main():
    # create user
    # user = User(id="A0001", email="jimmy@example.com", phone="0912345678", prefers_language="zh-TW")
    # register_event = RegisterEvent(user)
    # register_event.add_channel(Telegram()).notify()

    jonny = Student(id="A0001", email="jimmy@example.com", phone="0912345678", prefers_language="zh-TW")
    happy_new_year_event = HappyNewYearEvent(jonny)
    happy_new_year_event.add_channel(Line()).notify()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
