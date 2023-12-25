import pyperclip

def copy_message(message):
    pyperclip.copy(message)
    print(f'Message copied: {message}')

def paste_message():
    message = pyperclip.paste()
    print(f'Pasted message: {message}')
    return message

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Copy message")
        print("2. Paste message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message_to_copy = input("Enter the message to copy: ")
            copy_message(message_to_copy)
        elif choice == '2':
            pasted_message = paste_message()
        elif choice == '3':
            print("Exiting the script.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
