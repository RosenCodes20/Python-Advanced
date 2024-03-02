def movie_organizer(*args):
    movie_dict = {}
    result = []
    for movie, genre in args:
        if genre not in movie_dict:
            movie_dict[genre] = [movie]

        elif genre in movie_dict:
            movie_dict[genre].append(movie)

    for genre, movie in sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{genre} - {len(movie)}")

        for movies in sorted(movie):
            result.append(f"* {movies}")

    return "\n".join(result)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

