import os
import time

def send_message(username, message, shared_folder):
    timestamp = int(time.time())
    filename = f"{timestamp}_{username}.txt"
    filepath = os.path.join(shared_folder, filename)
    
    with open(filepath, 'w') as file:
        file.write(message)
    
    print(f"Message sent: {message}")

def main():
    username = input("Enter your username: ")
    shared_folder = "C:/Users/datnh/Desktop/ToLaptop2"

    while True:
        message = input("Enter your message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        send_message(username, message, shared_folder)

if __name__ == "__main__":
    main()
