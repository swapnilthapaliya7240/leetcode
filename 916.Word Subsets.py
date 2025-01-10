class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        for i in words2:
          for w in words1:
            if ( i not in w):
                words1.remove(w)
        return words1
                