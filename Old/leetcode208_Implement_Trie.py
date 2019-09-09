class TrieNode:

    def __init__(self):
    # 建立一个 TrieNode对象，包含从当前位置能达到下个位置的元素信息，用dict来保存
    # 和另外一个属性来表示到目前位置为止是不是一个完整的单词
        self.children = {}
        self.isword = False




    # 最重要的是建立一个TrieNode class包含 node.children and node.isword两个属Å
    # 最重要的是建立一个TrieNode class包含 node.children and node.isword两个属Å
    # 最重要的是建立一个TrieNode class包含 node.children and node.isword两个属Å

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 建立字典树，实际上等于建立一个根节点
        self.root = TrieNode()



    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # 从根节点开始搜索，如果有往下搜索，如果没有建立新的TrieNode,在进入到这个Node中继续往下搜索
        # 将字母每一个单词都输入进去后，把当前为止是单词标记为 True
        node = self.root
        for unit in word:
            if unit in node.children:
                node = node.children[unit]
            else:
                new_node = TrieNode()
                node.children[unit] = new_node
                node = node.children[unit]
        node.isword = True




    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node  = self.root
        for unit in word:
            if unit in node.children:
                node = node.children[unit]

            else:return False

        return node.isword


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for unit in prefix:
            if unit in node.children:
                node = node.children[unit]

            else:
                return False

        return True
