from itertools import permutations  # Import permutations for generating all possible routes
import statistics  # For calculating average distance

# Function to print the project description and user instructions
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

# List of all towns involved in the route
towns = ["Nairobi", "Meru", "Nyeri", "Nandi", "Kericho", "Nakuru"]

# Dictionary that stores distances (in km) between every pair of towns
distance_matrix = {
    "Nairobi": {"Meru": 225, "Nyeri": 150, "Nandi": 310, "Kericho": 275, "Nakuru": 160},
    "Meru": {"Nairobi": 225, "Nyeri": 105, "Nandi": 330, "Kericho": 300, "Nakuru": 210},
    "Nyeri": {"Nairobi": 150, "Meru": 105, "Nandi": 290, "Kericho": 260, "Nakuru": 170},
    "Nandi": {"Nairobi": 310, "Meru": 330, "Nyeri": 290, "Kericho": 80, "Nakuru": 190},
    "Kericho": {"Nairobi": 275, "Meru": 300, "Nyeri": 260, "Nandi": 80, "Nakuru": 120},
    "Nakuru": {"Nairobi": 160, "Meru": 210, "Nyeri": 170, "Nandi": 190, "Kericho": 120}
}

# Function to calculate the total distance of a given route (a sequence of towns)
def calculate_total_distance(route):
    """
    Calculates the sum of distances along a given route.
    """
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]
    return total

# Function to evaluate all possible routes and determine the shortest one
def display_all_routes_and_find_optimal():
    """
    Generates all valid routes, prints their distances,
    identifies and displays the shortest route.
    """
    start = "Nairobi"
    other_towns = [town for town in towns if town != start]

    min_distance = float('inf')
    best_route = []
    all_distances = []

    print("All Possible Routes:\n")

    count = 0  # Counter for how many routes are checked

    for perm in permutations(other_towns):
        route = [start] + list(perm) + [start]
        distance = calculate_total_distance(route)
        all_distances.append(distance)
        count += 1

        print(f"{count:2d}. {' -> '.join(route)} = {distance} km")

        if distance < min_distance:
            min_distance = distance
            best_route = route

    # Compute stats
    max_distance = max(all_distances)
    avg_distance = statistics.mean(all_distances)

    # Display optimal route and summary
    print("\n" + "=" * 60)
    print("Optimal Route Found:")
    print(" -> ".join(best_route))
    print(f"Total Distance: {min_distance} km")
    print("=" * 60)
    print(f"Total Routes Checked: {count}")
    print(f"Longest Distance: {max_distance} km")
    print(f"Average Distance: {avg_distance:.2f} km")
    print("=" * 60)

    # Save result to file
    with open("tsp_optimal_route.txt", "w") as f:
        f.write("Kenya TSP - Optimal Route\n")
        f.write(" -> ".join(best_route) + "\n")
        f.write(f"Total Distance: {min_distance} km\n")
        f.write(f"Routes Checked: {count}\n")

    print("Optimal route saved to 'tsp_optimal_route.txt'\n")

# Main execution block
if __name__ == "__main__":
    print_project_description()
    display_all_routes_and_find_optimal()
