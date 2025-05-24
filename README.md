TSP Product Distribution Project – Kenya Counties
This project solves the Travelling Salesman Problem (TSP) to determine the shortest route for distributing a product across six counties in Kenya. It ensures each county is visited exactly once and the route returns to the starting point (Nairobi).
Problem Statement
A company wants to deliver its product to the following counties:
•	Nairobi (Start and End)
•	Meru
•	Nyeri
•	Nandi
•	Kericho
•	Nakuru
The goal is to minimize the total travel distance while visiting each county exactly once and returning to the starting point.
Technology Used
•	Python 3.x
•	Standard Python Library: itertools
Distance Matrix (in kilometers)
The distances are stored in a dictionary format:
distance_matrix = {
    "Nairobi": {"Meru": 225, "Nyeri": 150, "Nandi": 310, "Kericho": 275, "Nakuru": 160},
    "Meru": {"Nairobi": 225, "Nyeri": 105, "Nandi": 330, "Kericho": 300, "Nakuru": 210},
    "Nyeri": {"Nairobi": 150, "Meru": 105, "Nandi": 290, "Kericho": 260, "Nakuru": 170},
    "Nandi": {"Nairobi": 310, "Meru": 330, "Nyeri": 290, "Kericho": 80, "Nakuru": 190},
    "Kericho": {"Nairobi": 275, "Meru": 300, "Nyeri": 260, "Nandi": 80, "Nakuru": 120},
    "Nakuru": {"Nairobi": 160, "Meru": 210, "Nyeri": 170, "Nandi": 190, "Kericho": 120}
}
How It Works
1.	Defines the list of counties and distances between each pair using a dictionary.
2.	Uses itertools.permutations to generate all possible routes (excluding Nairobi).
3.	Appends Nairobi at the start and end of each route.
4.	Calculates the total distance for each route.
5.	Finds and displays the shortest route and its distance.
Sample Output
All Possible Routes:

Nairobi -> Meru -> Nyeri -> Nandi -> Kericho -> Nakuru -> Nairobi = 1280 km
Nairobi -> Meru -> Nyeri -> Nandi -> Nakuru -> Kericho -> Nairobi = 1270 km
...
============================================================
Optimal Route:
Nairobi -> Nyeri -> Meru -> Nakuru -> Kericho -> Nandi -> Nairobi
Total Distance: 1155 km
============================================================
License
This project is open source and available under the MIT License.

