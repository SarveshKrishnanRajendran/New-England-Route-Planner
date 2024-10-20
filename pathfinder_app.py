#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import folium
from streamlit_folium import st_folium
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.distances = {}

    def add_node(self, value, lat, lon):
        self.nodes[value] = (lat, lon)

    def add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, []).append(to_node)
        self.distances[(from_node, to_node)] = distance

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph.edges.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return bfs_order

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for next_node in graph.edges.get(start, []):
        if next_node not in visited:
            dfs(graph, next_node, visited)
    return visited

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {initial: None}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def visualize_graph(graph, path_data, algorithm):
    map_center = graph.nodes[next(iter(graph.nodes))]  # Default to the first node's position
    folium_map = folium.Map(location=map_center, zoom_start=10)

    # Draw nodes
    for node, position in graph.nodes.items():
        folium.Marker(position, popup=node).add_to(folium_map)

    # Draw lines for paths
    if algorithm in ["BFS", "DFS"]:
        for i in range(len(path_data)-1):
            start_pos = graph.nodes[path_data[i]]
            end_pos = graph.nodes[path_data[i+1]]
            line = folium.PolyLine(locations=[start_pos, end_pos], weight=5, color='blue')
            folium_map.add_child(line)
    elif algorithm == "Dijkstra":
        for node, parent in path_data.items():
            if parent is not None:
                start_pos = graph.nodes[parent]
                end_pos = graph.nodes[node]
                line = folium.PolyLine(locations=[start_pos, end_pos], weight=5, color='red')
                folium_map.add_child(line)

    return folium_map




# Setup Graph
g = Graph()
places = {
    
    "Hartford": (41.7658, -72.6734),
    'Augusta': (44.3106, -69.7795),
    'Boston': (42.3601, -71.0589),
    'Concord': (43.2081, -71.5376),
    'Providence': (41.8240, -71.4128),
    'Montpelier': (44.2601, -72.5754)

}

for place, coords in places.items():
    g.add_node(place, *coords)

edges = [   
    ('Hartford', 'Augusta', 228.73),
    ('Boston', 'Hartford', 92.61),
    ('Concord', 'Hartford', 115.23),
    ('Providence', 'Hartford', 65.23),
    ('Montpelier', 'Hartford', 172.25),
    ('Augusta', 'Boston', 149.28),
    ('Augusta', 'Concord', 116.33),
    ('Augusta', 'Providence', 190.51),
    ('Augusta', 'Montpelier', 138.71),
    ('Concord', 'Boston', 63.39),
    ('Providence', 'Boston', 41.23),
    ('Montpelier', 'Boston', 151.81),
    ('Concord', 'Providence', 95.75),
    ('Montpelier', 'Concord', 89.30),
    ('Montpelier', 'Providence', 178.16)
]

for from_node, to_node, weight in edges:
    g.add_edge(from_node, to_node, weight)

st.title('Graph Algorithm Visualizer on a Map')
start_point = st.selectbox("Choose starting node:", list(g.nodes.keys()))
algorithm = st.radio("Choose an algorithm:", ["BFS", "DFS", "Dijkstra"])

if st.button("Run Algorithm"):
    path_data = None
    if algorithm == "BFS":
        visited_order = bfs(g, start_point)
        path_data = visited_order  # For BFS, the path is the visited order
    elif algorithm == "DFS":
        visited_order = dfs(g, start_point)
        path_data = visited_order  # For DFS, the path is also the visited order
    elif algorithm == "Dijkstra":
        distances, path = dijkstra(g, start_point)
        path_data = path  # For Dijkstra, the path is a dictionary of predecessors
        st.write("Distances from Start:", distances)
    
    # Store the map in session_state after running the algorithm and visualizing the graph
    st.session_state['map'] = visualize_graph(g, path_data, algorithm)

if 'map' in st.session_state:
    st_folium(st.session_state['map'], width=725, height=500)


# In[ ]:




