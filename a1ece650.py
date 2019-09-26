import sys
import re
from CommandFunctions import *


class Street:
    def __init__(self,temp):
        self.st_name = temp[0]
        self.points = temp[1]

    def __repr__(self):
        pass
        return "Street name is {0} and associated points are {1}".format(self.st_name, self.points)

    def __getitem__(self, item):
        return self.points


class PointTuples:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '({0:.2f},{1:.2f})'.format(self.x, self.y)


streets_and_points = []


def update_streets_and_points(streets_and_points_temp):
    try :
        streets_and_points = streets_and_points_temp
    except :
        print >> sys.stderr, "Error: Make Sure inputs are valid"


def input_command_check(points_in_temp):
    try :
        point_releft = re.compile(r'\(')
        point_reright = re.compile(r'\)')
        points_in = points_in_temp.strip()
        if points_in[0] in ('a', 'c'):
            if len(points_in) > 2:
                if points_in[1] == ' ':
                    if len(point_releft.findall(points_in)) == len(point_reright.findall(points_in)) and len(
                            point_releft.findall(points_in)) != 0 and len(point_reright.findall(points_in)) != 0:
                        if len(re.findall(r'"\s+\(', points_in)) > 0:
                            return True
                        else:
                            print >> sys.stderr, 'Error:Points/space is missing after street name'
                            return False
                    else:
                        print >> sys.stderr, 'Error: Brackets are missing for Points  after street name'
                        return False
                else:
                    print >> sys.stderr, 'Error:Space is missing after command Character'
                    # print("Error:Space is missing after command Character")
                    return False
            else:
                print >> sys.stderr, "Error:The remaining part of Command is missing"
                # print("Error:The remaining part of Command is missing")
                return False
        elif points_in[0] == 'r':
            point_releft = re.compile(r'\(')
            point_reright = re.compile(r'\)')
            point_quotes = re.compile(r'\"')
            if len(points_in) > 2:
                if points_in[1] == ' ':
                    if len(point_releft.findall(points_in)) == 0 and len(point_reright.findall(points_in)) == 0 and len(
                            point_quotes.findall(points_in)) == 2:
                        return True
                    else:
                        print >> sys.stderr, "Error: There should not be any \( or \) and there should be street name in Quotes"
                        # print("Error: There should not be any \( or \) and there should be street name in Quotes")
                        return False
                else:
                    print >> sys.stderr, "Error: Separate Street name from command using Space"
                    return False
            else:
                print >> sys.stderr, "Error:Enter Street name after command"
                return False
        elif points_in[0] == 'g':
            if points_in.rstrip() == 'g':
                return True
            else:
                print >> sys.stderr, "Error: For graph command 'g' there should not be any other inputs"
                return False
        else:
            print >> sys.stderr, "Error: Input command must be either 'a' or 'r' or 'c' with a space after command followed by street name"
            return False
    except :
        print >> sys.stderr, "Error: Make Sure inputs are valid"



def input_command_split(input_cmd_temp):
    try :
        input_cmd = []
        input_cmd_temp = input_cmd_temp.strip()
        input_cmd = input_cmd_temp.split(' ', 1)
        flag_street=True
        if input_cmd[0] == 'a':
            if len(input_cmd_temp.split()) > 2:
                temp_streets_and_points = command_a_function(input_cmd[1])
                if len(temp_streets_and_points) == 0:
                    print >> sys.stderr, "Error: Enter points properly"
                    return None
                for sap in streets_and_points:
                    if sap.st_name == temp_streets_and_points[0]:
                        flag_street = False
                if flag_street:
                    streets_and_points.append(Street(temp_streets_and_points))
                else:
                    print >> sys.stderr, "Error: Street already exists"
                flag_street=True
            else:
                print >> sys.stderr, "Error:Separate street name from command and points using spaces or enter the missed points"
                return None
        elif input_cmd[0] == 'c':
            update_streets_and_points(command_c_function(input_cmd[1], streets_and_points))
        elif input_cmd[0] == 'r':
            update_streets_and_points(command_r_function(input_cmd[1], streets_and_points))
        else:
            print >> sys.stderr, "Error:There is somme error in the input.Please check the documentation for more details"
            return None
    except :
        print >> sys.stderr, "Error: Make Sure inputs are valid"


def main():
    while True:
        try:
            input_command = sys.stdin.readline()
            if input_command == '':
                break
            if input_command_check(input_command):
                if input_command[0] == 'g':
                    command_g_function(streets_and_points)
                else:
                    input_command_split(input_command)
        except:
            print >> sys.stderr, 'Error: Please make sure inputs are Correct'
    print 'Finished reading input'
    sys.exit(0)
     


if __name__ == '__main__':
    main()

