import collections
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        #先排序 在
        index = collections.deque(range(len(deck)))
        ans = [0]*len(deck)
        for n in sorted(deck):
            ans[index.popleft()] = n
            if index:
                index.append(index.popleft())
        return ans

    def bd_solution(self,deck):
        quick_sort = lambda deck: deck if len(deck) <= 1 else quick_sort(
            [item for item in deck[1:] if item <= deck[0]]) + [deck[0]] + quick_sort(
            [item for item in deck[1:] if item > deck[0]])

        deck1 = quick_sort(deck)[0:int(len(deck) / 2 + 1)]
        print(deck1)
        deck2 = quick_sort(deck)[int(len(deck) / 2 + 1):]
        # deck2.reverse()
        print(deck2)
        for i in range(len(deck2)):
            deck[i * 2] = deck1[i]
            if i == 0 or i % 2 == 0:
                deck[int(len(deck) / 2) + i] = deck2[i]
            else:
                deck[int(len(deck) / 2) - i - 1] = deck2[i]
            # deck[i*2+1] = deck2[i]
        return deck

