from itertools import permutations
import matplotlib.pyplot as plt

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

# Towns and their coordinates (for visualization only)
town_coordinates = {
    "Nairobi": (0, 0),
    "Meru": (2, 4),
    "Nyeri": (1, 3),
    "Nandi": (-4, 6),
    "Kericho": (-3, 4),
    "Nakuru": (-1, 2)
}

towns = list(town_coordinates.keys())

# Distance matrix
distance_matrix = {
    "Nairobi": {"Meru": 225, "Nyeri": 150, "Nandi": 310, "Kericho": 275, "Nakuru": 160},
    "Meru": {"Nairobi": 225, "Nyeri": 105, "Nandi": 330, "Kericho": 300, "Nakuru": 210},
    "Nyeri": {"Nairobi": 150, "Meru": 105, "Nandi": 290, "Kericho": 260, "Nakuru": 170},
    "Nandi": {"Nairobi": 310, "Meru": 330, "Nyeri": 290, "Kericho": 80, "Nakuru": 190},
    "Kericho": {"Nairobi": 275, "Meru": 300, "Nyeri": 260, "Nandi": 80, "Nakuru": 120},
    "Nakuru": {"Nairobi": 160, "Meru": 210, "Nyeri": 170, "Nandi": 190, "Kericho": 120}
}

def calculate_total_distance(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

# Function to visualize a given route
def visualize_route(route, title="Route", color='blue', show_plot=True):
    x = [town_coordinates[t][0] for t in route]
    y = [town_coordinates[t][1] for t in route]

    plt.plot(x, y, marker='o', color=color, linewidth=2)
    for i, town in enumerate(route):
        plt.text(x[i], y[i]+0.2, town, ha='center', fontsize=9)

    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    if show_plot:
        plt.show()

# Main TSP logic with visualization
def display_all_routes_and_find_optimal():
    start = "Nairobi"
    other_towns = [town for town in towns if town != start]
    min_distance = float('inf')
    best_route = []

    print("All Possible Routes:\n")

    for idx, perm in enumerate(permutations(other_towns)):
        route = [start] + list(perm) + [start]
        distance = calculate_total_distance(route)
        print(" -> ".join(route), f"= {distance} km")

        # Plot only first few for speed (optional)
        if idx < 3:  # remove limit to plot all
            visualize_route(route, title=f"Route #{idx+1}: {distance} km", show_plot=False)

        if distance < min_distance:
            min_distance = distance
            best_route = route

    # Final optimal route
    print("\n" + "=" * 60)
    print("Optimal Route:")
    print(" -> ".join(best_route))
    print(f"Total Distance: {min_distance} km")
    print("=" * 60)

    visualize_route(best_route, title=f"Optimal Route: {min_distance} km", color='green')

# Main execution
if __name__ == "__main__":
    print_project_description()
    display_all_routes_and_find_optimal()
