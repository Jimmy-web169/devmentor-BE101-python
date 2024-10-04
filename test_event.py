import unittest
from unittest.mock import Mock
from notification import Notification, Email, SMS, Telegram
from user import User
from event import RegisterEvent, CourseBookingEvent, CourseCancelEvent, HappyNewYearEvent

class TestEvent(unittest.TestCase):

    def setUp(self):
        # Set up a mock user with a preferred language and phone number
        self.user = Mock(spec=User)
        self.user.prefers_language = 'en_us'
        self.user.email = 'test@example.com'
        self.user.phone = '1234567890'  # Add a mock phone number

    def test_register_event(self):
        # Initialize the RegisterEvent
        event = RegisterEvent(self.user)

        # Verify initial channels
        self.assertIsInstance(event.channels[0], Email)
        self.assertIsInstance(event.channels[1], SMS)

        # Mock the send_message method of each channel
        for channel in event.channels:
            channel.send_message = Mock()

        # Call notify and verify each channel's send_message is called with the correct message
        event.notify()
        for channel in event.channels:
            channel.send_message.assert_called_once_with("Registration Successful", self.user)

    def test_course_booking_event(self):
        # Initialize the CourseBookingEvent
        event = CourseBookingEvent(self.user)

        # Verify initial channels
        self.assertIsInstance(event.channels[0], Email)
        self.assertIsInstance(event.channels[1], Telegram)

        # Mock the send_message method of each channel
        for channel in event.channels:
            channel.send_message = Mock()

        # Call notify and verify each channel's send_message is called with the correct message
        event.notify()
        for channel in event.channels:
            channel.send_message.assert_called_once_with("Course Booking Successful", self.user)

    def test_course_cancel_event(self):
        # Initialize the CourseCancelEvent
        event = CourseCancelEvent(self.user)

        # Verify initial channels
        self.assertIsInstance(event.channels[0], Email)
        self.assertIsInstance(event.channels[1], Telegram)

        # Mock the send_message method of each channel
        for channel in event.channels:
            channel.send_message = Mock()

        # Call notify and verify each channel's send_message is called with the correct message
        event.notify()
        for channel in event.channels:
            channel.send_message.assert_called_once_with("Course Cancellation", self.user)

    def test_happy_new_year_event(self):
        # Initialize the HappyNewYearEvent
        event = HappyNewYearEvent(self.user)

        # Verify initial channels
        self.assertIsInstance(event.channels[0], Email)
        self.assertIsInstance(event.channels[1], Telegram)
        self.assertIsInstance(event.channels[2], SMS)

        # Mock the send_message method of each channel
        for channel in event.channels:
            channel.send_message = Mock()

        # Call notify and verify each channel's send_message is called with the correct message
        event.notify()
        for channel in event.channels:
            channel.send_message.assert_called_once_with("Happy New Year", self.user)
    def test_preferred_language_not_in_event_map(self):
        self.user.prefers_language = 'fr_fr' 
        
        event = RegisterEvent(self.user)
        
        for channel in event.channels:
            channel.send_message = Mock()

        event.notify()

        for channel in event.channels:
            channel.send_message.assert_called_once_with("Notification", self.user)



    def test_add_channel(self):
        # Initialize a RegisterEvent
        event = RegisterEvent(self.user)
        
        # Add a new notification channel (mocked)
        new_channel = Mock(spec=Notification)
        event.add_channel(new_channel)

        # Check if the new channel was added
        self.assertIn(new_channel, event.channels)

        # Mock the send_message method of the new channel
        new_channel.send_message = Mock()

        # Call notify and verify the new channel's send_message is called
        event.notify()
        new_channel.send_message.assert_called_once_with("Registration Successful", self.user)


if __name__ == '__main__':
    unittest.main()
