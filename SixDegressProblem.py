'''According to the Six Degrees of Kevin Bacon game, anyone
in the Hollywood film industry can be connected to Kevin Bacon
within six steps, where each step consists of finding a film that two actors both starred in.

In this problem, we’re interested in finding the shortest path
between any two actors by choosing a sequence of movies that
connects them. For example, the shortest path between Jennifer
Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to
Kevin Bacon by both starring in “X-Men: First Class,” and Kevin
Bacon is connected to Tom Hanks by both starring in “Apollo 13.”

We can frame this as a search problem: our states are people.
Our actions are movies, which take us from one actor to another
(it’s true that a movie could take us to multiple different actors, but
that’s okay for this problem). Our initial state and goal state are
defined by the two people we’re trying to connect. By using breadth-first
search, we can find the shortest path from one actor to another.'''
import csv
from collections import deque

import csv
from collections import deque

# Lese die Daten aus den CSV-Dateien ein
actors = {}
movies = {}
connections = {}

with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        actors[row['id']] = row['name']

with open('movies.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        movies[row['id']] = row['title']

with open('stars.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['person_id'] in connections:
            connections[row['person_id']].append(row['movie_id'])
        else:
            connections[row['person_id']] = [row['movie_id']]

# Implementiere with Breadth-First Search
def find_shortest_path(start_actor, end_actor):
    queue = deque([(start_actor, [start_actor])])
    visited = set()

    while queue:
        actor, path = queue.popleft()
        if actor == end_actor:
            return path
        if actor not in visited:
            visited.add(actor)
            for movie_id in connections.get(actor, []):
                for connected_actor in connections:
                    if movie_id in connections[connected_actor]:
                        queue.append((connected_actor, path + [connected_actor]))

    return None

# Beispielverwendung
start_actor = '102'  # Kevin Bacon
end_actor = '158'    # Tom Hanks
shortest_path = find_shortest_path(start_actor, end_actor)

if shortest_path:
    print(f"\nDer kürzeste Pfad zwischen {actors[start_actor]} und {actors[end_actor]} ist:")
    for actor in shortest_path:
        print(actors[actor])
else:
    print("Kein Pfad gefunden.\n")

# Beispiel 2: Pfad von Emma Watson zu Dustin Hoffman
start_actor = '914612'  # Emma Watson
end_actor = '163'       # Dustin Hoffman
shortest_path = find_shortest_path(start_actor, end_actor)

if shortest_path:
    print(f"Der kürzeste Pfad zwischen {actors[start_actor]} und {actors[end_actor]} ist:")
    for actor in shortest_path:
        print(actors[actor])
else:
    print("\nKein Pfad gefunden.")

# Beispiel 3: Pfad von Cary Elwes zu Sally Field
start_actor = '144'     # Cary Elwes
end_actor = '398'       # Sally Field
shortest_path = find_shortest_path(start_actor, end_actor)

if shortest_path:
    print(f"\nDer kürzeste Pfad zwischen {actors[start_actor]} und {actors[end_actor]} ist:")
    for actor in shortest_path:
        print(actors[actor])
else:
    print("Kein Pfad gefunden.\n")