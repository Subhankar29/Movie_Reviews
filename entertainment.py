import media
import fresh_tomatoes
Batman1 = media.Movie("Batman Begins",
                        "After witnessing his parents' death, Bruce learns the art of fighting to confront injustice. When he returns to Gotham as Batman, he must stop a secret society that intends to destroy the city.",
                        "http://www.gstatic.com/tv/thumb/movieposters/35903/p35903_p_v8_ae.jpg",
                        "https://youtu.be/neY2xVmOfUM")
Batman2 = media.Movie("The Dark Knight",
                     "Batman has a new foe, the Joker, who is an accomplished criminal hell-bent on decimating Gotham City. Together with Gordon and Harvey Dent, Batman struggles to thwart the Joker before it is too late.",
                     "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_at.jpg",
                     "https://youtu.be/EXeTwQWrcwY")
Batman3 = media.Movie("The Dark Knight Rises",
                       "Bane, an imposing terrorist, attacks Gotham City and disrupts its eight-year-long period of peace. This forces Bruce Wayne to come out of hiding and don the cape and cowl of Batman again.",
                       "http://images.sequart.org/images/The-Dark-Knight-Rises-teaser-image.jpg",
                       "https://youtu.be/GokKUqLcvD8")
Interstellar = media.Movie("Interstellar",
                           "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",
                           "https://youtu.be/0vxOhd4qlnA")
ThePrestige = media.Movie("The Prestige",
                          "Two friends and fellow magicians become bitter enemies after a sudden tragedy. As they devote themselves to this rivalry, they make sacrifices that bring them fame but with terrible consequences.",
                          "http://www.gstatic.com/tv/thumb/movieposters/161581/p161581_p_v8_aa.jpg",
                          "https://youtu.be/o4gHCmTQDVI")
Insomnia = media.Movie("insomnia",
                       "A police detective goes to an Alaskan town to investigate the killing of a teenaged girl. The main suspect plays a psychological game of cat and mouse with him, jeopardising his own mental stability.",
                       "http://www.gstatic.com/tv/thumb/movieposters/30021/p30021_p_v8_aa.jpg",
                       "https://youtu.be/brHA3CF4_Mw")
Memento = media.Movie("Memento",
                      "A man, suffering from short-term memory loss, uses notes and tattoos to hunt for the man he thinks killed his wife. Stars: Guy Pearce",
                      "http://www.gstatic.com/tv/thumb/movieposters/28578/p28578_p_v8_af.jpg",
                      "https://youtu.be/0vS0E9bBSL0")

Following = media.Movie("Following",
                        "Lacking prospects, a writer (Jeremy Theobald) begins tailing strangers, until he encounters a voyeuristic thief (Alex Haw).",
                        "http://www.gstatic.com/tv/thumb/movieposters/66576/p66576_p_v8_aa.jpg",
                        "https://youtu.be/5q8bBAKNSA8")

Doodlebug = media.Movie("Doodlebug",
                        "Doodlebug is a 1997 short psychological thriller film by Christopher Nolan",
                        "http://www.parkingfilm.asia/wp-content/uploads/2014/05/Doodlebug-1997-TopSerial.jpg",
                        "https://youtu.be/-WhKt_CkXD0")

movies = [Batman1, Batman2, Batman3, Interstellar, ThePrestige, Insomnia, Memento, Following, Doodlebug]
fresh_tomatoes.open_movies_page(movies)
                     
