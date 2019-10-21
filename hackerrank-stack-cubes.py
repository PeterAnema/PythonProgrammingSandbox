def solution(n, sides):
    stack_top = None

    left_index = 0
    right_index = len(sides) - 1

    while left_index <= right_index:
        if sides[left_index] >= sides[right_index]:
            if stack_top is None or sides[left_index] <= stack_top:
                stack_top = sides[left_index]
                left_index += 1
            else:
                return False
        else:
            if stack_top is None or sides[right_index] <= stack_top:
                stack_top = sides[right_index]
                right_index -= 1
            else:
                return False

    return True

#-------------------------------------------------------------------------

if __name__ == '__main__':

    T = int(input())
    stacks = []
    for t in range(T):
        n = int(input())
        sides = tuple(map(int, input().split()))
        assert n == len(sides)
        stacks.append((n, sides))

    for n, sides in stacks:
        success = solution(n, sides)
        print("Yes" if success else "No")
