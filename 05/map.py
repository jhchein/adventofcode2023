from collections import OrderedDict
import re


numbers_pattern = re.compile(r"(\d+)")

class Map:
    def __init__(self, map):
        self.map = map
        self._parse_map()

    def _parse_map(self):
        self.title = self.map.split("\n")[0].split()[0]
        self.lines = self.map.split("\n")[1:]
        
        self.sources2destinations = {}
        self.destinations2sources = {}

        for line in self.lines:
            d, s, r = numbers_pattern.findall(line)
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