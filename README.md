from itertools import permutations

# List of towns
towns = ["Nairobi", "Meru", "Nyeri", "Nandi", "Kericho", "Nakuru"]

# Distance matrix (in km)
# Matrix[i][j] represents distance from towns[i] to towns[j]
distance_matrix = [
    # Nai  Meru  Nyeri Nandi Kericho Nakuru
    [  0,   225,   150,  310,   275,   160],  # Nairobi
    [225,     0,   105,  330,   300,   210],  # Meru
    [150,   105,     0,  290,   260,   170],  # Nyeri
    [310,   330,   290,    0,    80,   190],  # Nandi
    [275,   300,   260,   80,     0,   120],  # Kericho
    [160,   210,   170,  190,   120,     0],  # Nakuru
]

# Function to calculate the total distance of a route
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    return total_distance

# Index of Nairobi
start_index = towns.index("Nairobi")

# Generate all permutations of intermediate towns (excluding Nairobi)
town_indices = list(range(len(towns)))
intermediate_indices = town_indices[1:]  # exclude Nairobi

min_distance = float('inf')
optimal_route = None

# Try all permutations of the intermediate towns
for perm in permutations(intermediate_indices):
    # Complete route: start at Nairobi -> permuted towns -> back to Nairobi
    route = [start_index] + list(perm) + [start_index]
    distance = calculate_total_distance(route, distance_matrix)

    if distance < min_distance:
        min_distance = distance
        optimal_route = route

# Convert indices back to town names
optimal_town_route = [towns[i] for i in optimal_route]

# Output
print("Optimal Route:")
print(" -> ".join(optimal_town_route))
print(f"Total Distance: {min_distance} km")
