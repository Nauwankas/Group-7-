from itertools import permutations

def print_project_description():
    print("=" * 60)
    print("Kenya Travelling Salesman Problem (TSP) Solver".center(60))
    print("=" * 60)
    print("Counties Involved: Nairobi, Meru, Nyeri, Nandi, Kericho, Nakuru\n")
    print("Goal:")
    print("- Start at Nairobi")
    print("- Visit all other towns once")
    print("- Return to Nairobi")
    print("- Find the shortest route (minimum total distance)\n")
    print("Instructions:")
    print("1. Make sure Python is installed.")
    print("2. Run this script: python kenya_tsp.py")
    print("3. You'll get the optimal route and total distance.\n")

towns = ["Nairobi", "Meru", "Nyeri", "Nandi", "Kericho", "Nakuru"]

distance_matrix = {
    "Nairobi": {"Meru": 225, "Nyeri": 150, "Nandi": 310, "Kericho": 275, "Nakuru": 160},
    "Meru": {"Nairobi": 225, "Nyeri": 105, "Nandi": 330, "Kericho": 300, "Nakuru": 210},
    "Nyeri": {"Nairobi": 150, "Meru": 105, "Nandi": 290, "Kericho": 260, "Nakuru": 170},
    "Nandi": {"Nairobi": 310, "Meru": 330, "Nyeri": 290, "Kericho": 80, "Nakuru": 190},
    "Kericho": {"Nairobi": 275, "Meru": 300, "Nyeri": 260, "Nandi": 80, "Nakuru": 120},
    "Nakuru": {"Nairobi": 160, "Meru": 210, "Nyeri": 170, "Nandi": 190, "Kericho": 120}
}

def calculate_total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i+1]]
    return total

def find_optimal_route():
    start = "Nairobi"
    other_towns = [town for town in towns if town != start]
    min_distance = float('inf')
    best_route = []

    for perm in permutations(other_towns):
        route = [start] + list(perm) + [start]
        distance = calculate_total_distance(route)
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

if __name__ == "__main__":
    print_project_description()
    route, distance = find_optimal_route()
    print("Optimal Route:")
    print(" -> ".join(route))
    print(f"Total Distance: {distance} km\n")
    print("=" * 60)
    print()
