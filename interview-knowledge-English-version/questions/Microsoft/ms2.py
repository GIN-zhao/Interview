import random


def matrixRandomChoose(a, b, n):
    member_num = [i for i in range(a * b)]
    matrix_length = a * b
    member_chosen = []
    if n > matrix_length:
        return member_num
    for i in range(n):
        index = random.randint(0, matrix_length - i - 1)
        member_chosen.append(member_num[index])
        member_num[index], member_num[matrix_length - i - 1] = member_num[matrix_length - i - 1], member_num[index]

    return member_chosen


if __name__ == '__main__':
    print(matrixRandomChoose(2, 2, 5))
