import collections
#先定义字典树的每一层的结点
#用dict实现是因为，每一层的字母需要映射下一层的结点
class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()    #root是dummy node, 不存储任何值

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for s in word:
            current_node = current_node.children[s] #若存在会返回dict的映射，若不存在会自动生成下一层的dict
        current_node.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for s in word:
            current_node = current_node.children.get(s, None)
            if current_node is None:
                return False
        return current_node.is_word 

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for s in prefix:
            current_node = current_node.children.get(s, None)
            if current_node is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)