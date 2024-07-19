def area_sum(rectangles):
    sum_area = 0
    for i in range(len(rectangles)):
        sum_area += rectangles[i]["height"]*rectangles[i]["width"]
    return sum_area