import sys
from notebook import Notebook, Note

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit}

    def display_menu(self):
        print("""
Note Menu

1. Show All Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice".format(choice))

    def show_notes(self):
        self.notebook.show_notes()

    def search_notes(self):
        text = input("Search for: ")
        notes = self.notebook.search(text)

    def add_note(self):
        memo = input("Enter memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        note_id = int(input("Enter a note id: "))
        memo = input("Enter a memo:" )
        tags = input("Enter tags: ")

        if not self.notebook._find_note(note_id):
            print("ID is not valid.")
            return None
        if memo:
            self.notebook.modify_memo(note_id, memo)
        if tags:
            self.notebook.modify_tags(note_id,tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
