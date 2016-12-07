import requests
import bs4

from pokemon import Pokemon

_base_url = "http://bulbapedia.bulbagarden.net/"

_listUrl = _base_url + "/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
_res = requests.get(_listUrl)
_res.raise_for_status()
listSoup = bs4.BeautifulSoup(_res.text, "html.parser")


def get_generations():
    return [header for header in listSoup.select("h3") if header.text.startswith("Generation")]


def get_generation_tables():
    return [header.next_sibling.next_sibling for header in get_generations()]


def get_pokemon_links_from_gen_number(gen_number):
    return get_pokemon_links_from_gen_table(get_generation_tables()[gen_number])


def get_pokemon_links_from_gen_table(gen_table):
    return [list(row.find_all())[3]['href'] for row in gen_table.find_all('tr')[1:]]


def get_all_pokemon_links():
    out = []
    for gen_table in get_generation_tables():
        out += get_pokemon_links_from_gen_table(gen_table)
    seen = set()
    seen_add = seen.add
    return [link for link in out if not (link in seen or seen_add(link))]



def get_pokemon_from_link(link):
    local_number = -1
    nat_number = -1
    name = ""
    types = []
    return Pokemon(local_number, nat_number, name, types)
