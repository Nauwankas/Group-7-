import googlemaps #To get real road distances
from itertools import permutations #To generate all possible routes
import matplotlib.pyplot as plt  #To plot optimal route
from tabulate import tabulate  #To display route data in table format
import time # To add delays (e.g., before opening the browser)
import webbrowser # To open the best route in your browser on Google Maps

# Project description
def print_project_description():
    print("=" * 70)
    print("Kenya Travelling Salesman Problem (TSP) Solver".center(70))
    print("=" * 70)
    print("Counties Involved: Nairobi, Meru, Nyeri, Nandi, Kericho, Nakuru\n")
    print("Goal:")
    print("- Start at Nairobi")
    print("- Visit all other towns once")
    print("- Return to Nairobi")
    print("- Find the shortest route using real road distances via Google Maps API\n")

# Coordinates (longitude, latitude) for each town
town_coordinates = {
    "Nairobi": (36.8219, -1.2921),
    "Meru": (37.6525, 0.0463),
    "Nyeri": (36.9510, -0.4197),
    "Nandi": (35.1531, 0.1209),
    "Kericho": (35.2833, -0.3667),
    "Nakuru": (36.0800, -0.3031)
}

towns = list(town_coordinates.keys()) #Create a list of town names

# Build distance matrix using coordinates
def build_distance_matrix(api_key):
    gmaps = googlemaps.Client(key=api_key)
    distance_matrix = {town: {} for town in towns}

    for from_town in towns: # Loop through each pair of towns to get the distance
        for to_town in towns:
            if from_town == to_town:
                distance_matrix[from_town][to_town] = 0
                continue
            try:                
                result = gmaps.distance_matrix(  
                    origins=[town_coordinates[from_town][::-1]], # Google Maps expects coordinates in (lat, lng) format, so we reverse the tuple
                    destinations=[town_coordinates[to_town][::-1]],
                    mode="driving",
                    units="metric"
                )
                element = result['rows'][0]['elements'][0]
                if element['status'] == 'OK':
                    distance = element['distance']['value'] / 1000  # meters to km
                    distance_matrix[from_town][to_town] = round(distance, 1)
                else:
                    distance_matrix[from_town][to_town] = float('inf') # If API fails
            except Exception as e:
                print(f"Error between {from_town} and {to_town}: {e}")
                distance_matrix[from_town][to_town] = float('inf')

    return distance_matrix

# Compute total distance
def calculate_total_distance(route, matrix):
    total = 0
    for i in range(len(route) - 1):
        dist = matrix[route[i]][route[i + 1]]
        if dist == float('inf'):
            return float('inf')
        total += dist
    return total

# Plot best route
def plot_best_route(route, distance):
    x = [town_coordinates[t][0] for t in route]
    y = [town_coordinates[t][1] for t in route]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='green', linewidth=2)
    for i, town in enumerate(route):
        plt.text(x[i], y[i] + 0.05, town, ha='center')

    plt.title(f"Optimal Route ({distance:.1f} km)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Open route in browser
def open_route_in_browser(route):
    base_url = "https://www.google.com/maps/dir/"
    waypoints = "/".join(route)
    print("🕒 Opening route in Google Maps in 2 seconds...")
    time.sleep(2)
    webbrowser.open(base_url + waypoints)

# TSP solver
def find_optimal_route(matrix):
    start = "Nairobi"
    others = [t for t in towns if t != start]
    min_distance = float('inf')
    best_route = []
    summary = []

    print("\nEvaluating all possible routes...\n")

    for idx, perm in enumerate(permutations(others)):
        route = [start] + list(perm) + [start]
        total = calculate_total_distance(route, matrix)
        readable_distance = f"{total:.1f} km" if total != float('inf') else "Unavailable"
        summary.append([idx + 1, " → ".join(route), readable_distance])

        if total < min_distance:
            min_distance = total
            best_route = route

    print(tabulate(summary, headers=["#", "Route", "Distance"], tablefmt="grid"))

    print("\n" + "=" * 70)
    if best_route:
        print("✅ Optimal Route:")
        print(" → ".join(best_route))
        print(f"Total Distance: {min_distance:.1f} km")
        plot_best_route(best_route, min_distance)
        open_route_in_browser(best_route)
    else:
        print("❌ No valid route found.")
    print("=" * 70)

# Run program
if __name__ == "__main__":
    print_project_description()

    API_KEY = 'AIzaSyBMQhiM9cac7e1UXIHUUy3ag82luY7LplM'  # Replace with your key
    matrix = build_distance_matrix(API_KEY)

    if matrix:
        find_optimal_route(matrix)
    else:
        print("Failed to retrieve distance matrix. Check your API key or internet.")
