import generationParser
from pokemon import Pokemon

# for table in generationParser.soup.select("table"):
#     print(str(table))
rows = generationParser.get_row_entries(0)
p = generationParser.get_pokemon_from_row_entry(rows[0])
print(p)
# for row in generationParser.get_row_entries(0):
#     p = generationParser.get_pokemon_from_row_entry(row)
#     print(p)
