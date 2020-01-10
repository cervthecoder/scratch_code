import requests

spec_url = ''

def gj(spec_url):
    sw = requests.get('https://swapi.co/api/' + spec_url).json()
    res = sw['results']
    return res


def get(sub, what, spec):
    return [requests.get(temp).json()[what] for temp in sub[spec]]


def ship_detail(ship_name):
    global list_ship
    spec_url = 'starships'
    for ship in gj(spec_url):
        if ship['name'] == ship_name:
            list_ship = [ship['name'], ship['model'], ship['starship_class'], ship['hyperdrive_rating'],
                         get(ship, 'title', 'films')]
    return list_ship


def species_detail(species_name):
    global list_species
    spec_url = 'species'
    for specie in gj(spec_url):
        if specie['name'] == species_name:
            planet = requests.get(specie['homeworld']).json()
            list_species = [specie['name'], specie['classification'], specie['designation'], planet['name'], [requests.get(title).json()['title'] for title in specie['films']]]
    return list_species


def person_detail(name):
    global list_people
    spec_url = 'people'
    for person in gj(spec_url):
        if person['name'] == name:
            planet = requests.get(person['homeworld']).json()
            list_people = [person['name'], person['gender']], planet['name'], [requests.get(title).json()['title'] for title in person['films']]
    return list_people


def film_detail(film_):
    global list_film
    spec_url = 'films'
    for film in gj(spec_url):
        if film['title'] == film_ or film['episode_id'] == film_:
            list_film = [film['title'], film['director'], film['episode_id'], get(film, 'name', 'characters'),
                         get(film, 'name', 'starships')]
    return list_film


def crawl(film_title):
    spec_url = 'films'
    for film in gj(spec_url):
        if film['title'] == film_title or film['episode_id'] == film_title:
            print(film['opening_crawl'])

if __name__ == '__main__':
    #  print(ship_detail('Death Star'))
    #  crawl('Return of the Jedi')
    #  crawl(1)
    #  print(film_detail('Attack of the Clones'))
    #  print(film_detail(5))
    print(person_detail('Obi-Wan Kenobi'))
    #print(species_detail('Hutt'))