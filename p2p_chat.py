import os
import time
import threading

def send_message(username, message, shared_folder1):
    timestamp = int(time.time())
    filename = f"{timestamp}_{username}.txt"
    filepath = os.path.join(shared_folder1, filename)
    
    with open(filepath, 'w') as file:
        file.write(message)
    
    print(f"Message sent: {message}")

def receive_messages(shared_folder2, last_check, username):
    messages = []
    for filename in os.listdir(shared_folder2):
        if filename != f"{last_check}_{username}.txt":
            filepath = os.path.join(shared_folder2, filename)
            if os.path.isfile(filepath):
                timestamp = int(filename.split('_')[0])
                sender = filename.split('_')[1].split('.')[0]
                if timestamp > last_check:
                    with open(filepath, 'r') as file:
                        message = file.read()
                        messages.append((timestamp, sender, message))
    return messages

def continuous_receive(username, shared_folder2, interval=5):
    last_check = int(time.time()) - 60  # Check messages from the last 60 seconds
    while True:
        messages = receive_messages(shared_folder2, last_check, username)
        for timestamp, sender, message in messages:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}] {sender}: {message}")
        last_check = int(time.time())
        time.sleep(interval)  # Check for new messages every 'interval' seconds

def main():
    username = input("Enter your username: ")
    shared_folder1 = "C:/Users/datnh/Desktop/ToLaptop2"
    shared_folder2 = "C:/Users/datnh/Desktop/FromLaptop2"

    # Start the message receiving thread
    receive_thread = threading.Thread(target=continuous_receive, args=(username, shared_folder2, 5))
    receive_thread.daemon = True
    receive_thread.start()

    # Main loop for sending messages
    while True:
        message = input("Enter your message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        send_message(username, message, shared_folder1)

if __name__ == "__main__":
    main()
