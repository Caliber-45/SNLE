class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end

    def _walk_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    def starts_with(self, prefix):
        return self._walk_prefix(prefix) is not None

    def autocomplete(self, prefix):
        start_node = self._walk_prefix(prefix)
        if start_node is None:
            return []

        matches = []

        def collect(node, built):
            if node.is_end:
                matches.append(built)
            for char in sorted(node.children.keys()):
                collect(node.children[char], built + char)

        collect(start_node, prefix)
        return matches
