# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if not all([title, genre,rating]):
        return None

    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie


def add_to_watched(user_data, movie):
    user_data.setdefault("watched", []).append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data.setdefault("watchlist", []).append(movie)
    return user_data

def watch_movie(user_data, title):
    movie = next((movie for movie in user_data.setdefault("watchlist", []) if movie["title"] == title), None)
    if movie is not None:
        user_data.setdefault("watched",[]).append(movie)
        user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
