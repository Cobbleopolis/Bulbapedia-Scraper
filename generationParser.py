import requests
import bs4

from pokemon import Pokemon

_listUrl = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
_res = requests.get(_listUrl)
_res.raise_for_status()
soup = bs4.BeautifulSoup(_res.text, "html.parser")


def get_generations():
    return [header for header in soup.select("h3") if header.text.startswith("Generation")]


def get_generation_tables():
    return [header.next_sibling.next_sibling for header in get_generations()]


def get_row_entries(gen_number):
    return [row.find_all() for row in get_generation_tables()[gen_number].find_all('tr')[1:]]


def get_pokemon_from_row_entry(row_entry):
    # for i in row_entry:
    #     print(i)
    print(row_entry)
    local_number = int(row_entry[0].text.strip()[1:])
    nat_number = -int(row_entry[1].text.strip()[1:])
    name = ""
    types = []
    return Pokemon(local_number, nat_number, name, types)
