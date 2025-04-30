import random
import numpy as np
from tabulate import tabulate

def main():
    n = get_n()
    squared = n * n
    n_type = get_n_type(n)
    n_center = get_n_center(n, n_type, squared)
    num_list = list(range(1, squared + 1))
    goal = get_goal(n, squared, n_type)
    init_square = np.zeros((n, n), dtype=np.int64)

    if n_type == 1:
        square = siamese(n, num_list, n_center, init_square)
    elif n_type == 3:
        square = generic(n, num_list, squared)
    else:
        square = strachey(n, n_center, num_list, squared)

    square = rotate(square)

    if check_sums(square, goal):
        magic = square
        if n <= 31:
            print(tabulate(magic, tablefmt="heavy_grid"))
        else:
            print(square)
        print("congrats! you made magic")
    else:
        print(square)
        print("you suck")

    



def siamese(n, list, n_center, z_square):
    square = z_square
    i, j = 0, n_center - 1

    for num in list:
        square[i, j] = num

        t_i, t_j = (i - 1) % n, (j + 1) % n

        if square[t_i, t_j] != 0:
            i, j = (i + 1) % n, j
        else:
            i, j = t_i, t_j

    square = z_square
    return square


def strachey(n, n_center, num_list, squared):
    count = 0
    size = n // 2
    kmo = ((n - 2) // 4) - 1
    slicer = n_center - 1

    for _ in range(4):
        sublist = num_list[0:(squared // 4)]
        num_list = [x for x in num_list if x not in sublist]
        temp_square = np.zeros((size, size), dtype=np.int64)
        sub_square = siamese(size, sublist, n_center, temp_square)
        
        if count == 0:
            a = sub_square
        elif count == 1:
            b = sub_square
        elif count == 2:
            c = sub_square
        else:
            d = sub_square

        count += 1


    sublist = a[0:size, 0:slicer]
    sub = np.copy(sublist)
    a[0:size, 0:slicer] = d[0:size, 0:slicer]
    d[0:size, 0:slicer] = sub

    if kmo >= 1:
        sublist = c[0:size, -int(kmo):size]
        sub = np.copy(sublist)
        c[0:size, -int(kmo):size] = b[0:size, -int(kmo):size]
        b[0:size, -int(kmo):size] = sub

    t_c = a[slicer, slicer]
    tt_c = np.copy(t_c)
    a[slicer, slicer] = d[slicer, slicer]
    d[slicer, slicer] = tt_c

    t_m = a[slicer, 0]
    tt_m = np.copy(t_m)
    a[slicer, 0] = d[slicer, 0]
    d[slicer, 0] = tt_m


    square = np.zeros((n, n), dtype=np.int64)
    square[0:size, 0:size] = a
    square[0:size, size:n] = c
    square[size:n, 0:size] = d
    square[size:n, size:n] = b
    
    return square


def generic(n, num_list, squared):
    square = np.array(num_list).reshape(n, n)

    maker = squared + 1

    iterator = n // 4

    i, j = 0, 4
    q, r = 0, 4

    for _ in range(iterator):
        for _ in range(iterator):
            piece = square[i:j, q:r]

            itc = [
                (0, 1),
                (0, 2),
                (1, 0),
                (1, 3),
                (2, 0),
                (2, 3),
                (3, 1),
                (3, 2),
            ]

            for v in itc:
                piece[v] = maker - piece[v]

            square[i:j, q:r] = piece

            q += 4
            r += 4

        q = 0
        r = 4
        i += 4
        j += 4

    return square
    


def get_n_type(n):
    if n % 2 != 0:
        n_type = 1  # 1 - n is odd
    else:
        if n % 4 != 0:
            n_type = 2  # 2 - n is singly even
        else:
            n_type = 3  # 3 - n is doubly even

    return n_type

def get_n_center(n, n_type, squared):
    if n_type == 1:
        n_center = int((n / 2) + 0.5)
    elif n_type == 2:
        size = (squared // 4) // (n // 2)
        n_center = int((size / 2) + 0.5)
    else:
        return None

    return n_center


def check_sums(square, goal_num):
    row_sums = np.sum(square, axis=1)
    column_sums = np.sum(square, axis=0)
    diagonal_sum_1 = np.trace(square)
    diagonal_sum_2 = np.trace(np.flip(square, axis=1))
    diagonal_sums = diagonal_sum_1, diagonal_sum_2

    print(f"row sum = {row_sums}")
    print(f"column sum = {column_sums}")
    print(f"diagonal sum = {diagonal_sums}")

    all_sums = row_sums, column_sums, diagonal_sums
    sums = [i for x in all_sums for i in x]

    for i in sums:
        if i == goal_num:
            continue
        else:
            return False
    return True

def rotate(square):
    rotations = [
        np.rot90(square, k=-1),
        np.rot90(square, k=1),
        np.rot90(square, k=2),
        np.flipud(square),
        np.fliplr(square),
    ]
    
    square = random.choice(rotations)

    return square

def get_goal(n, squared, n_type):
    goal = (n * (squared + 1)) // 2

    if n_type == 1:
        print("-Number is odd")
    else:
        print("-Number is even")
    print(f"-Square will be {n} by {n} cells for a total of {squared} cells")
    print(f"-All lines, columns, and diagonals must equal {goal}")

    return goal


def get_n():
    while True:
        try:
            n = int(input("Enter Square size: "))
            if n < 3:
                print(
                    "Square of n < 3 is not possible. Please enter a valid number for n"
                )
                continue
            else:
                return n

        except ValueError:
            print("n must be a valid integer")
            continue


if __name__ == "__main__":
    main()
