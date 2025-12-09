import math

class circuit(object):
    def __init__(self,starting_junction):
        self.junctions = [starting_junction]

    def __str__(self):
        string = ""
        for junction in self.junctions:
            string += str(junction) + " --- "
        return f"{string}"

    def add_junction(self, junction):
        if not self.check_junction(junction) and not self.check_junction(junction.nearest_neighbour_object):
            return False
        elif self.check_junction(junction.nearest_neighbour_object):
            self.junctions.append(junction)
            return True
        else:
            return False

    def get_num_junctions(self):
        return len(self.junctions)

    def check_junction(self, junction):
        if junction not in self.junctions:
            return False
        return True


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
        return f"{self.coord_name}, {self.shortest_distance}"

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
    junctions.sort(key=lambda i: i.shortest_distance)

    for x in junctions:
        print(x, x.nearest_neighbour_coord)
    circuits = []
    max_connections = 10
    connections = 0
    for node in junctions:
        if not circuits:
            circuits.append(circuit(node))
        else:
            added = False
            for i, x in enumerate(circuits):
                if x.add_junction(node):
                    added = True
                    connections +=1
                    break
                else:
                    added = False
            if not added:
               circuits.append(circuit(node))
        if connections == max_connections:
            break

    return circuits

def calc_nearest_neighbour(new_junction, junctions):
    distances = []
    for x in junctions:
        val1 = new_junction.calc_distance(x)
        val2 =x.calc_distance(new_junction)
        distances.append(val1)
    junctions.append(new_junction)
    distances.sort()
    print(distances)
    return junctions

if __name__ == "__main__":
    circuits = read_file("tests/day8.txt")
    circuits.sort(key=lambda i: len(i.junctions))
    print(len(circuits[-1].junctions)*len(circuits[-2].junctions)*len(circuits[-3].junctions))

    for x in circuits:
        print(x)
    '''
    for circuit in circuits:
        for junction in circuit.junctions:
            print(f"{junction.shortest_distance} - "
                  f"Node {junction.x},{junction.y},{junction.z} to "
                  f"{junction.nearest_neighbour_coord}")
    '''