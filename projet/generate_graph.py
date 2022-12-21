import random
import re
import json

class Graph:
    
    def __init__(self):
        self.adjancency_list = {}
        self.vertices_number = 0

    # Function for generating randomly
    def generate_graph(self, vertices_number):
        # P is the probability to have an edge
        p = random.randint(0,1)
        # p = 0.4
        self.vertices_number = vertices_number
        for n in range(self.vertices_number):
            self.adjancency_list[n] = []
            for m in range(self.vertices_number):
                if n != m:
                    if random.randint(0,1) <= p:
                        self.adjancency_list[n].append(m)
        # for loop to complete the neighbours of all other vertices
        for n in self.adjancency_list:
            for m in self.adjancency_list[n]:
                if n not in self.adjancency_list[m]:
                    self.adjancency_list[m].append(n)

    def display_graph(self):
        print(self.adjancency_list)

    # Function that returns the number of paths of length 2 in the adjancency list
    def vertices_of_path_two(self):
        count = 0
        for x in self.adjancency_list:
            liste_voisin = self.adjancency_list[x]
            for i in liste_voisin:
                for j in self.adjancency_list[i]:
                    if x != j:
                        if j not in self.adjancency_list[x]:
                            count += 1
        return int(count/2)

    # Function to extract the data in texts files
    def extract_data(self, file_name, destination_file):
        fichier = open(file_name)
        temp_list = []
        for line in fichier:
            temp_liste = re.split('\t|\n| ', line)
            if temp_liste[0] not in self.adjancency_list.keys():
                self.adjancency_list[temp_liste[0]] = []
            self.adjancency_list[temp_liste[0]].append(temp_liste[1])
        
        # This loop is to make sure that all the neighbours of the vertices are corresponding neighbours
        temp_list_neighbour = []
        for n in self.adjancency_list:
            for m in self.adjancency_list[n]:
                if m not in self.adjancency_list:
                    temp_list_neighbour.append(m)
        for n in temp_list_neighbour:
            self.adjancency_list[n] = []
                    
        # This loop is to complete the neighbours of all other vertices
        for n in self.adjancency_list:
            for m in self.adjancency_list[n]:
                if n not in self.adjancency_list[m]:
                    self.adjancency_list[m].append(n)
        # json_file = open(destination_file, "w")
        # json_file.write(json.dumps(self.adjancency_list))
        with open(destination_file, 'w') as f:
            json.dump(self.adjancency_list, f)

    # Read the json content of a text file
    def read_data(self, file_name):
        file = open(file_name)
        self.adjancency_list = json.load(file)

graph = Graph()
# graph.extract_data("facebook_combined.txt", "file.json")
# graph.read_data("facebook_json.txt")
# print("This is the number : ", graph.vertices_of_path_two())