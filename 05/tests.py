import re
from map import Map
    
def test_1(maps):
    results = {79: 81, 14:14, 55: 57, 13: 13}
    print("Test 1 (first map)")
    map = maps[0]
    seeds = [79, 14, 55, 13]
    for seed in seeds:
        print(f"Seed: {seed} -> {map.get_destination(seed)}")
        assert map.get_destination(seed) == results[seed]

def test_2(maps):
    seeds = [79, 14, 55, 13]
    results = {79: 82, 14:43, 55: 86, 13: 35}

    print("Test 2 (forward)")
    
    for seed in seeds:
        source = seed
        for map in maps:
            destination = map.get_destination(source)
            source = destination
    
        print(f"Seed: {seed} -> {destination}")
        assert destination == results[seed]

def test_3(maps):
    locations = [35, 86, 43, 82]
    results = {35: 13, 86: 55, 43: 14, 82: 79}

    print("Test 3 (reverse)")

    maps = maps[::-1]
    for location in locations:
        destination = location
        for map in maps:
            source = map.get_source(destination)
            destination = source
    
        print(f"Location: {location} -> {source}")
        assert source == results[location]
    
def test_4(maps):
    locations = list(range(100))
    results = {35: 13, 86: 55, 43: 14, 82: 79}

    print("Test 4 (reverse)")

    results = {}
    maps = maps[::-1]
    for location in locations:
        destination = location
        for map in maps:
            source = map.get_source(destination)
            destination = source
        results[location] = source
    
    valid_seeds = [79, 14, 55, 13]
    for location, destination in sorted(results.items(), key=lambda x: x[0]):
        if destination in valid_seeds:
            print(f"Location: {location} -> {destination}")
            assert destination == results[location]
    


if __name__ == "__main__":
    with open("example.txt", "r") as f:
        lines = f.readlines()
    
    numbers = re.compile(r"\d+")
    
    maps = "".join(lines).split("\n\n")[1:]
    maps = [Map(map) for map in maps]
    print(maps)

    test_1(maps)
    test_2(maps)
    test_3(maps)
    test_4(maps)