import os

FILENAME = "file.txt"

def create_file():
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()
        print("File created successfully.")
    else:
        print("File already exists.")

def write_file():
    with open(FILENAME, "w") as f:
        data = input("Enter data to write:\n")
        f.write(data)
    print("Data written successfully.")

def append_file():
    with open(FILENAME, "a") as f:
        data = input("Enter data to append:\n")
        f.write("\n" + data)
    print("Data appended successfully.")

def read_file():
    if not os.path.exists(FILENAME):
        print("File does not exist.")
        return
    with open(FILENAME, "r") as f:
        content = f.read()
        print("\nFile Content:\n")
        print(content)

def count_data():
    if not os.path.exists(FILENAME):
        print("File does not exist.")
        return

    with open(FILENAME, "r") as f:
        text = f.read()
        lines = text.split("\n")
        words = text.split()

        print("Lines:", len(lines))
        print("Words:", len(words))
        print("Characters:", len(text))

def search_word():
    if not os.path.exists(FILENAME):
        print("File does not exist.")
        return

    word = input("Enter word to search: ")
    with open(FILENAME, "r") as f:
        text = f.read()

        if word in text:
            print("Word found!")
        else:
            print("Word not found!")

def copy_file():
    if not os.path.exists(FILENAME):
        print("Source file does not exist.")
        return

    with open(FILENAME, "r") as f1:
        content = f1.read()

    with open("copy.txt", "w") as f2:
        f2.write(content)

    print("File copied successfully to copy.txt")

def menu():
    while True:
        print("\n--- FILE HANDLING MENU ---")
        print("1. Create File")
        print("2. Write to File")
        print("3. Append to File")
        print("4. Read File")
        print("5. Count Lines, Words, Characters")
        print("6. Search Word")
        print("7. Copy File")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            append_file()
        elif choice == "4":
            read_file()
        elif choice == "5":
            count_data()
        elif choice == "6":
            search_word()
        elif choice == "7":
            copy_file()
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

# Run program
menu()