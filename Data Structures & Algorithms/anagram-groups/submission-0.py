class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listy = []
        dicty = {}
        i = 0
        for word in strs:
            sortedWord = "".join(sorted(word))
            listy2 = [word]
            if dicty.get(sortedWord) == None:
                dicty[sortedWord] = i
                i += 1
                listy.append(listy2)
            else:
                listy[dicty.get(sortedWord)].append(word)
        return listy

