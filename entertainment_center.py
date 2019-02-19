# Importacao dos modulos media e fresh_tomatoes
import media
import fresh_tomatoes

# Instanciacao dos Objetos da classe Movie
toy_story = media.Movie("Toy Story",
                        "1h49",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/" +
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc",
                        "Movie")

avatar = media.Movie("Avatar",
                     "1h49",
                     "Marines in a alien planet",
                     "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/" +
                     "Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "Movie")

goodfellas = media.Movie("Goodfellas",
                         "1h49",
                         "Mobsters in tha house",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/" +
                         "Goodfellas.jpg",
                         "https://www.youtube.com/watch?v=h3QpxNI-PtE",
                         "Movie")


karate_kid = media.Movie("Karate Kid",
                         "1h49",
                         "Daniel Larusso kicking asses",
                         "https://upload.wikimedia.org/wikipedia/" +
                         "pt/thumb/9/92/Karate_kid_P%C3%B4ster.jpg/" +
                         "200px-Karate_kid_P%C3%B4ster.jpg",
                         "https://www.youtube.com/watch?v=yDi3an8WgN4",
                         "Movie")


cassino = media.Movie("Cassino",
                      "1h49",
                      "Mobster ruling Las Vegas",
                      "https://upload.wikimedia.org/wikipedia/pt/thumb/a/" +
                      "a0/Casino_1995.jpg/200px-Casino_1995.jpg",
                      "https://www.youtube.com/watch?v=EJXDMwGWhoA",
                      "Movie")


rambo = media.Movie("Rambo",
                    "1h49",
                    "Rambo shooting all bad guys",
                    "https://upload.wikimedia.org/wikipedia/pt/thumb/" +
                    "c/cf/Rambowallpaperkr8.jpg/200px-Rambowallpaperkr8.jpg",
                    "https://www.youtube.com/watch?v=2CRjdwRYQbU",
                    "Movie")

# Instanciacao dos Objetos da classe TV Show
sopranos = media.TVShow("The Sopranos",
                        "60 min",
                        "Season 1",
                        "Episode 1",
                        "HBO",
                        "https://upload.wikimedia.org/wikipedia/en/4/4a/" +
                        "The_Sopranos_S1_DVD.jpg",
                        "https://www.youtube.com/watch?v=wrN2k3qGbVA&t=11s",
                        "TV Show")

got = media.TVShow("Game Of Thrones",
                   "60 min",
                   "Season 1",
                   "Episode 1",
                   "HBO",
                   "https://upload.wikimedia.org/wikipedia/pt/a/a4/" +
                   "Game_of_Thrones_Temporada_1_Poster.jpg",
                   "https://www.youtube.com/watch?v=BpJYNVhGf1s",
                   "TV Show")

vikings = media.TVShow("Vikings",
                       "60 min",
                       "Season 1",
                       "Episode 4",
                       "History Channel",
                       "https://upload.wikimedia.org/wikipedia/pt/thumb/" +
                       "7/74/Vikings_Temporada_1_Poster.jpg" +
                       "/230px-Vikings_Temporada_1_Poster.jpg",
                       "https://www.youtube.com/watch?v=XELvE1WPGAY",
                       "TV Show")

# Criacao da lista contendo os objetos instanciados
movies = [toy_story, avatar, goodfellas, karate_kid, cassino, rambo,
          sopranos, got, vikings]
# Chamada do metodo open_movies page passando a lista como parametro
fresh_tomatoes.open_movies_page(movies)
