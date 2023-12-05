import re
from tqdm import tqdm


numbers = re.compile(r"(\d+)")


def get_destination(sources, map):
    map_lines = map.split("\n")[1:]
    processed_map = {source: int(d) + (source - int(s)) for map_line in map_lines for source in sources
                     for d, s, r in [numbers.findall(map_line)] if int(s) <= source <= int(s) + int(r) - 1}
    return processed_map


with open("input.txt", "r") as f:
    lines = f.readlines()

seeds = [int(seed) for seed in lines[0].split()[1:]]
results = {seed: seed for seed in seeds}

for map in tqdm("".join(lines).split("\n\n")[1:], desc="Maps"):
    mapping = get_destination(list(results.values()), map)
    results = {k: mapping.get(v, v) for k, v in results.items()}
    # print(f"Results: {results}")

print(f"Results: {results}")
print(f"Shortest: {min(results.values())} for seed {min(results, key=results.get)}")