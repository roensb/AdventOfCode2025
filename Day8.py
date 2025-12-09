import math

class circuit(object):
    def __init__(self,starting_junction):
        self.junctions = [starting_junction]

    def __str__(self):
        return f"{self.junctions}"

    def add_junction(self, junction):
        if junction not in self.junctions:
            for existing in self.junctions:
                if junction.nearest_neighbour_coord == existing.coord_name:
                    self.junctions.append(junction)
                    break
                return False
        return True
    def get_num_junctions(self):
        return len(self.junctions)


class junction(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.coord_name = f"{x},{y},{z}"
        self.nearest_neighbour_object = None
        self.shortest_distance = 9999999999999999999999
        self.nearest_neighbour_coord = None

    def __str__(self):
        return f"{self.coord_name}"

    def calc_distance(self, other_junction):
        distance = math.sqrt((self.x - other_junction.x)**2 +
                             (self.y-other_junction.y)**2 +
                             (self.z-other_junction.z)**2)
        if distance < self.shortest_distance:
            self.shortest_distance = distance
            self.nearest_neighbour_object = other_junction
            self.nearest_neighbour_coord = f"{other_junction.x},{other_junction.y},{other_junction.z}"
        return distance

def read_file(filename):
    junctions = []
    with open(filename, 'r') as f:
        for line in f:
            x, y, z = [int(x) for x in line.strip().split(",")]
            new_junction = junction(x,y,z)
            if not junctions:
                junctions.append(new_junction)
            else:
                junctions = calc_nearest_neighbour(new_junction, junctions)
    junctions.sort(key=lambda junction: junction.shortest_distance)
    circuits = []
    for node in junctions:
        print(node)
        if not circuits:
            circuits.append(circuit(node))
        else:
            for group in circuits:
                if group.add_junction(node):
                    break
                else:
                    circuits.append(circuit(node))

    return circuits

def calc_nearest_neighbour(new_junction, junctions):
    for junction in junctions:
        new_junction.calc_distance(junction)
        junction.calc_distance(new_junction)
    junctions.append(new_junction)
    return junctions

if __name__ == "__main__":
    circuits = read_file("tests/day8.txt")
    print(len(circuits))
    '''
    for circuit in circuits:
        for junction in circuit.junctions:
            print(f"{junction.shortest_distance} - "
                  f"Node {junction.x},{junction.y},{junction.z} to "
                  f"{junction.nearest_neighbour_coord}")
    '''