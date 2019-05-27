class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        str_dic = {}
        for p in range(len(S)):
            str_dic[p] = S[p]

        for k, v in list(str_dic.items()):
            if v == '(':
                for k1,v2 in list(str_dic.items()):
                    if k1 < k:
                        pass
                    elif v2 == ')':
                        del str_dic[k1]
                        break
            if v == ')':
                for k1, v2 in list(str_dic.items()):
                    if k1 > k:
                        break
                    elif v2 == '(':
                        del str_dic[k1]
                        break
        return len(str_dic)

s = Solution()
print(s.minAddToMakeValid("())"))

'''
Java Solution
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

class Solution {
    public int minAddToMakeValid(String S) {
        ConcurrentHashMap<Integer, Character> str_dic = new ConcurrentHashMap<Integer, Character>();
        for (int i = 0; i < S.length(); i++) {
            str_dic.put(i, S.charAt(i));
        }


        for (ConcurrentHashMap.Entry<Integer, Character> entry : str_dic.entrySet()) {
            if (entry.getValue().equals('(')) {
                for (ConcurrentHashMap.Entry<Integer, Character> entry1 : str_dic.entrySet()) {
                    if (entry1.getKey() > entry.getKey() && entry1.getValue().equals(')')) {
                        str_dic.remove(entry1.getKey());
                        str_dic.remove(entry.getKey());
                        break;
                    }
                }
            } else {
                for (ConcurrentHashMap.Entry<Integer, Character> entry1 : str_dic.entrySet()) {
                    if (entry1.getKey() > entry.getKey()) {
                        break;
                    }
                    if (entry1.getKey() < entry.getKey() && entry1.getValue().equals('(')) {
                        str_dic.remove(entry1.getKey());
                    }
                }
            }
        }
        return str_dic.size();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.minAddToMakeValid("()))(("));
    }
}
'''
