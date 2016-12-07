import generationParser
from pokemon import Pokemon

# for table in generationParser.soup.select("table"):
#     print(str(table))
links = generationParser.get_all_pokemon_links()
for l in links:
    print(l)
print(len(links))
# for row in generationParser.get_row_entries(0):
#     p = generationParser.get_pokemon_from_row_entry(row)
#     print(p)
