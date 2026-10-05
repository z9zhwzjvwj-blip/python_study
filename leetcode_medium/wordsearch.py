board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "ABCCED"


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    rows = len(board)
    cols = len(board[0])

    # Track Visited Node
    visited = [[False] * cols for _ in range(rows)]

    # dfs function to visit every row and column
    def dfs(r, c, i):
        # True if word was found
        if i == len(word):
            return True

        # False if row and column out of index
        if r < 0 or r >= rows or c < 0 or c >= rows:
            return False

        # False if node visited before
        if visited[r][c]:
            return False

        # False if the node doesn't match with the target word
        if board[r][c] != word[i]:
            return False

        # check visited
        visited[r][c] = True

        # find the next alphabet in the adjacent nodes
        found = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )

        # recover visited once dfs has been done
        visited[r][c] = False

        return found

    # perform dfs for every node
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False


print(exist(board1, word1))
