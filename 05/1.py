import re
from tqdm import tqdm


numbers = re.compile(r"(\d+)")

def map_destinations(sources: list, map: str) -> dict:
    """Returns a mapping of sources to destinations ({source: destination}}])"""
    map_lines = map.split("\n")[1:]                                                 # Remove first line (Title)
    processed_map = {
        source: int(destination_start) + (source - int(source_start))               # Create mapping: {source: destination + (source - start)}
        for map_line in map_lines
        for source in sources
        for destination_start, source_start, range in [numbers.findall(map_line)]   # destination, source, range
        if int(source_start) <= source <= int(source_start) + int(range) - 1        # if source is in range
    }
    return processed_map


with open("input.txt", "r") as f:
    lines = f.readlines()

seeds = [int(seed) for seed in lines[0].split()[1:]]                # Seeds are the first line of the input
results = {seed: seed for seed in seeds}                            # Initial Mapping: {seed: seed}

for map in tqdm("".join(lines).split("\n\n")[1:], desc="Maps"):     # Display progress bar for each map
    sources = list(results.values())
    mapping = map_destinations(sources, map)
    results = {k: mapping.get(v, v) for k, v in results.items()}    # Get the new destination for each seed. If the source was not in the map, keep the old destination.

print(f"Results: {results}")
print(f"Shortest: {min(results.values())} for seed {min(results, key=results.get)}")