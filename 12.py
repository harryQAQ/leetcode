class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        #哈希表，按照从大到小顺序排列
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        for key in hashmap:
            if num // key > 0:
                times = num // key 
                res += hashmap[key] * times
                num %= key
        return res
