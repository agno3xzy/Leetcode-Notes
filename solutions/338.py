from typing import List


class Solution:

    def countBits(self, num: int) -> List[int]:
        ans = []
        def singleBits(nums):
            ans = 0
            if nums == 1:
                return 1
            div = nums // 2
            while div != 0:
                mod = nums % 2
                if mod == 1:
                    ans+=1
                mod = 0
                nums = div
                div = nums // 2
                if nums == 1:
                    ans+=1
            return ans
        for i in range(num+1):
            ans.append(singleBits(i))
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(7))

'''
Java Solution

class Solution {
    public int[] countBits(int num) {
        int[] ans = new int[num+1];
        ans[0] = 0;
        for (int i = 0; i <= num; i++) {
            if(i%2==0){
                ans[i] = ans[i/2];
            }
            else{
                ans[i] = ans[i-1]+1;
            }
        }
        return ans;
    }
}
'''