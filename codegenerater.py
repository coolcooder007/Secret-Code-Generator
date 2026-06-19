def encode(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


print("🕵️ Secret Code Generator")

while True:
    choice = input("\n1. Encode\n2. Decode\n3. Exit\nChoose: ")

    if choice == "3":
        print("Goodbye!")
        break

    message = input("Enter your message: ")

    try:
        shift = int(input("Enter secret key (number): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == "1":
        print("Encoded Message:", encode(message, shift))

    elif choice == "2":
        print("Decoded Message:", encode(message, -shift))

    else:
        print("Invalid choice!")
