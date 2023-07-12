class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        numRows, numCols, startRow, startCol = len(grid), len(grid[0]), 0, 0
        allKeysPresent, directions = [0, 0, 0, 0, 0, 0], [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == '@':
                    startRow, startCol = row, col
                elif grid[row][col].islower():
                    allKeysPresent[ord(grid[row][col]) - ord('a')] = 1
        currentLevel, allKeysPresent = [(startRow, startCol, tuple(6 * [0]))], tuple(allKeysPresent)
        visited, moves = {(startRow, startCol, tuple(6 * [0]))}, 0
        while currentLevel:
            nextLevel = []
            for row, col, keys in currentLevel:
                for direction in directions:
                    newRow, newCol = row + direction[0], col + direction[1]
                    if 0 <= newRow < numRows and 0 <= newCol < numCols and grid[newRow][newCol] != '#':
                        if grid[newRow][newCol] in '.@':
                            if (newRow, newCol, keys) not in visited:
                                visited.add((newRow, newCol, keys))
                                nextLevel.append((newRow, newCol, keys))
                        elif grid[newRow][newCol].islower():
                            newKeys = list(keys)
                            newKeys[ord(grid[newRow][newCol]) - ord('a')] = 1
                            newKeys = tuple(newKeys)
                            if newKeys == allKeysPresent:
                                return moves + 1
                            if (newRow, newCol, newKeys) not in visited:
                                visited.add((newRow, newCol, newKeys))
                                nextLevel.append((newRow, newCol, newKeys))
                        else:
                            if keys[ord(grid[newRow][newCol].lower()) - ord('a')] == 1 and (newRow, newCol, keys) not in visited:
                                visited.add((newRow, newCol, keys))
                                nextLevel.append((newRow, newCol, keys))
            currentLevel = nextLevel
            moves += 1
        return -1
                
