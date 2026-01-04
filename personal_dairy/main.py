from user import User
from diary import DiaryEntry
import session_store
from decorators import login_required
from file_manager import *
from utils import *

ensure_data_dir()

# Load users
users_data = load_json(USERS_FILE)
users = {}
for u in users_data:
    users[u["username"]] = User(u["username"], u["email"], u["password"])

# Load diary entries
entries = load_json(DIARY_FILE)


def login():
    username = input("Username: ")
    password = input("Password: ")

    user = users.get(username)
    if user and user.authenticate(password):
        session_store.current_user = user  # MUST update session_store
        print(" Logged in as", username)
    else:
        print(" Invalid credentials")


@login_required
def add_entry():
    title = input("Title: ")
    content = input("Content: ")
    y = int(input("Year: "))
    m = int(input("Month: "))
    d = int(input("Day: "))
    tags = input("Tags (comma separated): ").split(",")

    entry = DiaryEntry(title, content, (y, m, d), tags)
    entries.append(entry.to_dict())
    print("Entry added")


@login_required
def view_entries():
    if not entries:
        print("No diary entries yet.")
        return
    for e in entries:
        print(f"Title: {e['title']}, Date: {e['date']}, Tags: {e['tags']}")
        print(f"Content: {e['content']}\n")


def logout():
    session_store.current_user = None
    print(" Logged out")


def menu():
    global entries

    while True:
        print("""
1. Login
2. Add Diary Entry
3. View All Entries
4. Filter Entries
5. Search Entries
6. Sort Entries
7. Save Diary
8. Logout
9. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            login()

        elif choice == "2":
            add_entry()

        elif choice == "3":
            view_entries()

        elif choice == "4":
            tag = input("Enter tag: ")
            results = filter_by_tag(entries, tag)

            if not results:
                print("No entries found.")
            else:
                for e in results:
                    print(f"{e['title']} | {e['date']} | {e['tags']}")
                    print(e["content"], "\n")

        elif choice == "5":
            keyword = input("Enter keyword: ")
            results = search_by_keyword(entries, keyword)

            if not results:
                print("No matching entries found.")
            else:
                for e in results:
                    print(f"{e['title']} | {e['date']}")
                    print(e["content"], "\n")

        elif choice == "6":
            entries = sort_by_date(entries)
            print("Entries sorted by date.")

        elif choice == "7":
            save_json(DIARY_FILE, entries)
            print("Diary saved.")

        elif choice == "8":
            logout()

        elif choice == "9":
            break

        else:
            print("Invalid choice")


menu()
