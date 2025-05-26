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
    print("3. You'll need to input distances between towns.")
    print("4. You'll get the optimal route and total distance.\n")

# Towns to be visited 
towns = ["Nairobi", "Meru", "Nyeri", "Nandi", "Kericho", "Nakuru"]

def get_user_distances():
    
    #Gets distances between towns from user input.
    #Returns a distance matrix dictionary with symmetric distances.
   
    distance_matrix = {town: {} for town in towns}    
    print("\nEnter distances between towns (in kilometers):")
    print("Note: Distance from Town A to Town B will be the same as Town B to Town A")
    
    # Loop through all unique pairs of towns
    for i in range(len(towns)):
        for j in range(i + 1, len(towns)):
            town1 = towns[i]
            town2 = towns[j]
            
            while True:
                try:
                    distance = float(input(f"Distance from {town1} to {town2}: "))
                    if distance <= 0:
                        print("Distance must be positive. Please try again.")
                        continue
                        
                    # Set distance in both directions
                    distance_matrix[town1][town2] = distance
                    distance_matrix[town2][town1] = distance
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
    
    return distance_matrix
    
 #Function to calculate total distance of a given route using the provided distance matrix.
def calculate_total_distance(route, distance_matrix):  
    
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i+1]]
    return total

#Function to display all possible routes and find the optimal one.
 #Uses the provided distance matrix for calculations.
def display_all_routes_and_find_optimal(distance_matrix):    
    start = "Nairobi"
    other_towns = [town for town in towns if town != start]
    min_distance = float('inf')
    best_route = []

    print("\nAll Possible Routes:\n")

    for perm in permutations(other_towns):
        route = [start] + list(perm) + [start]
        distance = calculate_total_distance(route, distance_matrix)
        print(" -> ".join(route), f"= {distance} km")

        if distance < min_distance:
            min_distance = distance
            best_route = route

    print("\n" + "=" * 60)
    print("Optimal Route:")
    print(" -> ".join(best_route))
    print(f"Total Distance: {min_distance} km")
    print("=" * 60)

if __name__ == "__main__":
    print_project_description()
    
    # Get distances from user
    distance_matrix = get_user_distances()
    
    # Pass the user-provided distance matrix to the route finder
    display_all_routes_and_find_optimal(distance_matrix)
