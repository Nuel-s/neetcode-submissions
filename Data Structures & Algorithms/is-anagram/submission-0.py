class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        mappedS = self.mapString(s)
        mappedT = self.mapString(t)
        for char in mappedS:
            if char not in mappedT:
                return False
            if mappedS[char] != mappedT[char]:
                return False
        
        return True

    def mapString(self, s: str):
        charMap = {}
        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1

        return charMap 
        