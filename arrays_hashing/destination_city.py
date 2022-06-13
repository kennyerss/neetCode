def destination_city(paths):
    """
    Given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
    Return the destination city, that is, the city without any path outgoing to another city.
    Guaranteed exactly one destination city.

    ex: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]] >> "Sao Paulo"
        paths = [["B","C"],["D","B"],["C","A"]] >> "A"
        paths = [["A","Z"]] >> "Z"

    Runtime: O(n) where n is the size of our array
    Space: O(n)
    """
    # Initialize our hash map {city: destination}
    hash_map = {}
    # Iterate through array paths and put each city and destination in our map
    for path in paths:
        # ["London":"New York"]
        hash_map[path[0]] = path[1]
    # Check which value is not a key >> return that value
    for destination in hash_map.values():
        if destination not in hash_map.keys():
            return destination


paths_1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
paths_2 = [["B", "C"], ["D", "B"], ["C", "A"]]
paths_3 = [["A", "Z"]]

print(destination_city(paths_1))
print(destination_city(paths_2))
print(destination_city(paths_3))
