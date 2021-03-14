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
        ls = set()
        cur = self
        while cur:
            if cur in ls:
                return True
            ls.add(cur)
            cur = cur.next
        return False
