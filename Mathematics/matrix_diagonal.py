M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


N = [[2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

left_right = [M[i][i] for i in range(len(M))]

right_left = [M[i][len(M)-1-i] for i in range(len(M))]