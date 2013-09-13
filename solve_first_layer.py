from cube import Cube

cube = Cube()

def solve_first_layer():
    crosses = [ 'white:green', 'white:red', 'white:yellow', 'white:orange' ]
    correct_locations = {
        'white:green'  : 'top:left',
        'white:red'    : 'top:right',
        'white:yellow' : 'top:front',
        'white:orange' : 'top:back'
    }

    while not cross_solved(cube):
        cross = find_next_cross(crosses.pop)
        cross_location = find_correct_location_for_cross(cross)
        do_first_layer(cross, cross_location)

def do_first_layer(source_location, target_location):
    # rotate the cube so that the piece faces you first (on the front/bottom face)
    # rotate the front to be in top 2 (arbitrary position chosen)

    # TODO: fix up
    {
        'top:left'  : solve_top_left,
        'top:right' : solve_top_left,
        'top:front' : solve_top_left,
        'top:back'  : solve_top_left
    }[source_location]()
    # rotate it back

def cross_solved():
    return [cube.top.find_location(loc).top_face == 'white' for loc in [2,4,6,8]]

def solve_front_2():
    cube.front.rotate('R')
    solve_front_6()

def solve_front_4():
    cube.front.rotate('R')
    solve_front_2()

def solve_front_6():
    cube.right.rotate('R')

def solve_front_8():
    cube.front.rotate('L')
    solve_front_6()

def solve_bottom_2():
    cube.front.rotate('R')
    solve_bottom_6()

def solve_bottom_4():
    cube.front.rotate('R')
    solve_bottom_2()
    
def solve_bottom_6():
    cube.right.rotate('R')
    solve_front_6()

def solve_bottom_8():
    cube.front.rotate('L')
    solve_bottom_6()
