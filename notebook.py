import datetime

class Note:
    '''Represent a note in the notebook. Match against a string in
    searches and store tags for each note.'''

    last_id = 0

    def __init__(self, memo, tags=''):
        '''Initialise a note with memo and optional space-separated
        tags. Automatically set the note's creation date and unique
        id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today().strftime("%d %B %Y")
        Note.last_id += 1
        self.id = Note.last_id

    def __str__(self):
        rep = "Note ID: {}".format(self.id) + "\n" + "Memo: {}".format(self.memo) + "\n" + \
              "Tags: {}".format(self.tags)
        return rep

    def match(self, text):
        '''Determines if this note matches the text. Return True
        if it matches and False otherwise.

        Search is case sensitive and matches both memo and tags.'''

        return text in self.memo or text in self.tags

class Notebook:
    '''Represent a collection of notes that can be tagged, modified
    and searched.'''

    def __init__(self):
        '''Initialise a notebook with an empty list.'''
        self.notes = []

    def show_notes(self):
        for note in self.notes:
            print()
            print(str(note))

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Find note with given id.'''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Findnote with the given id and change its memo to the
        given value.'''
        try:
            self._find_note(note_id).memo = memo
        except AttributeError:
            print("No note found with given ID.")

    def modify_tags(self, note_id, tags):
        '''Find note with the given id and change its tags to the
        given value.'''
        try:
            self._find_note(note_id).tags = tags
        except AttributeError:
            print("No note found with given ID.")

    def search(self, text):
        '''Search all notes and match against given text.'''
        match = False
        print("Search results: ")
        print("-" * 14)
        for note in self.notes:
            if note.match(text):
                match = True
                print()
                print(note)
        if not match:
            print("No matches found.")
