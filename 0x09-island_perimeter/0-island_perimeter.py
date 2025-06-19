#!/usr/bin/python3
""" Solution for Islan Perimeter problem"""


def island_perimeter(grid):
    """ uses recursive function with a deep first search technqiue to get
    the perimeter of the island

    Retrun:
    perimeter: (int) perimeter of the island
    """
    visit = set()

    def dfs(i, j):
        """ recursive function ot get the perime
        i: rows of the 2D grid
        j: columns of the 2D grid

        Return:
        value of the perim
        """
        if i >= len(grid) or j >= len(grid[0]) /
        or i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0

        visit.add((i, j))
        perimeter = dfs(i, j + 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
