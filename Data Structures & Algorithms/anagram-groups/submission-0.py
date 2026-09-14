class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # possible chars =[a, b, c .. z]
        # for an anagram, order is not important
        # hash map count of chars -> value 

        char_hashmap = {
            # hat: [hat]
            # act: [act, cat]
            # stop: [stop, pots, tops]
        }


        for word in strs:
            sorted_word = "".join(str(sorted(word)))
            char_hashmap[sorted_word] = []

        
        for w in strs:
            sorted_w = "".join(str(sorted(w)))
            if sorted_w in char_hashmap:
                char_hashmap[sorted_w].append(w)
            

        return list(char_hashmap.values())

        

