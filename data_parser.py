#import pprint
#pp = pprint.PrettyPrinter(indent=2)

################################################################################
# data.csv parser (Flight Data)
################################################################################

def parse_flight_data():
    parsed = {}

    csvfile = open("data2.csv", "r")
    csvdata = csvfile.readlines()

    xy_map = {} # Map number to unique x,y coordinates (nodes)

    # Parse data set
    j = 0
    for i in range(len(csvdata)):
        if i is 0: # at header
            pass
        else: 
            line = csvdata[i]
            line = line.split(",")
            line = {
                "DepLat": line[0],
                "DepLon": line[1],
                "ArrLat": line[2],
                "ArrLon": line[3]
            }

            key = str(line["DepLat"] + "," + line["DepLon"])
            val = str(line["ArrLat"] + "," + line["ArrLon"])

            # Add departure node if doesn't exist
            if key not in parsed:
                parsed[key] = [val]
                xy_map[j] = key
                j += 1
            # Else append arrival node as visited to departure node
            else:
                parsed[key].append(val)

            # Add arrival node if doesn't exist
            if val not in parsed:
                parsed[val] = []
                xy_map[j] = val
                j += 1

    # Inverse of xy_map - map unique x,y coordinates back to numbers
    inverse_xy_map = {v: k for k, v in xy_map.iteritems()}

    # Nodes
    nodes = {}
    for node in xy_map:
        coordinates = xy_map[node]
        coordinates = coordinates.split(",")
        x = coordinates[1]
        y = coordinates[0]

        nodes[str(node)] = {"x": float(x) * 8, "y": float(y) * 8}

    # Edges
    edges = []
    for node in parsed:
        for dest in parsed[node]:
            edges.append({"source": inverse_xy_map[node], "target": inverse_xy_map[dest]})

    return {
        "node_data": nodes,
        "edge_data": edges
    }

################################################################################
# Public functions
################################################################################

def parse(name):
    if name == "flight":
        return parse_flight_data()
    else:
        return None
