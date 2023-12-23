class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Initialize the starting point at the origin (0, 0)
        x, y = 0, 0
        # Set to keep track of all visited coordinates, starting with the origin
        visited = {(x, y)}

        # Define moves for each direction
        moves = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        # Iterate through each character in the path string
        for move in path:
            # Move in the direction specified by the current character
            dx, dy = moves[move]
            x, y = x + dx, y + dy

            # Check if the new position has already been visited
            if (x, y) in visited:
                return True  # The path crosses itself

            # Mark the new position as visited
            visited.add((x, y))

        # If no crossing was found, return False
        return False
