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

def get_friends_watched_movies(user_data): 
    """helper function. Find the movies that friends have watched
    Returns: 
        lists of movie dictionaries [{},{}]
    """
    friends_watched = []
    for friend in user_data["friends"]: 
        for movie in friend["watched"]: 
            friends_watched.append(movie)

    return friends_watched
    
def get_unique_watched(user_data):
    """Find the movies that the user has watched, but none of the friends have watched. 
    Returns:
        lists of movie dictionaries [{},{}]
    """
    user_watched = user_data["watched"]                     # all the movies the user watched
    friends_watched = get_friends_watched_movies(user_data) # all the movies that friends watched

    unique = []                        
    # filter out the movies that the friends watched
    for movie in user_watched: 
        if movie not in friends_watched:
            unique.append(movie)

    return unique

def get_friends_unique_watched(user_data):
    """Find the movies that at least one friend has watched, but the user has not watched. 
    Returns:
        lists of movie dictionaries [{},{}]
    """
    user_watched = user_data["watched"]                     # all the movies the user watched
    friends_watched = get_friends_watched_movies(user_data) # all movies that friends watched

    unwatched = []
    # filter out the movies the user has watched and duplicates
    for movie in friends_watched: 
        if movie not in user_watched and movie not in unwatched: 
            unwatched.append(movie)

    return unwatched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data): 
    """Find recommended movies that the user has not watched but at least one 
    of the friends has watched. Only keep movies hosted on subscribed services

    Returns:
        lists of movie dictionaries [{},{}]
    """
    unwatched = get_friends_unique_watched(user_data)  #unwatched movies that at least one of the friends watched

    recommended = []
    # filter out movies on the platforms the user is not subscribed to
    for movie in unwatched: 
        if movie["host"] in user_data["subscriptions"]: 
            recommended.append(movie)

    return recommended

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data): 
    """Find the movies that the user has not watched but at least one of the friends watched
    Only keep movies of the user's most watched genre

    Returns:
        lists of movie dictionaries [{},{}]
    """
    unwatched = get_friends_unique_watched(user_data)  #unwatched movies that at least one of the friends watched
    genre = get_most_watched_genre(user_data)

    recommended = []
    # filter out movies of all genres except the favorite genre
    for movie in unwatched: 
        if movie["genre"] == genre: 
            recommended.append(movie)

    return recommended


def get_rec_from_favorites(user_data): 
    """Find the movies from user's favorites that none of the friends watched
    Returns:
        lists of movie dictionaries [{},{}]
    """
    favorites = user_data["favorites"]
    unique_watched = get_unique_watched(user_data)

    recommended = []
    # filter out movies that friends watched and duplicates
    for movie in favorites: 
        if movie in unique_watched and movie not in recommended: 
            recommended.append(movie)

    return recommended



