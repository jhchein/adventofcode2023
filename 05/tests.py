import re
from collections import OrderedDict

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
    
def test_1(maps):
    map = maps[0]
    seeds = [79, 14, 55, 13]
    for seed in seeds:
        print(f"Seed: {seed} -> {map.get_destination(seed)}")

def test_2(maps):
    seeds = [79, 14, 55, 13]

    print("Test 2 (forward)")
    
    for seed in seeds:
        source = seed
        for map in maps:
            # print(f"Getting destination for {source} in {map}")
            destination = map.get_destination(source)
            print(f"Seed: {seed} -> Map: {map} -> {source} -> {destination}")
            source = destination
    
        print(f"Seed: {seed} -> {destination}")

def test_3(maps):
    locations = [35, 86, 43, 82]

    print("Test 3 (reverse)")

    maps = maps[::-1]
    for location in locations:
        destination = location
        for map in maps:
            source = map.get_source(destination)
            print(f"Location: {location} -> Map: {map} -> {destination} -> {source}")
            destination = source
    
        print(f"Location: {location} -> {source}")
    
def test_4(maps):
    locations = list(range(100))

    print("Test 4 (reverse)")

    results = {}
    maps = maps[::-1]
    for location in locations:
        destination = location
        for map in maps:
            source = map.get_source(destination)
            # print(f"Location: {location} -> Map: {map} -> {destination} -> {source}")
            destination = source
    
        # print(f"Location: {location} -> {source}")
        results[location] = source
    
    # print results ordered by location
    valid_seeds = [79, 14, 55, 13]
    for location, destination in sorted(results.items(), key=lambda x: x[0]):
        if destination in valid_seeds:
            print(f"Location: {location} -> {destination}")

if __name__ == "__main__":
    with open("example.txt", "r") as f:
        lines = f.readlines()
    
    numbers = re.compile(r"\d+")
    
    maps = "".join(lines).split("\n\n")[1:]
    maps = [Map(map) for map in maps]
    print(maps)

    # test_1(maps)
    # test_2(maps)
    # test_3(maps)
    test_4(maps)