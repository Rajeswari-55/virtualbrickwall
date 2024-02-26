 def check_is_construction_of_wall_possible_with_bricks(N1, N2, no_of_bricks_available, no_of_units_of_brick):
    is_construction_of_wall_possible_with_available_bricks = False
    no_of_bricks = no_of_bricks_available
    are_bricks_enough = ((no_of_bricks * no_of_units_of_brick) >= N1)
    if are_bricks_enough:
        is_construction_of_wall_possible_with_available_bricks = True
    return is_construction_of_wall_possible_with_available_bricks

    
def get_the_brick(no_of_units_of_brick):
    length = no_of_units_of_brick
    a = no_of_units_of_brick * "*"
    b = "*" + (" " * (length - 2)) + "*"
    brick = (a + "\n" + b + "\n" + a)
    return brick

    
def print_the_wall(N1, N2, no_of_bricks_available, no_of_units_of_brick):
    for row in range(N2):
        for j in range(3):
            if j == 0 or j == 2:
                print(("*" * no_of_units_of_brick) * no_of_bricks_available)
            else:
                print(("*" + (" " * (no_of_units_of_brick - 2)) + "*") * no_of_bricks_available)
           
    print()
    
def main():
    one_unit = 5
    N1 = 6  
    N1 = one_unit * N1
    N2 = 3  
    N3 = 4
    N4 = 8
    N5 = 5
    no_of_units_of_N5 = one_unit
    no_of_units_of_N4 = (one_unit * 2)
    no_of_units_of_N3 = (one_unit * 3)
    type_3_brick = get_the_brick(no_of_units_of_N3)
    type_2_brick = get_the_brick(no_of_units_of_N4)
    type_1_brick = get_the_brick(no_of_units_of_N5)
    print("Type-3 brick")
    print(type_3_brick)
    print()
    print("Type-2 brick")
    print(type_2_brick)
    print()
    print("Type-1 brick")
    print(type_1_brick)
    
    for i in range(3):
        if i == 0:
            print("Type 1 Brick Wall")
            is_construction_of_wall_possible_with_type_1_bricks = check_is_construction_of_wall_possible_with_bricks(N1, N2, N5, no_of_units_of_N5)
            if is_construction_of_wall_possible_with_type_1_bricks:
                print_the_wall(N1, N2, N5, no_of_units_of_N5)
            else:
                print("CAN NOT BE DONE")
                print()
        if i == 1:
            print("Type 2 Brick Wall")
            is_construction_of_wall_possible_with_type_2_bricks = check_is_construction_of_wall_possible_with_bricks(N1, N2, N4, no_of_units_of_N4)
            if is_construction_of_wall_possible_with_type_2_bricks:
                print_the_wall(N1, N2, N4, no_of_units_of_N4)
            else:
                print("CAN NOT BE DONE")
                print()        
        if i == 2:
            print("Type 3 Brick Wall")
            is_construction_of_wall_possible_with_type_3_bricks = check_is_construction_of_wall_possible_with_bricks(N1, N2, N3, no_of_units_of_N3)
            if is_construction_of_wall_possible_with_type_3_bricks:
                print_the_wall(N1, N2, N3, no_of_units_of_N3)
            else:
                print("CAN NOT BE DONE")
                print()

               
main()
