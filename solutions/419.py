from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        self.ans = 0
        def isShips(board):
            tag = 0
            for s in range(len(board)):
                for i in range(len(board[0])):
                    if board[s][i] == 'X':
                        board[s][i] = tag
                        isVertical = False
                        if i != len(board[0]) - 1 and board[s][i + 1] == 'X':
                            isVertical = True
                            validJ1 = i + 1
                            for j in range(i + 1,len(board[0])):
                                if validJ1 != j :
                                    j = len(board[0])
                                    continue
                                if board[s][j] == 'X':
                                    board[s][j] = tag
                                    validJ1 += 1
                        if s != len(board) - 1 and board[s + 1][i] == 'X':
                            if isVertical == True:
                                return 0
                            validJ = s+1
                            for j in range(s+1, len(board)):
                                if validJ != j:
                                    j = len(board)
                                    continue
                                if board[j][i] == 'X':
                                    board[j][i] = tag
                                    validJ  = j + 1

                        tag+=1
            return tag
        return isShips(board)

s = Solution()
print(s.countBattleships(
[[".","X","X","X","X",".","X",".","X","."],["X",".",".",".",".",".",".",".","X","."],[".","X",".","X",".","X",".",".","X","."],["X",".","X",".","X",".",".",".","X","."],[".","X",".","X",".",".","X",".",".","X"]]
))

'''
class Solution {
    public int countBattleships(char[][] board) {
        int ship = 0;
        if (board.length == 0) {
            return 0;
        }
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j]=='.'){
                    continue;
                }
                if(i> 0 && board[i-1][j] == 'X')continue;
                if (j > 0 && board[i][j-1]=='X')continue; 
                ship++;
            }
        }
        return ship;
    }
}
'''