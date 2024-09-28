# Danny Regan
# CSC6003

# These methods alter information specific to the selected user and are called by the Program class.
class User:
    def __init__(self, username):
        self.username = username
        self.music_collection = {}

    def add_song(self, title, artist):
        self.music_collection[title] = artist
        print(f"Song '{title}' by {artist} added to {self.username}'s collection.")

    def retrieve_song(self, title):
        if title in self.music_collection:
            print(f"The song '{title}' is by {self.music_collection[title]}.")
        else:
            print(f"Song '{title}' not found in {self.username}'s collection.")

    def update_song(self, title, new_artist):
        if title in self.music_collection:
            self.music_collection[title] = new_artist
            print(f"Song '{title}' updated with new artist: {new_artist}.")
        else:
            print(f"Song '{title}' not found in {self.username}'s collection.")

    def delete_song(self, title):
        if title in self.music_collection:
            del self.music_collection[title]
            print(f"Song '{title}' removed from {self.username}'s collection.")
        else:
            print(f"Song '{title}' not found in {self.username}'s collection.")

    def display_all_songs(self):
        if self.music_collection:
            print(f"{self.username}'s music collection:")
            for title, artist in self.music_collection.items():
                print(f"- {title} by {artist}")
        else:
            print(f"{self.username} has no songs in their collection.")

# These methods control the flow of the program and call methods of the User class to edit information for each user.
class Program:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self):
        username = input("Enter new username: ")
        if username in self.users:
            print(f"User '{username}' already exists.")
        else:
            # We create a new instance of the User class. Now, we can refer to that instance as self.current_user and call methods for that specific instance.
            self.users[username] = User(username)
            self.current_user = self.users[username]
            print(f"User '{username}' added and selected.")

    def change_user(self):
        if not self.users:
            print("No users available. Please add a user first.")
            return
        print("Select a user: ")
        # List the users that have been stored in the users dictionary.
        for i, username in enumerate(self.users.keys(), 1):
            print(f"{i}) {username}")
        choice = int(input("Selection: ")) - 1
        if 0 <= choice < len(self.users):
            # Looks through values of the user dictionary and switches to the selected user.
            self.current_user = list(self.users.values())[choice]
            print(f"Switched to user '{self.current_user.username}'.")
        else:
            print("Invalid choice.")

    def add_song(self):
        if self.current_user:
            title = input("Enter song title: ")
            artist = input("Enter song artist: ")
            self.current_user.add_song(title, artist)
        else:
            print("No user selected. Please add or change user.")

    def retrieve_song(self):
        if self.current_user:
            title = input("Enter song title: ")
            self.current_user.retrieve_song(title)
        else:
            print("No user selected. Please add or change user.")

    def update_song(self):
        if self.current_user:
            title = input("Enter song title to update: ")
            new_artist = input("Enter new artist: ")
            self.current_user.update_song(title, new_artist)
        else:
            print("No user selected. Please add or change user.")

    def delete_song(self):
        if self.current_user:
            title = input("Enter song title to delete: ")
            self.current_user.delete_song(title)
        else:
            print("No user selected. Please add or change user.")

    def display_all_songs(self):
        if self.current_user:
            self.current_user.display_all_songs()
        else:
            print("No user selected. Please add or change user.")

# The menu that loops repeatedly during the program.
    def menu(self):
        while True:
            print("===Menu===")
            if self.current_user:
                print(f"==User {self.current_user.username}==")
            print("1) Add user")
            if self.current_user:
                print("2) Change User")
                print("3) Add a song")
                print("4) Retrieve song details")
                print("5) Update song details")
                print("6) Delete a song")
                print("7) Display all songs")
            print("0) Exit")
            choice = input("Select an option: ")
            
            # These choices call methods in the Program class. Then, those methods call methods in the User class.
            if choice == '1':
                self.add_user()
            elif choice == '2' and self.current_user:
                self.change_user()
            elif choice == '3' and self.current_user:
                self.add_song()
            elif choice == '4' and self.current_user:
                self.retrieve_song()
            elif choice == '5' and self.current_user:
                self.update_song()
            elif choice == '6' and self.current_user:
                self.delete_song()
            elif choice == '7' and self.current_user:
                self.display_all_songs()
            elif choice == '0':
                break
            else:
                print("Invalid option or no user selected.")

def main():
    app = Program()
    app.menu()

# ==========================================================================================

main()