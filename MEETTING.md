# Top 100 LeetCode — 2026 FAANG 面试备战清单

> **目标:**大公司 offer 投产比最优解
> **方法论:**基于 2025-2026 行业数据(见文末引用),按"AI 时代底层能力构建"优先级排序
> **原则:**AI 解决 Easy/Medium 95%+,Hard 50-80%。所以选题标准是——
> 1. **模式覆盖率** > 题目数量(100 题覆盖所有高频模式)
> 2. **AI 易错题优先**(state-heavy、变体多、需 verification)
> 3. **Meta 新格式**(AI 协作)与 **Amazon/Google 路线**(硬化变体)都要能接住
> 4. **大厂必考模式** 必入,小众模式压后

---

## 你的进度

仓库内已完成(12 题,标 ✓ ):
- S1 S2 S6 S8 S19 S20 A26 A38 A45 B51 C83

**剩余 88 题。**

---

## TIER S (20 题)— 立刻开始

> **为什么先做这 20 题:**覆盖 LinkedList、Tree、Stack、DP、Backtracking 的核心模式,几乎每场 FAANG 面试都会出现其中 1-2 题。**这 20 题没做透,其他题做了 ROI 也会打折。**

| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| S1 | 206 | Reverse Linked List | LinkedList | Easy | 中 | ✓ |
| S2 | 141 | Linked List Cycle (Floyd) | LinkedList | Easy | 中 | ✓ |
| S3 | 146 | LRU Cache | LinkedList+Hash | Med | **高** ⭐ | |
| S4 | 21 | Merge Two Sorted Lists | LinkedList | Easy | 低 | |
| S5 | 23 | Merge K Sorted Lists | Heap+LinkedList | Hard | **高** ⭐ | |
| S6 | 20 | Valid Parentheses | Stack | Easy | 低 | ✓ |
| S7 | 739 | Daily Temperatures | Monotonic Stack | Med | 中 | |
| S8 | 102 | Binary Tree Level Order | Tree+BFS | Med | 低 | ✓ |
| S9 | 104 | Maximum Depth of Binary Tree | Tree+DFS | Easy | 低 | |
| S10 | 226 | Invert Binary Tree | Tree | Easy | 低 | |
| S11 | 98 | Validate BST | Tree | Med | **高** ⭐ | |
| S12 | 230 | Kth Smallest in BST | Tree | Med | 中 | |
| S13 | 200 | Number of Islands | Graph+BFS/DFS | Med | 中 | |
| S14 | 133 | Clone Graph | Graph+BFS/DFS | Med | **高** ⭐ | |
| S15 | 70 | Climbing Stairs | DP 入门 | Easy | 低 | |
| S16 | 198 | House Robber | DP 模式奠基 | Med | 中 | |
| S17 | 322 | Coin Change | DP BFS 视角 | Med | 中 | |
| S18 | 300 | Longest Increasing Subsequence | DP+Patience | Med | 中 | |
| S19 | 51 | N-Queens | Backtracking | Hard | **极高** ⭐⭐ | ✓ |
| S20 | 239 | Sliding Window Maximum | Deque (单调队列) | Hard | **极高** ⭐⭐ | ✓ |

**S 阶段产出要求:**
- 每题**手写 3 遍**(第一遍想,第二遍闭眼写,第三遍换语言/换输入类型)
- S3 (LRU)、S11 (Validate BST)、S14 (Clone Graph) — 这三题是 Meta 验证题原型,重点练"找 AI 代码 bug"的能力
- S5, S19, S20 属于"AI 一遍写不对"的题,做这些时**禁用 AI**,纯脑推

---

## TIER A (30 题)— 核心模式全覆盖

> 覆盖 Hash、Two Pointers、Sliding Window、Tree 进阶、Backtracking 全家桶、Trie+Backtracking。

### 数组 & 哈希 (A21-A25)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| A21 | 1 | Two Sum | Hash | Easy | 低 | |
| A22 | 49 | Group Anagrams | Hash+Sort | Med | 中 | |
| A23 | 347 | Top K Frequent Elements | Hash+Bucket Sort | Med | 中 | |
| A24 | 238 | Product of Array Except Self | 前缀/后缀 | Med | 中 | |
| A25 | 128 | Longest Consecutive Sequence | Hash | Med | **高** ⭐ | |

### 双指针 (A26-A28)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| A26 | 15 | 3Sum | Two Pointers | Med | 中 | ✓ |
| A27 | 11 | Container With Most Water | Two Pointers | Med | 低 | |
| A28 | 42 | Trapping Rain Water | 双指针/单调栈 | Hard | **高** ⭐ | |

### 滑动窗口 (A29-A32)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| A29 | 121 | Best Time to Buy/Sell Stock | Sliding Window | Easy | 低 | |
| A30 | 3 | Longest Substring Without Repeating | Sliding Window | Med | 中 | |
| A31 | 424 | Longest Repeating Char Replacement | Sliding Window | Med | 中 | |
| A32 | 76 | Minimum Window Substring | Sliding Window | Hard | **高** ⭐ | |

### 链表进阶 (A33-A37)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| A33 | 2 | Add Two Numbers | LinkedList 模拟 | Med | 中 | |
| A34 | 143 | Reorder List | LinkedList | Med | 中 | |
| A35 | 19 | Remove Nth From End | LinkedList 双指针 | Med | 低 | |
| A36 | 138 | Copy List with Random Pointer | LinkedList+Hash | Med | **高** ⭐ | |
| A37 | 25 | Reverse Nodes in k-Group | LinkedList | Hard | **高** ⭐ | |

### 树进阶 (A38-A44)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| A38 | 235 | LCA of BST | Tree | Med | 中 | ✓ |
| A39 | 100 | Same Tree | Tree | Easy | 低 | |
| A40 | 572 | Subtree of Another Tree | Tree | Easy | 中 | |
| A41 | 105 | Construct BT from Preorder+Inorder | Tree | Med | **高** ⭐ | |
| A42 | 124 | Binary Tree Maximum Path Sum | Tree+DFS | Hard | **高** ⭐ | |
| A43 | 297 | Serialize/Deserialize Binary Tree | Tree | Hard | **高** ⭐ | |
| A44 | 108 | Convert Sorted Array to BST | Tree | Easy | 低 | |

### 回溯全家桶 (A45-A50)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| A45 | 22 | Generate Parentheses | Backtracking | Med | 中 | ✓ |
| A46 | 78 | Subsets | Backtracking | Med | 低 | |
| A47 | 46 | Permutations | Backtracking | Med | 低 | |
| A48 | 39 | Combination Sum | Backtracking | Med | 中 | |
| A49 | 79 | Word Search | Backtracking+DFS | Med | 中 | |
| A50 | 212 | Word Search II | Trie+Backtracking | Hard | **极高** ⭐⭐ | |

**A 阶段产出要求:**
- Hash 系列 (A21-A25) 闭眼写出来
- Sliding Window 四题 (A29-A32) 是同一模板,要能默写
- A50 (Word Search II) 重点练——是 **Tire + 回溯** 的复合,大厂最爱变体

---

## TIER B (30 题)— 完整模式,大厂高优

### 堆 (B51-B53)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| B51 | 703 | Kth Largest in Stream | Heap | Easy | 低 | ✓ |
| B52 | 973 | K Closest Points to Origin | Heap | Med | 中 | |
| B53 | 295 | Find Median from Data Stream | Two Heaps | Hard | **高** ⭐ | |

### 二分 (B54-B58)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| B54 | 33 | Search in Rotated Sorted Array | BS | Med | 中 | |
| B55 | 153 | Find Min in Rotated Sorted Array | BS | Med | 中 | |
| B56 | 74 | Search a 2D Matrix | BS | Med | 低 | |
| B57 | 875 | Koko Eating Bananas | BS on Answer | Med | 中 | |
| B58 | 4 | Median of Two Sorted Arrays | BS | Hard | **高** ⭐ | |

### 栈进阶 (B59-B62)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| B59 | 155 | Min Stack | Stack 维护 | Easy | 低 | |
| B60 | 150 | Evaluate RPN | Stack | Med | 低 | |
| B61 | 84 | Largest Rectangle in Histogram | Monotonic Stack | Hard | **极高** ⭐⭐ | |
| B62 | 853 | Car Fleet | Stack | Med | 中 | |

### DP 全家桶 (B63-B73)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| B63 | 152 | Maximum Product Subarray | DP | Med | 中 | |
| B64 | 5 | Longest Palindromic Substring | DP | Med | 中 | |
| B65 | 1143 | Longest Common Subsequence | 2D DP | Med | 中 | |
| B66 | 72 | Edit Distance | 2D DP | Hard | **高** ⭐ | |
| B67 | 139 | Word Break | DP+Trie | Med | 中 | |
| B68 | 55 | Jump Game | DP+Greedy | Med | 低 | |
| B69 | 53 | Maximum Subarray (Kadane) | DP | Med | 低 | |
| B70 | 91 | Decode Ways | DP | Med | 中 | |
| B71 | 62 | Unique Paths | 2D DP | Med | 低 | |
| B72 | 213 | House Robber II | DP | Med | 中 | |
| B73 | 416 | Partition Equal Subset Sum | 背包 DP | Med | 中 | |

### 区间 & 图 & BFS (B74-B80)
| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| B74 | 56 | Merge Intervals | Intervals | Med | 中 | |
| B75 | 57 | Insert Interval | Intervals | Med | 中 | |
| B76 | 435 | Non-overlapping Intervals | Greedy+Sort | Med | 中 | |
| B77 | 994 | Rotting Oranges | BFS 多源 | Med | 中 | |
| B78 | 207 | Course Schedule | Topo Sort | Med | 中 | |
| B79 | 210 | Course Schedule II | Topo Sort | Med | 中 | |
| B80 | 127 | Word Ladder | BFS | Hard | **高** ⭐ | |

---

## TIER C (20 题)— 补全小众模式

> 这些是"如果面试遇到不亏,没遇到也不亏"的题。**S+A+B 完成后还有余力再做。**

| # | LC# | 题目 | 模式 | 难度 | AI 易错? | 已做 |
|---|---|---|---|---|---|---|
| C81 | 208 | Implement Trie | Trie | Med | 中 | |
| C82 | 211 | Add and Search Words | Trie+DFS | Med | 中 | |
| C83 | 242 | Valid Anagram | Hash | Easy | 低 | ✓ |
| C84 | 125 | Valid Palindrome | Two Pointers | Easy | 低 | |
| C85 | 17 | Letter Combinations of Phone Number | Backtracking | Med | 低 | |
| C86 | 90 | Subsets II (含重复) | Backtracking | Med | 中 | |
| C87 | 131 | Palindrome Partitioning | Backtracking+DP | Med | 中 | |
| C88 | 518 | Coin Change II (组合数) | 背包 DP | Med | 中 | |
| C89 | 35 | Search Insert Position | BS | Easy | 低 | |
| C90 | 34 | First and Last Position | BS | Med | 低 | |
| C91 | 136 | Single Number | Bit XOR | Easy | 低 | |
| C92 | 191 | Number of 1 Bits | Bit | Easy | 低 | |
| C93 | 268 | Missing Number | Bit | Easy | 低 | |
| C94 | 338 | Counting Bits | Bit+DP | Easy | 低 | |
| C95 | 134 | Gas Station | Greedy | Med | 中 | |
| C96 | 621 | Task Scheduler | Heap+Greedy | Med | 中 | |
| C97 | 763 | Partition Labels | Greedy | Med | 中 | |
| C98 | 543 | Diameter of Binary Tree | Tree | Easy | 低 | |
| C99 | 110 | Balanced Binary Tree | Tree | Easy | 低 | |
| C100 | 236 | LCA of Binary Tree | Tree | Med | 中 | |

---

## 复习节奏建议

**Phase 1 (前 4 周):S + A (50 题)**
- 每天 2 题新题 + 1 题旧题复盘
- 重点:每题想清楚**为什么这样不是那样**、**模式名是什么**、**变体会有哪些**
- 禁用 AI 解题,但可以问 AI 思路

**Phase 2 (第 5-8 周):B (30 题)**
- 每天 1.5 题新题 + 1 题旧题
- 开始**用 AI 写、自己找 bug**——这是 Meta 新格式的刻意练习
- 每个模式(DP、BS、Graph)做一张"变体清单"

**Phase 3 (最后 2-3 周):C (20 题) + 全量 Mock**
- 计时做 Pramp / Interviewing.io
- 把 Top 20 AI-易错题在白板上手写一遍(无 IDE)
- 准备行为面试故事库(STAR 法)

**Phase 4 (面试中):**
- 如果公司是 **Meta 路线**(AI 协作):练习"用 AI 写、自己 verify"的循环,重点是**给 AI 准确的 prompt + 找出它的边界 case bug**
- 如果公司是 **Amazon/Google 路线**(硬化变体):练"看到新题 30 秒内识别模式"的速度

---

## 跳过/低 ROI 的题(明确不推荐做)

- 大数 Easy 题(Two Sum II、Fizz Buzz、Reverse Integer)— 已饱和,AI 100%,做了没区分度
- 偏数学证明类(Median of Two Sorted Arrays 后 30% 边界)— 出现率下降
- Hard 里小众模式(扫描线、KD-Tree、Suffix Array)— 出现率 < 5%
- Premium 题(除非你确定要面那家公司)— 投入产出比低

---

## 数据来源

- 面试形式变化:[TechCrunch — OpenAI embarrassing math](https://techcrunch.com/2025/10/19/openais-embarrassing-math) · [interviewing.io 调查](https://interviewing.io/blog/how-is-ai-changing-interview-processes-not-much-and-a-whole-lot) · [bytebytego](https://www.bytebytego.com/) · [Meta AI 编码面试](https://www.gankinterview.cn/en/blog/meta-allows-candidates-to-use-ai-in-coding-interviews-will-this-shift-the-focus-from-)
- AI 能力 benchmark:[GPT-5 vs Claude 4.5 比较](https://dobermanvc.com/comparative-analysis-openai-gpt-5-vs-anthropic-claude-4-5) · [datastudios 报告](https://www.datastudios.org/post/claude-opus-4-5-vs-chatgpt-5-1-full-report-and-comparison-of-models-features-performance-pricin)
- 题单基础:[NeetCode 150](https://neetcode.io/practice) · [Blind 75](https://leetcode.com/list/x1l9ajn8/) · [Tech Interview Handbook](https://www.techinterviewhandbook.org/blind75)
- AI 时代策略:[Stop Cheating with AI](https://dev.to/alex_hunter_44f4c9ed6671e/stop-cheating-with-ai-the-senior-engineers-guide-to-leetcode-144n) · [DSA & LeetCode in 2025](https://dev.to/govindup63/dsa-leetcode-in-2025-still-relevant-in-the-age-of-ai-1g8o)

---

**最后一句:**这 100 题做透,大厂算法面试有 80% 胜率。剩下 20% 拼的是**运气、behavioral、和运气**。别刷到 500——刷到 100 后,系统设计 + 行为故事 + 真项目经历的 ROI 更高。
