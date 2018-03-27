def is_inside(point=[], rect=[]):
    if rect[0] <= point[0] <= rect[0] + rect[2] \
    and rect[1] <= point[1] <= rect[1] + rect[3]:
        return True
    else:
        return False

#testcase, phiền a quý xóa cmt để check bài nhé :)))

point_is_inside = is_inside([200, 150], [140, 60, 100, 200])

point_is_outside = is_inside([300, 250], [140, 60, 100, 200])

if point_is_inside == True and point_is_outside == False:
    print("Your function is corret")
else:
    print("Oops, there's a bug")
