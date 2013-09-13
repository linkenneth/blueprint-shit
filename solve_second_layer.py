from cube import Cube

cube = Cube()

def solve_second_layer():
    # pick random white corner
    # if in the bottom layer (cross layer) bring it up (unless already correct place or "solved")
    # find corresponding edge
    # if connected, break them up (unless already "solved", how to define solve?)
    # rotate to proper face
    # if edge same top color as corner, it's the "bring down and rotate" technique
    # if white on top, "rotate and match up technique"
    # if edge / corner are "criss-cross" different color, use the "rotate and flip in one move" technique
    # repeat until no more white (cross layer) corners left

    corners = cube.search('white:corner'):

    while cube.search('white'):
        pass
