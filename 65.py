class Solution:
    def isNumber(self, s: str) -> bool:
        # s = s.strip()  # 去掉两端的空白符
        # if not s :
        #     return False
        # else:
        #     if s[0] in ['+', '-']:
        #         s = s[1:]  # 去掉正负号
        #     if 'e' in s:
        #         temp_list = s.split('e')
        #         if len(temp_list) > 2:  # 字符串s中含有多于一个的’e‘,返回False
        #             return False
        #         temp_list[0] = temp_list[0].replace('.', '', 1)  # 去掉e前面的字符串中的'.'
        #         if len(temp_list[1]) > 0 and temp_list[1][0] in ['+', '-']:  # 去掉e后面字符串中的'+'或者'-'
        #             temp_list[1] = temp_list[1].replace(temp_list[1][0], '', 1)
        #         if temp_list[0].isnumeric() and temp_list[1].isnumeric():
        #             return True
        #         return False
        #     else:  # s中不含'e'
        #         s = s.replace('.', '', 1)
        #         if s.isnumeric():
        #             return True
        #         return False
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        
        state = 0
        for c in s:
            if '0' <= c <= '9': now = 'd'
            elif c in '+-': now = 's'
            else: now = c
            if now not in states[state]: return False
            state = states[state][now]

        return state in [2, 3, 7, 8]

