# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_watched_movies(user_data): 
    friends_watched = []
    for friend in user_data["friends"]: 
        for movie in friend["watched"]: 
            friends_watched.append(movie)

    return friends_watched
    
def get_unique_watched(user_data):

    # user_watched and friends_watched are lists of movie dictionaries
    user_watched = user_data["watched"]     
    friends_watched = get_friends_watched_movies(user_data)

    unique_list = []                        
    for movie in user_watched: 
        if movie not in friends_watched:
            unique_list.append(movie)

    return unique_list

def get_friends_unique_watched(user_data):

    user_watched = user_data["watched"]                     # structure: list of movie dictionaries
    friends_watched = get_friends_watched_movies(user_data) # structure: list of movie dictionaries

    unwatched_list = []
    for movie in friends_watched: 
        if movie not in user_watched and movie not in unwatched_list: 
            unwatched_list.append(movie)

    return unwatched_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data): 

    # get a list of unwatched movies that at least one of the friends watched
    unwatched_list = get_friends_unique_watched(user_data)

    recommended_list = []
    # filter out movies on the platforms the user is not subscribed to
    for movie in unwatched_list: 
        if movie["host"] in user_data["subscriptions"]: 
            recommended_list.append(movie)

    return recommended_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

