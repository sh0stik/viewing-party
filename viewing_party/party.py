# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if not all([title, genre, rating]):
        return None

    movie = {"title": title, "genre": genre, "rating": rating}
    return movie


def add_to_watched(user_data, movie):
    user_data.setdefault("watched", []).append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data.setdefault("watchlist", []).append(movie)
    return user_data


def watch_movie(user_data, title):
    # movie = next((movie for movie in user_data.setdefault("watchlist", []) if movie["title"] == title), None)
    watched_movie = None
    for movie in user_data.setdefault("watchlist", []):
        if movie["title"] == title:
            watched_movie = movie
            break
    if watched_movie is not None:
        user_data.setdefault("watched", []).append(watched_movie)
        user_data["watchlist"].remove(watched_movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    total = 0.0
    for movie in user_data["watched"]:
        total += movie["rating"]
    return total / len(user_data["watched"])


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    most_watched_genre = None
    genres_count = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        genres_count[genre] = genres_count.get(genre, 0) + 1

    highest_count = 0
    for genre, count in genres_count.items():
        if count > highest_count:
            highest_count = count
            most_watched_genre = genre
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
