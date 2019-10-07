class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        visited_list = []
        stack = [(beginWord,1)]
        visited_list.append(beginWord)

        while stack:
            word, count = stack.pop(0)
            if word == endWord:
                return count


            else:
                for i in range(len(word)):
                    for j in range(0,26):
                        char = ord("a")+j
                        new_word = word[0:i] + chr(char) + word[i+1:]
                        if new_word not in visited_list and new_word in wordList:
                            stack.append((new_word,count+1))
                            visited_list.append(new_word)

        return 0



        
