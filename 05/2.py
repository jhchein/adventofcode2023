import re
from tqdm import tqdm
from collections import OrderedDict


numbers = re.compile(r"(\d+)")
seeds_and_ranges = re.compile(r"(\d+) (\d+)")

with open("input.txt", "r") as f:
    lines = f.readlines()


class Map:
    def __init__(self, map):
        self.map = map
        self._parse_map()

    def _parse_map(self):
        self.title = self.map.split("\n")[0].split()[0]
        self.lines = self.map.split("\n")[1:]
        self.sources2destinations = OrderedDict()
        self.destinations2sources = OrderedDict()
        for line in self.map.split("\n")[1:]:
            d, s, r = numbers.findall(line)
            d, s, r = int(d), int(s), int(r)
            self.sources2destinations[s] = (d, r)
            self.destinations2sources[d] = (s, r)
        self.sources2destinations = OrderedDict(sorted(self.sources2destinations.items(), key=lambda x: x[0]))
        self.destinations2sources = OrderedDict(sorted(self.destinations2sources.items(), key=lambda x: x[0]))

    def get_destination(self, source):
        for s, (d, r) in self.sources2destinations.items():
            if s <= source <= s + r - 1:
                return d + source - s
        return source

    def get_source(self, destination):
        for d, (s, r) in self.destinations2sources.items():
            if d <= destination <= d + r - 1:
                return s + destination - d
        if destination not in self.destinations2sources:
            return destination
        return None
    
    def __repr__(self):
        return f"Map ({self.title})"
    
    def __str__(self):
        return f"Map ({self.title})"

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
    
    # print results ordered by location
    valid_seeds = check_seeds(results, seeds_map)

    for location, destination in sorted(results.items(), key=lambda x: x[0]):
        if destination in valid_seeds:
            print(f"Location: {location} -> seed {destination}")
            break
    else:
        continue
    break
