from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS, start from the endWord
        if not beginWord or not endWord or not wordList:
            return 0

        q = deque()
        unvisited = set(wordList)
        if endWord not in unvisited:
            return 0

        size = 0
        level = 0
        q.append(endWord)

        def offByOne(w1, w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
            return diff

        while q:
            if size == 0:
                level += 1
                size = len(q)

            word = q.popleft()   

            if offByOne(word, beginWord) == 1:
                return level + 1      

            for w in wordList:
                # if visited already, skip
                if w in unvisited:
                    diff = offByOne(w, word)
                    if diff <= 1:
                        q.append(w)
                        unvisited.remove(w)
            size -= 1

        return 0
                