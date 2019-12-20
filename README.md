## leetcode
+ 1.Two Sum

    python中的hashmap用字典实现，可以用get方法获取key对应的value，用is not None判断是否在hashmap中. PS:用in/not in来判断是否在list中。list获取特定元素的索引：nums.index(item)

    带索引的迭代：
    ```
    for idx, num in enumerate(nums):
    ```      

+ 3.Longest Substring Without Repeating Characters

    滑动窗口。其实就是一个队列,比如例中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，滑动这个窗口！那滑到什么位置呢？右指针的位置不变，左指针滑一直到窗口内无重复的字符为止。

+ 6.ZigZag Conversion

    题目要求得到z字型字符串，但只需要按行打印即可，可以从按行打印入手，每一行作为一个字符串拼接即可。设numRows行字符串分别为$S_1$...$S_n$,显然，按顺序遍历字符串时，每个字符的行索引从小到大，再从大到小。如此模拟便可。

    PS：python列表生成式:[廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776)

+ 7.Reverse Integer

    最直接的想法是字符串翻转，可以利用python字符串切片直接完成翻转：
  ```
  str = str[::-1]
  ```
    但是注意完成转换后需要判断是否溢出. 32-bit signed integer range: [−2^31,  2^31 − 1].利用左移可以直接设置上限2^31 - 1 / 2^31 

    也可直接进行翻转，但是，python存储数字理论上是无限长度，每次计算好要判断是否溢出。Python的坑： 由于Python的 // 操作是向下取整，导致正负数取余 % 操作结果不一致，因此需要将原数字转为正数操作。

+ 8.String to Integer (atoi)

    string去空格，strip(),去左空格lstrip()

    python一行解法 正则表达式 还是强啊...

    ```
    class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

    ```  

    ```
    ^：匹配字符串开头
    [\+\-]：代表一个+字符或-字符
    ?：前面一个字符可有可无
    \d：一个数字
    +：前面一个字符的一个或多个
    \D：一个非数字字符
    *：前面一个字符的0个或多个
    ```


    ```
    max(min(数字, 1<<31 - 1), -1<<31) #用来防止结果越界
    ```

+ 9.Palindrome Number

    数字<0，有负号肯定不满足，正数利用字符串切片逆转下判断是否相同即可


+ 13.Roman to Integer

    建立map后，逆着读取字符串，若本位比上位小，就减去该位，否则加上该位。

+ 15.3Sum

    暴力搜索o(N^3)会超时，排序后，利用元素大小作为限制以及双指针的思想减小解空间来优化效率。

    注意要避免重复组合的保存，如果python写判断list是否在res中，一样也会超时。注意下面两种情况的优化。

    （1）当 nums[k] > 0 时直接break跳出：因为 nums[j] >= nums[i] >= nums[k] > 0，即 33 个数字都大于 00 ，在此固定指针 k 之后不可能再找到结果了。
    
    （2）当 k > 0且nums[k] == nums[k - 1]时即跳过此元素nums[k]：因为已经将 nums[k - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。

    当判断存在一组解后，在两边的指针保证不相交的情况下，两个指针都要移到与前一个位置不同的地方，否则还是已存在的解。

+ 24.Swap Nodes in Pairs

    看25题升级版吧

+ 25.Reverse Nodes in k-Group
  
    本题是24题的扩展，k==2时候就成了24题。题意是k个一组翻转链表，在翻转了前k个结点后，对剩余的链表操作其实是做了同样逻辑的操作，比较清晰的思路是把相同的操作抽象出来（较复杂可以作为一个函数），然后在对最上层的一部分做操作的时候调用自身解决下一个小规模的问题，在写递归的时候注意递归出口的条件(所谓的base case)。在本题中，base case是本次调用链表中的结点个数小于k，之后的顺序是：翻转当前链表的前k个，对剩下的链表调用自身。
  
    关于递归法翻转链表，推荐一个分析，很清晰：[步步拆解：如何递归地反转链表的一部分](https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/bu-bu-chai-jie-ru-he-di-gui-di-fan-zhuan-lian-biao/) 

     分析递归算法的时候，不要跳进递归（你的脑袋能压几个栈呀？），而是要根据函数定义，来弄清楚这段代码会产生什么结果。

+ 230.Kth Smallest Element in a BST

    利用python生成器，在中序递归的时候利用生成器存储中序结果。

    ```
    yield from some_generator
    ```
    相当于

    ```
    for x in some_generator: 
        yield x
    ```


+ 739.Daily Temperatures

    利用单调栈（Monotone Stack），每个数字只进栈并处理一次，而解决问题的核心就在处理这块，当前数字如果破坏了单调性，就会触发处理栈顶元素的操作，而触发数字有时候是解决问题的一部分。