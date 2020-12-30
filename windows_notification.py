

import time
from win10toast import ToastNotifier


def notifier(title, message, message_duration, delay):
    notificator = ToastNotifier()
    # set threaded=True if you want to execute other part of code to rune while this notification is active
    notificator.show_toast(title, message, duration=message_duration, threaded=False)
    time.sleep(delay)


if __name__ == "__main__":
    show_message_time = 4   # show message for this much seconds
    delay_until_next_popup = 6     # after message has been show, wait this much seconds and repeate
    while True:
        notifier("Notification title", "Your Message", show_message_time, delay_until_next_popup)
