from itertools import permutations

# Function to print project description and instructions
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

# List of towns to visit
towns = ["Nairobi", "Meru", "Nyeri", "Nandi", "Kericho", "Nakuru"]

# Dictionary containing distances between each pair of towns
distance_matrix = {
    "Nairobi": {"Meru": 225, "Nyeri": 150, "Nandi": 310, "Kericho": 275, "Nakuru": 160},
    "Meru": {"Nairobi": 225, "Nyeri": 105, "Nandi": 330, "Kericho": 300, "Nakuru": 210},
    "Nyeri": {"Nairobi": 150, "Meru": 105, "Nandi": 290, "Kericho": 260, "Nakuru": 170},
    "Nandi": {"Nairobi": 310, "Meru": 330, "Nyeri": 290, "Kericho": 80, "Nakuru": 190},
    "Kericho": {"Nairobi": 275, "Meru": 300, "Nyeri": 260, "Nandi": 80, "Nakuru": 120},
    "Nakuru": {"Nairobi": 160, "Meru": 210, "Nyeri": 170, "Nandi": 190, "Kericho": 120}
}

# Function to calculate total distance of a given route
def calculate_total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i+1]]
    return total

# Function to display all possible routes and find the optimal one
def display_all_routes_and_find_optimal():
    start = "Nairobi"  # Starting point
    other_towns = [town for town in towns if town != start]  # List of towns excluding start
    min_distance = float('inf')  # Initialize with infinity
    best_route = []  # To store the shortest route

    print("All Possible Routes:\n")

    # Generate all permutations of towns and calculate distance
    for perm in permutations(other_towns):
        route = [start] + list(perm) + [start]  # Full route including return to start
        distance = calculate_total_distance(route)  # Calculate total distance for route
        print(" -> ".join(route), f"= {distance} km")  # Print route and distance

        # Check if current route is shorter than the previously found shortest
        if distance < min_distance:
            min_distance = distance
            best_route = route

    # Display the optimal route
    print("\n" + "=" * 60)
    print("Optimal Route:")
    print(" -> ".join(best_route))
    print(f"Total Distance: {min_distance} km")
    print("=" * 60)
    print()

# Main execution
if __name__ == "__main__":
    print_project_description()
    display_all_routes_and_find_optimal()

