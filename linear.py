def linear(coord1, coord2, x):
    print(coord1)
    print(coord2)
    m = (coord2[1]-coord1[1]) / (coord2[0]-coord1[0])
    b = coord1[1] - m*coord1[0]

    y = m*x + b

    return y
