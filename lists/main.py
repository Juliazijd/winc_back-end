# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
list_of_films = [
        'Pulp Fiction', 'James Bond', 'Notebook', 'The Mist'
    ]
def alphabetical_order(list):
    return sorted(list)
alphabetical_order(list_of_films)

winners = [
        "jaws",
        "star wars: episode iv - a new hope",
        "e.t. the extra-terrestrial",
        "memoirs of a geisha",
    ]
def won_golden_globe(movie):
    if movie.lower() in winners:
        return True 
    return False
print(won_golden_globe('Jaws'))

compositions_list = [
        'Home Alone', 'Penelope', 'Fahrenheit',\
        'Old Is New', 'Heidi', 'Images', 'The Cowboys', 'Conrack', 'Falling In Between'
    ]
toto_albums = [
        'Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling In between',\
        '35th Anniversary', 'Toto XIV', 'Old Is New', '40 Tours Around The Sun',\
        'With A Little Help From My Friends'
    ]
def remove_toto_albums(compositions):
    matches = list(set(compositions) & set(toto_albums))
    updated_compositions_list = list(set(compositions) - set(matches))
    return updated_compositions_list
remove_toto_albums(compositions_list)
