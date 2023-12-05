import re
from tqdm import tqdm
from map import Map


seeds_and_ranges = re.compile(r"(\d+) (\d+)")

with open("input.txt", "r") as f:
    lines = f.readlines()


def check_seeds(results, seeds_map):
    seeds_map_iter = iter(seeds_map)
    return_value = {}
    for start, r in seeds_map_iter:
        for location, seed in results.items():
            if int(start) <= seed <= int(start) + int(r) - 1:
                return_value[seed] = location
    return return_value
    
step_size = 10000
seeds_map = seeds_and_ranges.findall(lines[0])
reverse_maps = "".join(lines).split("\n\n")[1:][::-1]

reverse_maps = [Map(map) for map in reverse_maps]
print(f"Reverse maps: {reverse_maps}")


# iterate over all billions of locations
for location_range_start in tqdm(range(0, 1000000000, step_size), desc="Locations"):
    locations = range(location_range_start, location_range_start + step_size)

    results = {}
    maps = reverse_maps
    for location in locations:
        destination = location
        for map in maps:
            source = map.get_source(destination)
            destination = source
        results[location] = source
    
    valid_seeds = check_seeds(results, seeds_map)
    for location, destination in sorted(results.items(), key=lambda x: x[0]):
        if destination in valid_seeds:
            print(f"Location: {location} -> seed {destination}")
            break
    else:
        continue
    break
