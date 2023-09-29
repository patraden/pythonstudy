from collections import deque


def solution(nums: list, k: int) -> list:
    q = deque()
    res = []
    for i in range(len(nums)):
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        q.append(i)
        if i + 1 == k:
            res.append(nums[q[0]])
        elif i + 1 > k:
            while q and q[0] <= i - k:
                q.popleft()
            res.append(nums[q[0]])

    return res


if __name__ == "__main__":
    print(solution([3, 3, 4, -1, 1, 2, 4, 6, 7], 3))
