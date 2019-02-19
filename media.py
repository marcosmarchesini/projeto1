# Importacao do modulo webbbrowser
import webbrowser


# Criacao de classe generica Video
class Video():
    def __init__(self, title, duration, poster_image, trailer_youtube, status):
        self.title = title
        self.duration = duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.status = status

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# Criacao de classe especivica Movie
class Movie(Video):
    def __init__(self, title, duration, movie_storyline, poster_image,
                 trailer_youtube, status):
        Video.__init__(self, title, duration, poster_image,
                       trailer_youtube, status)
        self.storyline = movie_storyline


# Criacao de classe especivica TV Show
class TVShow(Video):
    def __init__(self, title, duration, season, episode, tv_station,
                 poster_image, trailer_youtube, status):
        Video.__init__(self, title, duration, poster_image,
                       trailer_youtube, status)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
