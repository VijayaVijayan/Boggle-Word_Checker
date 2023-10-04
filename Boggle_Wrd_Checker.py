def find_word(board, word):
    def search(i, j, k):
        if k == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        
        temp, board[i][j] = board[i][j], None
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for x, y in directions:
            if search(i + x, j + y, k + 1):
                board[i][j] = temp  
                return True
        
        
        board[i][j] = temp
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if search(i, j, 0):
                return True

    return False