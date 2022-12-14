from song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in [song.name for song in self.songs]:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."

        song_to_remove = next(filter(lambda s: song_name == s.name, self.songs))
        self.songs.remove(song_to_remove)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        [result.append(f"== {s.get_info()}") for s in self.songs]
        return '\n'.join(result)

