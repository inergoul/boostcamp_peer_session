https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590/



###### 문제 설명

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.

### 조건

- The number of nodes in the tree is in the range [1, 10^4].
- The values of the nodes of the tree are unique.
- target node is a node from the original tree and is not null.

### 입출력 예제

Example 1

![image](https://user-images.githubusercontent.com/77219563/106407950-9860bc00-6480-11eb-9813-12a05b3d7be8.png)

```python
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
```

Example 2

![image](https://user-images.githubusercontent.com/77219563/106407981-a8789b80-6480-11eb-8f68-090a88b5bd9e.png)

```python
Input: tree = [7], target =  7
Output: 7
```

Example 3

![image](https://user-images.githubusercontent.com/77219563/106407987-aca4b900-6480-11eb-8b8a-63f4fe625cb3.png)

```python
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
```

Example 4

![image](https://user-images.githubusercontent.com/77219563/106407992-b1696d00-6480-11eb-9d77-203e9f90e076.png)

```python
Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5
```

Example 5

![image](https://user-images.githubusercontent.com/77219563/106408000-b4fcf400-6480-11eb-9db4-067cf1a8ec9f.png)

```python
Input: tree = [1,2,null,3], target = 2
Output: 2
```
