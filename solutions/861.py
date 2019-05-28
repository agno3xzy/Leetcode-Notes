import math
from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        ans = 0
        for a in A:
            if a[0] != 1 :
                for i in range(len(a)):
                    if a[i] == 1:
                        a[i] = 0
                    else:
                        a[i] = 1
        for i in range(1, len(A[0])):
            zero = 0
            one = 0
            for a in A:
                if a[i] == 1:
                    one += 1
                else:
                    zero += 1
            if one >= zero:
                continue
            if zero > one:
                for b in A:
                    if b[i] != 1:
                        b[i] = 1
                    else:
                        b[i] = 0

        for a in A:
            for i in range(len(a)):
                ans += a[i] * math.pow(2, len(a) - i - 1)
        print(A)
        return int(ans)

s = Solution()
print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
'''
Java Solution
class Solution {
    public int matrixScore(int[][] A) {
        for (int i = 0; i < A.length; i++) {
            if(A[i][0] != 1){
                for (int j = 0; j < A[0].length; j++) {
                    if (A[i][j] != 1) {
                        A[i][j] = 1;
                    }
                    else{
                        A[i][j] = 0;
                    }
                }
            }
        }

        for (int i = 1; i < A[0].length; i++) {
            int zero = 0;
            int one = 0;
            for (int j = 0; j < A.length; j++) {
                if(A[j][i] == 1) one++;
                else zero++;
            }
            if (one >= zero) {
                continue;
            }
            if (zero > one){
                for (int x = 0; x < A.length; x++) {
                    if (A[x][i] == 1) {
                        A[x][i] = 0;
                    }
                    else{
                        A[x][i] = 1;
                    }
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++) {
                ans += A[i][j]*Math.pow(2,A[0].length-j-1);
            }
        }
        return ans;
    }

    public static void main(String[] args) {

    }
}
'''