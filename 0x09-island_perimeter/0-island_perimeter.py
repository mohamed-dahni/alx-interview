def island_perimeter(grid):
    perimeter = 0
    
    for ri, row in enumerate(grid):
        for ci, column in enumerate(row):
            if column:
                # check top part
                if ri == 0 or grid[ri - 1][ci] == 0:
                    perimeter = perimeter + 1
                # check left part
                if ci == 0 or grid[ri][ci - 1] == 0:
                    perimeter = perimeter + 1
                # check right part
                if ci == ri + 1 or grid[ri][ci + 1] == 0:
                    perimeter = perimeter + 1
                # check bottom part
                if ri == len(grid) - 1 or grid[ri + 1][ci] == 0:
                    perimeter = perimeter + 1
    
    return perimeter

