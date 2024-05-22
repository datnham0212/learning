import os
import time

def receive_messages(shared_folder, last_check, username):
    messages = []
    for filename in os.listdir(shared_folder):
        if filename != f"{last_check}_{username}.txt":
            filepath = os.path.join(shared_folder, filename)
            if os.path.isfile(filepath):
                timestamp = int(filename.split('_')[0])
                sender = filename.split('_')[1].split('.')[0]
                if timestamp > last_check:
                    with open(filepath, 'r') as file:
                        message = file.read()
                        messages.append((timestamp, sender, message))
    return messages

def continuous_receive(username, shared_folder, interval=5):
    last_check = int(time.time()) - 60  # Check messages from the last 60 seconds
    while True:
        messages = receive_messages(shared_folder, last_check, username)
        for timestamp, sender, message in messages:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}] {sender}: {message}")
        last_check = int(time.time())
        time.sleep(interval)  # Check for new messages every 'interval' seconds

def main():
    username = input("Enter your username: ")
    shared_folder = "C:/Users/datnh/Desktop/FromLaptop2"

    continuous_receive(username, shared_folder, 5)

if __name__ == "__main__":
    main()
