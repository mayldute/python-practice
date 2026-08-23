"""
Task:
Implement a simple music playlist using object-oriented programming.

Requirements:
- Create a `Song` class.
- Create a `Playlist` class.
- A `Song` has a title, artist, and duration.
- Duration must be greater than 0.
- Invalid duration must raise `ValueError`.
- `Playlist` stores multiple Song objects.
- `add_song()` adds a Song to the playlist.
- `remove_song()` removes the first song with the given title.
- If the title does not exist, do nothing.
- `total_duration()` returns the total duration of all songs.
- `longest_song()` returns the song with the greatest duration.
- If the playlist is empty, `longest_song()` returns `None`.
- If multiple songs have the same duration, return the first one.

Algorithm:
- For `total_duration()`, iterate through the songs and add their durations.
- For `longest_song()`, iterate through the songs and keep track of the longest song found so far.
"""


class Song:
    def __init__(self, title: str, artist: str, duration: int) -> None:
        self.title = title
        self.artist = artist

        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")
        
        self.duration = duration


class Playlist:
    def __init__(self) -> None:
        self.playlist: list[Song] = []

    def add_song(self, song: Song) -> None:
        self.playlist.append(song)

    def remove_song(self, title: str) -> None:
        for song in self.playlist:
            if song.title == title:
                self.playlist.remove(song)
                break

    def total_duration(self) -> int:
        if not self.playlist:
            return 0
        
        total = 0

        for song in self.playlist:
            total += song.duration

        return total

    def longest_song(self) -> Song | None:
        if not self.playlist:
            return None

        return max(self.playlist, key=lambda song: song.duration)