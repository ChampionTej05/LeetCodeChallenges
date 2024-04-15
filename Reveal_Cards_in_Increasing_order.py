'''

https://leetcode.com/problems/reveal-cards-in-increasing-order/description/?envType=daily-question&envId=2024-04-08

Simulate the process with a queue.

Sort the deck, it is actually the "final sequence" we want to get according to the question.
Then put it back to the result array, we just need to deal with the index now!
Simulate the process with a queue (initialized with 0,1,2...(n-1)), now how do we pick the card?
We first pick the index at the top: res[q.poll()]=deck[i]
Then we put the next index to the bottom: q.add(q.poll());
Repeat it n times, and you will have the result array!


Let's walk through the example:
Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]

Sort the deck: [2,3,5,7,11,13,17], this is the increasing order we want to generate
Initialize the queue: [0,1,2,3,4,5,6], this is the index of the result array
The first card we pick is res[0], observe the deck, it should be deck[0]==2, so assign res[0]=2
Then we put res[1] to the bottom, so we re-insert 1 to the queue
The second card we pick is res[2], which should be deck[1]==3, so assign res[2]=3
Then we re-insert 3 to the queue
Each time we assign 1 value to the res, so we repeat this n times
'''


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        
        from collections import deque
        
        deck.sort()
        
        result = deck[::]
        
        queue = deque([i for i in range(len(deck))])
        
        for i in range(len(deck)):
            print("--------------")
            print("i, ", i)
            print("Queue: ", queue)
            print("Result", result)
            index = queue.popleft()
            result[index] = deck[i]
            if queue:
                next_index = queue.popleft()
                queue.append(next_index)
                
                print("Queue: ", queue)
                print("Result", result)
                # print("Deck", deck)
                print("--------------")

        return result 
        
        
deck = [17,13,11,2,3,5,7]

deck = [90,3,1,4,6,89,45,61,23,68,98]

obj = Solution()

print(obj.deckRevealedIncreasing(deck))
        
        