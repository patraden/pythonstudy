def solution(nums: list) -> list:
    if not nums:
        return nums

    p = 0  # positive num index
    while nums[p] < 0:
        p += 1

    res = []
    n = p - 1  # negative num index
    while n + 1 > 0 or p < len(nums):
        if n + 1 == 0:
            res.append(nums[p] * nums[p])
            p += 1
        elif p == len(nums):
            res.append(nums[n] * nums[n])
            n -= 1
        elif -nums[n] < nums[p]:
            res.append(nums[n] * nums[n])
            n -= 1
        else:
            res.append(nums[p] * nums[p])
            p += 1
    return res


if __name__ == "__main__":
    print(solution([-5, -3, -2, -1, 1, 2, 4, 6, 7]))
    print(solution([-1, 0, 1, 2, 3]))
