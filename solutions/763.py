class Solution:
    def solution(self, S):
        last = {c: i for i, c in enumerate(S)}
        print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            print(i,c)
            print("j: " ,j)
            print(ans)
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans

    def partitionLabels(self, s):
        def solve(s):
            appear = {}
            finish = {}
            ans = []
            for index in range(len(s)):
                if not (s[index]) in appear:
                    appear[s[index]] = index
                finish[s[index]] = index
            finish = dict(sorted(finish.items(), key=lambda item: item[1]))
            print(appear)
            print(finish)

            ans.append(get_string(appear, finish))

            while sum(ans) < len(s):
                if len(appear) == 0 or len(finish) == 0:
                    break
                tmp = get_string(appear, finish)
                if tmp != 0:
                    ans.append(tmp)
            return ans

        def get_string(appear, finish):
            tmp_appear = list(appear.items())
            if len(tmp_appear) == 0:
                return 0
            first = tmp_appear[0][0]
            start = tmp_appear[0][1]
            end = finish[first]
            end_or_not = is_end(first, end, appear, finish)
            while  end_or_not != -1 and end_or_not + 1 < len(appear):
                end = finish[tmp_appear[end_or_not][0]]
                tmp_end_or_not = is_end(first, end, appear, finish)
                if tmp_end_or_not == end_or_not:
                    break
                end_or_not = tmp_end_or_not
            if end_or_not + 1 == len(appear) and start == 0:
                path = len(s)
            else:
                path = end - start + 1
            tmp_del = []
            for key, value in appear.items():
                if value > end:
                    break
                else:
                    tmp_del.append(key)

            for key, value in list(finish.items()):
                if key in tmp_del:
                    del finish[key]
            for key, value in list(appear.items()):
                if key in tmp_del:
                    del appear[key]

            return path
        def is_end(first, end , appear, finish):
            tmp_set = []
            index = -1
            for key, value in list(finish.items()):
                if key == first:
                    break
                tmp_set.append(key)
            tmp_set.append(first)
            for key, value in list(appear.items()):
                if key not in tmp_set and value < end:
                    index = list(appear.keys()).index(key)
                if value > end:
                    break
            return index



s = Solution()
print(s.solution("ababcbacadefegdehijhklij"))