import requests



def ship_detail(ship_name):
    url = 'https://swapi.co/api/starships'
    r = requests.get(url).json()
    res = r['results']
    ship_absolute = ''
    for ship in res:
        if ship['name'] == ship_name:
            ship_absolute = ship
            break
    return[ship_absolute['name'], ship_absolute['model'], [requests.get(film).json()['title'] for film in ship_absolute['films']]]


def species_detail(species_name):
    url = 'https://swapi.co/api/species'
    r = requests.get(url).json()
    res = r['results']
    species_absolute = ''
    for specie in res:
        if specie['name'] == species_name:
            species_absolute = specie
            break
    list_title = [requests.get(film).json()['title'] for film in species_absolute['films']]
    list_id = [requests.get(film).json()['episode_id'] for film in species_absolute['films']]
    sort = sorted(zip(list_id, list_title))
    return [species_absolute['name'], species_absolute['classification'], species_absolute['designation'], requests.get(species_absolute['homeworld']).json()['name'], sort]


def person_detail(name):
    url = 'https://swapi.co/api/people'
    r = requests.get(url).json()
    res = r['results']
    person_absolute = ''
    for person in res:
        if person['name'] == name:
            person_absolute = person
            break

    list_title = [requests.get(film).json()['title'] for film in person_absolute['films']]
    list_id = [requests.get(film).json()['episode_id'] for film in person_absolute['films']]
    sort = sorted(zip(list_id, list_title))
    return [person_absolute['name'], person_absolute['gender'], requests.get(person_absolute['homeworld']).json()['name'], sort]


def crawl(film_title_or_id):
    url = 'https://swapi.co/api/films'
    r = requests.get(url).json()
    res = r['results']
    film_absolute = ''
    for film in res:
        if film['title'] == film_title_or_id or film['episode_id'] == film_title_or_id:
            film_absolute = film
            break
    print(film_absolute['opening_crawl'])


def film_detail(film_identifier):
    url = 'https://swapi.co/api/films'
    r = requests.get(url).json()
    res = r['results']
    film_absolute = ''
    for film in res:
        if film['title'] == film_identifier or film['episode_id'] == film_identifier:
            film_absolute = film
            break
    list_char = [requests.get(char).json() for char in film_absolute['characters']]
    list_ship = [requests.get(char).json() for char in film_absolute['starships']]
    return [film_absolute['title'], film_absolute['director'], film_absolute['episode_id'], sorted([ch['name'] for ch in list_char]), sorted([ch['name'] for ch in list_ship])]


if __name__ == '__main__':
    print(ship_detail('Executor'))
    print(species_detail('Hutt'))
    print(person_detail('Luke Skywalker'))
    print(film_detail(3))
    print(film_detail('A New Hope'))
    crawl('The Phantom Menace')

