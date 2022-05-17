from ast import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b=board

        r=defaultdict(list)
        c=defaultdict(list)
        square=defaultdict(list)

        for i in range (9):
          for j in range(9):
            if b[i][j]=='.':
              continue
            elif (b[i][j] in r[i] or b[i][j] in c[j] or b[i][j] in square[(i//3,j//3)]):
              return False

            r[i].append(b[i][j])
            c[j].append(b[i][j])
            square[(i//3,j//3)].append(b[i][j])

        return True