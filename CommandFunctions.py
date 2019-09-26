import re
import math
import sys
import itertools


flag = True
vertex_points = []
vertex_inter_points = []
flag = True
edges_points_temp = []
edges_indexes=[]


class GraphPoints:
    def __init__(self, obj1, obj2, obj3,  obj4):
        self.line_one_point_one = obj1
        self.line_one_point_two = obj2
        self.line_two_point_one = obj3
        self.line_two_point_two = obj4

    def __repr__(self):
        return self


def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def command_a_function(street_points):
    streets_and_points = []
    # print("Input to command_a_function"+street_points)
    street = re.compile(r'"([^"^[0-9]*)"')
    points = re.compile(r'(\(-?[0-9]+,-?[0-9]+\))\s*')
    street_name_temp = street.findall(street_points)
    street_name=str(street_name_temp).lower()
    # print(type(street_name))
    if len(street_name) == 0:
        print >> sys.stderr, "Error: Enter Street name along with points - command_a_function"
    points_name = points.findall(street_points)
    if len(points_name) < 2:
        print >> sys.stderr, "Error: Enter at least 2 points for each Street - command_a_function"
    else:
        pass
        # print("Extracted points from command_a_function")
        # print(points_name)

    streets_and_points.append(street_name)
    streets_and_points.append(points_name)
    return streets_and_points


def command_c_function(street_points,streets_and_points_temp):
    # print(streets_and_points_temp)
    street = re.compile(r'"([^"^[0-9]*)"')
    street_name_temp = street.findall(street_points)
    street_name = str(street_name_temp).lower()
    # print(type(street_name))
    points = re.compile(r'(\([0-9]+,[0-9]+\))\s*')
    points_name = points.findall(street_points)
    if len(points_name) < 2:
        print >> sys.stderr, "Error: Enter at least 2 points for each Street - command_c_function"
    if len(streets_and_points_temp) == 0:
        print >> sys.stderr, "Error: First enter the street info and then try to change it"
    for sp in streets_and_points_temp:
        if sp.st_name == street_name:
            sp.points = points_name
            flag=False
    # print(streets_and_points_temp)
    if flag:
        print >> sys.stderr, "Error:No such street name to change the info"
    flag=True
    return streets_and_points_temp


def command_r_function(street_points,streets_and_points_temp):
    # print("Called remove function")
    # print(streets_and_points_temp)
    street = re.compile(r'"([^"^[0-9]*)"')
    street_name_temp = street.findall(street_points)
    street_name = str(street_name_temp).lower()
    # print(type(street_name))
    if len(streets_and_points_temp) == 0:
        print >> sys.stderr, "Error: First enter the street info and then try to change it"
    for sp in streets_and_points_temp:
        if sp.st_name == street_name:
            streets_and_points_temp.remove(sp)
            break
    return streets_and_points_temp


def command_g_function(streets_and_points):
    global vertex_inter_points
    vertex_inter_points = []
    global edges_points_temp
    edges_points_temp = []
    global edges_indexes
    edges_indexes = []
    global vertex_points
    vertex_points = []
    streets_length=range(len(streets_and_points)-1)
    # print(streets_length)
    for sp in streets_length:
        calculate_intersection_points(streets_and_points[sp], streets_and_points[sp+1])
    # print("V = {")
    print_vertices_function(vertex_points)
    # length = range(len(vertex_points))
    # for i in length:
    #     print('{0}: {1}'.format(i+1, vertex_points[i]))
    # print("}")
    finding_edges(vertex_inter_points,vertex_points,streets_and_points)


def calculate_intersection_points(sp_obj_one, sp_obj_two):
    # print("2")
    # print(sp_obj_one)
    # print(sp_obj_two)
    # sp_one_points=create_points_list(sp_obj_one)
    # sp_two_points = create_points_list(sp_obj_two)
    # print("objects sent")
    number_of_points_one = range(len(sp_obj_one.points)-1)
    number_of_points_two = range(len(sp_obj_two.points)-1)
    for i in (number_of_points_one):
        for j in (number_of_points_two):
            # print(sp_obj_one.points[i], sp_obj_one.points[i + 1])
            # print(sp_obj_two.points[j], sp_obj_two.points[j + 1])
            intersection_points(GraphPoints(sp_obj_one.points[i], sp_obj_one.points[i+1],
                                            sp_obj_two.points[j], sp_obj_two.points[j+1]))


def intersection_points(graphpoints_temp):
    # print("graph function")
    # print(GraphPoints_temp.line_one_point_one[1])
    # print(GraphPoints_temp.line_one_point_one[3])
    # print(GraphPoints_temp.line_one_point_two[1])
    # print(GraphPoints_temp.line_one_point_two[3])
    # print(GraphPoints_temp.line_two_point_one[1])
    # print(GraphPoints_temp.line_two_point_one[3])
    # print(GraphPoints_temp.line_two_point_two[1])
    # print(GraphPoints_temp.line_two_point_two[3])
    temp = graphpoints_temp.line_one_point_one.replace('(', '')
    temp = temp.replace(')', '')
    temp = temp.split(',')
    x1 = float(temp[0])
    y1 = float(temp[1])
    temp = graphpoints_temp.line_one_point_two.replace('(', '')
    temp = temp.replace(')', '')
    temp = temp.split(',')
    x2 = float(temp[0])
    y2 = float(temp[1])
    temp = graphpoints_temp.line_two_point_one.replace('(', '')
    temp = temp.replace(')', '')
    temp = temp.split(',')
    x3 = float(temp[0])
    y3 = float(temp[1])
    temp = graphpoints_temp.line_two_point_two.replace('(', '')
    temp = temp.replace(')', '')
    temp = temp.split(',')
    x4 = float(temp[0])
    y4 = float(temp[1])
    global vertex_points
    global vertex_inter_points
    try:
        a = (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)
        b = (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)
        c = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if calculate_distance(x1, y1, x2, y2) >= calculate_distance(x1, y1, float(a/c), float(b/c)):
            if (a / c, b / c) not in vertex_points:
                vertex_points.append((a / c, b / c))
                vertex_inter_points.append((a / c, b / c))
            if (x1, y1) not in vertex_points:
                vertex_points.append((x1, y1))
            if (x2, y2) not in vertex_points:
                vertex_points.append((x2, y2))
            if (x3, y3) not in vertex_points:
                vertex_points.append((x3, y3))
            if (x4, y4) not in vertex_points:
                vertex_points.append((x4, y4))
    except ZeroDivisionError:
        # print("Exception occurred")
        return None


def finding_edges(vertex_inter_points_temp,vertex_points_temp,streets_and_points):
    # print("reached edges calculation function")
    global flag
    global edges_points_temp
    # print("vertex_inter_points_temp in edges function ")
    # print(vertex_inter_points_temp)
    # print("vertex_points_temp All in edges function")
    # print(vertex_points_temp)
    # print("streets_and_points All in edges function")
    # print(streets_and_points)
    type_of_fun = "finding edges"
    for intersection in vertex_inter_points_temp:
        for vertex in vertex_points_temp:
            if intersection != vertex:
                for ck in vertex_points_temp:
                    if ck not in vertex_inter_points_temp :
                        if ck != vertex:
                            if not is_point_between(intersection, vertex, ck,type_of_fun):
                                if (vertex_points_temp.index(intersection)+1, vertex_points_temp.index(vertex)+1) not in edges_points_temp :
                                    edges_points_temp.append((vertex_points_temp.index(intersection) + 1, vertex_points_temp.index(vertex) + 1))
    # print("printing edges temp initial")
    # print(edges_points_temp)
    points_on_same_street(streets_and_points, edges_points_temp, vertex_points_temp)


def points_on_same_street(streets_and_points_temp, edges_points_all, vertex_points_temp):
    # print("reached function finding - edges pairs on same street function")
    # print("streets_and_points_temp in - edges pairs on same street ")
    # print(streets_and_points_temp)
    # print("edges_points_all in - edges pairs on same street ")
    # print(edges_points_all)
    # print("vertex_points_temp in - edges pairs on same street")
    # print(vertex_points_temp)
    flagone=False
    flagtwo=False
    flagthree=True
    global edges_indexes
    # print("printing final in - edges pairs on same street- should be empty")
    # print(edges_indexes)
    for ckp in edges_points_all:
        for stp in streets_and_points_temp:
            # print("edge index pair in LOOP 1 - edges pairs on same street")
            # print(ckp)
            # print("Street Selected to check for edge index pair in LOOP 1 - edges pairs on same street")
            # print(stp)
            if vertex_points_temp[ckp[0]-1] in stp.points:
                # print("MAKING FLAG ONE TRUE as directly in street points - edges pairs on same street")
                flagone=True
            elif check_street(stp.points,vertex_points_temp[ckp[0]-1]):
                # print("MAKING FLAG ONE TRUE by same street  - edges pairs on same street")
                flagone = True
            if vertex_points_temp[ckp[1]-1] in stp.points:
                # print("as returned true")
                # print("MAKING FLAG two TRUE as directly in street points - edges pairs on same street")
                flagtwo = True
            elif check_street(stp.points, vertex_points_temp[ckp[1]-1]):
                # print("as returned true")
                # print("MAKING FLAG two TRUE by same street  - edges pairs on same street")
                flagtwo = True
            if check_vertex_between(vertex_points_temp[ckp[0]-1],vertex_points_temp[ckp[1]-1],vertex_points_temp,stp):
                flagthree =False
            if flagone == True and flagtwo == True and flagthree == True:
                edges_indexes.append(ckp)
                # print("printing edges inside loop")
                # print(edges_indexes)
                # print("Breaking the loop as both points are on same street")
                break
            flagthree = True
            flagone = False
            flagtwo = False
        # print("printing flag one and flag two - edges pairs on same street")
        # print(flagone)
        # print(flagtwo)
        # print(flagthree)
        # print("checking the edge index pair going to be appended to final edges ")
        # print(ckp)
        # if flagone == True and flagtwo == True and flagthree == True:
        #     print("both flags are true- so appending the pair to final edges -- both flags are true- so appending the pair to final edges -- both flags are true- so appending the pair to final edges")
        #
    # print("printing edges after  - edges pairs on same street function")
    print_edges_function(edges_indexes)


def check_street(stp_points, point_check):
    # print("Reached checking whether a points on lies in the selected street - check_street function")
    # print("stp_points - printing all points of selected street - check_street function")
    # print(stp_points)
    # print("point_check - point to check whether it iles on the above points street  - check_street function")
    # print(point_check)
    type_of_func = "is point between"
    for first, second in itertools.izip(stp_points[:-1], stp_points[1:]):
        if not isinstance(first,int) and not isinstance(second,int):
            # print("pair of points between which the point_check has to lie - check_street function ")
            # print(first,second)
            # print("point which has to be checked to lie b/w above points -check_street function ")
            if is_point_between(first, second, point_check, type_of_func):
                # print("true below point is in the below street")
                # print(point_check)
                # print(stp_points)
                # print("return true")
                return True
    return False


def is_point_between(intersection, vertex, checkpoint,type_of_function):
    if type_of_function == "is point between":
        # print("Reached is_point_between function ")
        points_temp_one = re.compile(r'(-?[0-9]+)\s*')
        points_one = points_temp_one.findall(intersection)
        # print("type of points_two")
        # print(type(points_one))
        # print(points_one[0],points_one[1])
        points_two = points_temp_one.findall(vertex)
        # print("type of points_two")
        # print(type(points_two))
        # print(points_two[0],points_two[1])
        # print(checkpoint[0],checkpoint[1])
        if (float(checkpoint[0]) == float(points_one[0]) and float(checkpoint[1]) == float(points_one[1])) or (float(
                checkpoint[0]) == float(points_two[0]) and float(checkpoint[1]) == float(points_two[1])):
            # print("returning true from is_point_between function - condition 1")
            return True
        elif float(checkpoint[0]) == float(points_one[0]) == float(points_two[0]) :
            if ((float(points_one[1]) < float(checkpoint[1])<float(points_two[1])) or float(points_one[1]) > float(checkpoint[1]) > float(points_two[1])):
                # print("returning true from is_point_between function - condition 1")
                return True
            else:
                # print("returning False from is_point_between function - condition 1")
                return False
        elif float(checkpoint[1]) == float(points_one[1]) == float(points_two[1]):
            if ((float(points_one[0]) < float(checkpoint[0])<float(points_two[0])) or float(points_one[0]) > float(checkpoint[0]) > float(points_two[0])):
                # print("returning true from is_point_between function - condition 2")
                return True
            else:
                # print("returning False from is_point_between function - condition 2")
                return False
        elif (float(points_one[1]) == float(points_two[1]) != float(checkpoint[1])) or (float(points_one[0]) == float(points_two[0]) != float(checkpoint[0])) :
            # print("returning False from is_point_between function - condition 3")
            return False

        elif int(0) <= (float(checkpoint[0])-float(points_one[0]))/(float(points_two[0])-float(points_one[0])) <= int(1) and int(0) <= (float(checkpoint[1])-float(points_one[1]))/(float(points_two[1])-float(points_one[1])) <=int(1) :
            if (float(checkpoint[0])-float(points_one[0]))/(float(points_two[0])-float(points_one[0])) == (float(checkpoint[1])-float(points_one[1]))/(float(points_two[1])-float(points_one[1])) :
                # print("returning true from is_point_between function - condition 4")
                return True
            else:
                # print("returning False from is_point_between function - condition 4")
                return False

        else:
            # print("returning false from is_point_between function - condition 4")
            return False
    elif type_of_function == "finding edges":
        return calculate_distance(float(intersection[0]), float(intersection[1]), float(vertex[0]), float(vertex[1])) == \
               calculate_distance(float(intersection[0]), float(intersection[1]), float(checkpoint[0]), float(checkpoint[1]))+calculate_distance(float(vertex[0]), float(vertex[1]), float(checkpoint[0]), float(checkpoint[1]))
    elif type_of_function == "vertex_between_edges" :
        # print("Reached vertex_between_edges function ")
        # points_temp_one = re.compile(r'(-?[0-9]+)\s*')
        points_one_t = intersection
        points_two_t = vertex
        # points_one_t = points_temp_one.findall(intersection)
        # print("points_one")
        # print(type(points_one_t))
        # print(points_one_t[0], points_one_t[1])
        # points_two_t = points_temp_one.findall(vertex)
        # print("type of points_two")
        # print(type(points_two_t))
        # print(points_two_t[0], points_two_t[1])
        # checkpoint_temp=points_temp_one.findall(checkpoint)
        # print(type(checkpoint_temp))
        # print(checkpoint[0], checkpoint[1])
        if float(checkpoint[0]) == float(points_one_t[0]) == float(points_two_t[0]) :
            if ((float(points_one_t[1]) < float(checkpoint[1])<float(points_two_t[1])) or float(points_one_t[1]) > float(checkpoint[1]) > float(points_two_t[1])):
                # print("returning true from is_point_between function - condition 1")
                return True
            else:
                # print("returning False from is_point_between function - condition 1")
                return False
        elif float(checkpoint[1]) == float(points_one_t[1]) == float(points_two_t[1]):
            if ((float(points_one_t[0]) < float(checkpoint[0])<float(points_two_t[0])) or float(points_one_t[0]) > float(checkpoint[0]) > float(points_two_t[0])):
                # print("returning true from is_point_between function - condition 2")
                return True
            else:
                # print("returning False from is_point_between function - condition 2")
                return False
        elif (float(points_one_t[1]) == float(points_two_t[1]) != float(checkpoint[1])) or (float(points_one_t[0]) == float(points_two_t[0]) != float(checkpoint[0])) :
            # print("returning False from is_point_between function - condition 3")
            return False

        elif int(0) <= (float(checkpoint[0])-float(points_one_t[0]))/(float(points_two_t[0])-float(points_one_t[0])) <= int(1) and int(0) <= (float(checkpoint[1])-float(points_one_t[1]))/(float(points_two_t[1])-float(points_one_t[1])) <=int(1) :
            if (float(checkpoint[0])-float(points_one_t[0]))/(float(points_two_t[0])-float(points_one_t[0])) == (float(checkpoint[1])-float(points_one_t[1]))/(float(points_two_t[1])-float(points_one_t[1])) :
                # print("returning true from is_point_between function - condition 4")
                return True
            else:
                # print("returning False from is_point_between function - condition 4")
                return False

        else:
            # print("returning false from is_point_between function - condition 4")
            return False


def check_vertex_between(intersection_point,point_two,vertex_points,stp):
    is_between=False
    is_endpoint = True
    # print("check_vertex_between")
    # print(type(intersection_point),type(point_two),type(vertex_points))
    for vert in vertex_points:
        if intersection_point != vert and point_two != vert and is_point_between(intersection_point, point_two, vert,"vertex_between_edges"):
            is_between = True
    for point in stp.points:
        points_temp_one_here = re.compile(r'(-?[0-9]+)\s*')
        points_here = points_temp_one_here.findall(point)
        # print("type of point")
        # print(points_here)
        # print(stp)
        # print("points send to check whether its an edge")
        # print(point_two, points_here, intersection_point)
        if is_point_between(point_two, points_here, intersection_point,"vertex_between_edges") :
            # print(point_two,points_here,intersection_point)
            # print("yes the above point is an end point of intersation line")
            is_endpoint = False
            break
    # print(is_between,is_between,is_between or is_endpoint)
    return is_between or is_endpoint


def print_vertices_function(vertex_points_temp):
    # print(type(vertex_points_temp))
    # print(type(vertex_points_temp[0]))
    length = range(len(vertex_points_temp))
    print("V = {")
    for i in length:
        # print(type(vertex_points_temp[i]))
        print('{0}: ({1:.2f},{2:.2f})'.format(i + 1, vertex_points_temp[i][0],vertex_points_temp[i][1]))
    print("}")


def print_edges_function(edges_indexes):
    # print(type(edges_indexes))
    # print(type(edges_indexes[0]))
    # for tu in edges_indexes:
    #     if (tu[1],tu[0]) in edges_indexes:
    #         return edges_indexes.remove((tu[1], tu[0]))
    for tu in edges_indexes:
        if tuple_reverse(tu) in edges_indexes:
            edges_indexes.remove(tuple_reverse(tu))
    print("E = {")
    for tup in edges_indexes:
        print("<{0},{1}>".format(tup[0],tup[1]))
    # print(edges_indexes)
    print("}")


def tuple_reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


