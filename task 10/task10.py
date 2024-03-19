class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def audio_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def playlist_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0
class User:
    def __init__(self, name):
        self.name = name

    def rate_audio(self, audio, rating):
        audio.add_rating(rating)

    def rate_playlist(self, playlist, rating):
        playlist.add_rating(rating)

class MusicPlayer:
    def __init__(self):
        self.users = []
        self.playlists = []

    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist
    def search_audio_by_name(self, name):
        # Implement audio search logic by name
        pass
    def search_Playlist_by_name(self, name):
        # Implement audio search logic by name
        pass


# Example usage:
player = MusicPlayer()

