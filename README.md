# Project Overview
This Python project solves a Travelling Salesman Problem (TSP) to find the shortest route for distributing a product across 6 counties in Kenya. It starts and ends in Nairobi, visiting each county exactly once.


# Problem Statement
A company wants to deliver its product to the following towns:
- Nairobi (Start and End)
- Meru
- Nyeri
- Nandi
- Kericho
- Nakuru
  
The objective is to minimize the total travel distance while visiting each town once and returning to the starting point.

#  Technology Used
  . Python 3.x
  . Google Maps Distance Matrix API
  . Libraries:
  . googlemaps
  . itertools
  . matplotlib
  . tabulate
  . time
  . webbrowser


# Distance Matrix (in kilometers)

| From \ To | Nairobi | Meru | Nyeri | Nandi | Kericho | Nakuru |
|-----------|---------|------|-------|--------|---------|--------|
| Nairobi   | 0       | 225 | 150   | 310    | 275     | 160    |
| Meru      | 225     | 0    | 105   | 330    | 300     | 210    |
| Nyeri     | 150     | 105 | 0     | 290    | 260     | 170    |
| Nandi     | 310     | 330 | 290   | 0      | 80      | 190    |
| Kericho   | 275     | 300 | 260   | 80     | 0       | 120    |
| Nakuru    | 160     | 210 | 170   | 190    | 120     | 0      |

# How It Works
1. Fetches real road distances using Google Maps API.
2. Generates all possible routes (permutations).
3. Each route starts and ends in Nairobi.
4. Calculates total distance for each route.
5. Selects and displays the shortest route.
6. Plots the best route on a graph.
7. Opens the optimal route on Google Maps.



