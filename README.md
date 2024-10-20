# New-England-Route-Planner

This project implements a route planner for New England state capitals using fundamental graph algorithms like Breadth-First Search (BFS), Depth-First Search (DFS), and Dijkstra's algorithm. The app uses **Streamlit** as the front-end interface and **Folium** to visualize the map and routes between the cities.

## Overview

The New England Route Planner is a web-based application that allows users to visualize paths and calculate the shortest routes between various state capitals in New England. Users can choose between BFS, DFS, and Dijkstra's algorithm to find routes between the cities.

## Features

- **Graph Algorithms**: Implementations of BFS, DFS, and Dijkstra's algorithm.
- **Map Visualization**: Geographical visualization of routes between the capitals using Folium.
- **Interactive Interface**: Streamlit-based interface for selecting starting points and algorithms, and viewing results on a map.
- **State Capitals Included**:
  - Hartford (Connecticut)
  - Augusta (Maine)
  - Boston (Massachusetts)
  - Concord (New Hampshire)
  - Providence (Rhode Island)
  - Montpelier (Vermont)

## Algorithms Implemented

### Breadth-First Search (BFS)
- BFS traverses the graph level by level and is particularly useful for finding the shortest path in unweighted graphs.

### Depth-First Search (DFS)
- DFS explores as far down a branch as possible before backtracking. It’s useful for exploring all possible paths in a graph.

### Dijkstra's Algorithm
- Dijkstra's algorithm finds the shortest path between a source node and all other nodes in a weighted graph.

## Technologies Used

- **Python**: The primary programming language.
- **Streamlit**: Web framework for creating the user interface.
- **Folium**: Used for interactive map visualizations.
- **NetworkX**: For creating and managing the graph data structure.
- **Matplotlib**: For additional graph visualization.

## Application

This project creates an API to help tourists plan trips between the capitals of the New England states. The graph data structure represents the cities as nodes and the roads between them as edges with weights representing distances.

### State Capitals

1. Hartford (Connecticut)
2. Augusta (Maine)
3. Boston (Massachusetts)
4. Concord (New Hampshire)
5. Providence (Rhode Island)
6. Montpelier (Vermont)

## How to Run Locally

### Requirements
- Python 3.x
- Install dependencies using the following command:

```bash
pip install -r requirements.txt
```
### Running the App
- Clone the repository:
  ```bash
  git clone https://github.com/your-username/NewEnglandRoutePlanner.git
  ```
- Navigate to the project directory:
  ``` bash
  cd NewEnglandRoutePlanner
  ```
- Run the Streamlit app:
  ```bash
  streamlit run app.py
  ```
- Open the local URL in your browser

## Visualizations

The app displays the state capitals and the routes between them on an interactive map.
Users can choose their preferred graph algorithm, and the results are dynamically displayed on the map using Folium.
Project Report

For a detailed analysis of the algorithms and their implementation, refer to the Report.pdf included in the repository.

## References

- GeeksForGeeks - BFS Algorithm
- GeeksForGeeks - DFS Algorithm
- Dijkstra's Algorithm - Scaler

## Contributors

- Gowtham Saravanan
- Sarvesh Krishnan Rajendran
