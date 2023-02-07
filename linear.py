def linear(coord1, coord2, x):
    m = (coord2[1]-coord1[1]) / (coord2[0]-coord2[0])
    b = coord1[1] - m*coord1[0]

    y = m*x + b

    return y