class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        my_dict = {"b":0,"a":0,"l":0,"o":0, "n":0}
        for key in text:
            if key in my_dict:
                my_dict[key] = my_dict.get(key, 0) + 1

        return min(my_dict['b'], my_dict['a'], my_dict['l'] // 2, my_dict['o'] // 2, my_dict['n'])

        