from typing import List
from collections import defaultdict, deque
import string


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)

        if len(wordSet) == 0 or endWord not in wordSet:
            return []
        res = []
        #图的存储
        G = defaultdict(set)
        if not self.__bfs(beginWord, endWord, G, wordSet):
            return res

        path = [beginWord]
        self.__dfs(beginWord, endWord, G, path, res)
        return res

    def __bfs(self, beginWord, endWord, G, wordSet):
        isFind = False
        q = deque()
        q.append(beginWord)
        #记录已访问的每一层结点信息，防止相同层的结点互相访问
        visited = set()
        visited.add(beginWord)

        next_visit = set()

        while q:
            len_current_que = len(q)
            for i in range(len_current_que):
                current_word = q.popleft()
                tmp_word_list = list(current_word)

                for j in range(len(tmp_word_list)):
                    original_char = tmp_word_list[j]

                    for k in string.ascii_lowercase:
                        tmp_word_list[j] = k
                        next_judge_word = "".join(tmp_word_list)

                        if next_judge_word in wordSet:
                            if next_judge_word not in visited:
                                next_visit.add(next_judge_word)
                                G[current_word].add(next_judge_word)
                                q.append(next_judge_word)
                                #说明当前层已经访问到了endword，建图到当前层即可
                                if next_judge_word == endWord:
                                    isFind = True

                    tmp_word_list[j] = original_char
            if isFind:
                break
            visited |= next_visit
            next_visit.clear
        return isFind

    def __dfs(self, nowWord, endWord, G, path, res):
        if nowWord == endWord:
            res.append(path[:])
            return
        
        next_words = G[nowWord]
        for next_word in next_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, G, path, res)
            path.pop()

    # def __bidirectional_bfs(self, beginWord, endWord, word_set, successors):
    #     visited = set()
    #     visited.add(beginWord)
    #     visited.add(endWord)

    #     begin_visited = set()
    #     begin_visited.add(beginWord)

    #     end_visited = set()
    #     end_visited.add(endWord)

    #     found = False
    #     forward = True
    #     word_len = len(beginWord)
    #     while begin_visited:
    #         if len(begin_visited) > len(end_visited):
    #             begin_visited, end_visited = end_visited, begin_visited
    #             forward = not forward

    #         next_level_visited = set()
    #         for current_word in begin_visited:
    #             word_list = list(current_word)
    #             for j in range(word_len):
    #                 origin_char = word_list[j]
    #                 for k in string.ascii_lowercase:
    #                     word_list[j] = k
    #                     next_word = ''.join(word_list)
    #                     if next_word in word_set:
    #                         if next_word in end_visited:
    #                             found = True
    #                             # 在另一侧找到单词以后，还需把这一层关系添加到「后继结点列表」
    #                             self.__add_to_successors(successors, forward, current_word, next_word)
    #                         if next_word not in visited:
    #                             next_level_visited.add(next_word)
    #                             self.__add_to_successors(successors, forward, current_word, next_word)
    #                 word_list[j] = origin_char
    #         begin_visited = next_level_visited
    #         # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
    #         visited |= next_level_visited
    #         if found:
    #             break
    #     return found

    # def __add_to_successors(self, successors, forward, current_word, next_word):
    #     if forward:
    #         successors[current_word].add(next_word)
    #     else:
    #         successors[next_word].add(current_word)
