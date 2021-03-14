class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        confirm = {self.name}
        temp = self.next
        while temp:
            if temp.name in confirm:
                return True
            confirm.add(temp.name)
            temp = temp.next
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist())