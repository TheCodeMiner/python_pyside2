

import time
from win10toast import ToastNotifier


def timer(message, message_duration, delay):
    notificator = ToastNotifier()
    notificator.show_toast(title="Achtung", msg=message, duration=message_duration)
    time.sleep(delay)


if __name__ == "__main__":
    message_to_show = "Leave your desk and do some body exercises"
    show_message_time = 3   # show message for this much seconds
    delay_until_next_popup = 5     # after message has been show, wait this much seconds and repeate
    while True:
        timer(message_to_show, show_message_time, delay_until_next_popup)
