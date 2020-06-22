# quickhull.py
# Quickhull Algorithm
# By: Shahzeb Jadoon

def convex_hull(unordered_points):
    """ Preprocess (sort, and eliminate repeated points), and use quickhull algorithm

        pre: unordered_points is a list which is not sorted in nondecreasing order. 
             unordered_points comprises of tuples of the form (x, y) where x represents
             the x-axis location and y represents the y-axis location of the point
             on the cartesian plane
        post: returns the list of points which form the conve hull when connected 
              in the order they are in the list
    """

    convex_merge_sort(unordered_points)
    ordered_points = convex_elim(unordered_points)
    hull_lst = quick_hull(ordered_points)

    return hull_lst


def convex_merge_sort(unordered_points):
    """ Helping function for convex_hull() which sorts the points in nondecreasing order

        pre: unordered_points is a list that needs to be sorted in nondecreasing order.
             unordered_points comprises of tuples of the form (x, y) where x represents
             the x-axis location and y represents the y-axis location of the point
             on the cartesian plane
        post: sorts the unordered_points in non-decreasing order
    """

    lst_size = len(unordered_points)

    if lst_size > 1:
        first_half = unordered_points[:lst_size//2]
        second_half = unordered_points[lst_size//2:]
        convex_merge_sort(first_half)
        convex_merge_sort(second_half)
        convex_merge(first_half, second_half, unordered_points)


def convex_merge(first_half, second_half, lst):
    """ Helping function for convex_merge_sort()

        pre: first_half and second_half are the first and second half of the list
             that have been sorted
        post: alters lst so that the elements of first_half and second_half are 
              placed in nondecreasing order
    """

    i = 0; j = 0; k = 0
    p = len(first_half); q = len(second_half)

    while i < p and j < q:

        if first_half[i] <= second_half[j]:
            lst[k] = first_half[i]
            i += 1

        else:
            lst[k] = second_half[j]
            j += 1
            
        k += 1

    if i == p:

        for item in second_half[j:]:
            lst[k] = item
            k += 1

    else:

        for item in first_half[i:]:
            lst[k] = item
            k += 1


def convex_elim(ordered_points):
    """ Helping function for convex_hull() which eliminates repeating points

        pre: ordered_points is a list of points sorted in nondecreasing order.
             ordered_points comprises of tuples of the form (x, y) where x represents
             the x-axis location and y represents the y-axis location of the point
             on the cartesian plane
        post: retruns a list with distinct points of ordered_points
    """

    new_lst = []

    for i in range(len(ordered_points) - 1):

        if ordered_points[i] != ordered_points[i + 1]:
            new_lst.append(ordered_points[i])

    new_lst.append(ordered_points[-1])

    return new_lst


def quick_hull(ordered_points):
    """ Helping function for convex_hull() that finds the points that comprise the
        convex hull of the ordered_points

        pre: ordered_points is a list of points sorted in nondecreasing order.
             ordered_points comprises of tuples of the form (x, y) where x represents
             the x-axis location and y represents the y-axis location of the point
             on the cartesian plane
        post: returns the list of points which form the conve hull when connected 
              in the order they are in the list
    """

    lst_size = len(ordered_points)

    if lst_size > 2:
        p_first = ordered_points[0]
        p_last = ordered_points[-1]

        determ_lst = [determ(p_first, p_last, p) for p in ordered_points]
        left_points = [(ordered_points[i], determ_lst[i]) for i in range(lst_size) if determ_lst[i] > 0]
        right_points = [(ordered_points[i], determ_lst[i]) for i in range(lst_size) if determ_lst[i] < 0]

        upper_points = upper_hull(p_first, p_last, left_points)
        lower_points = lower_hull(p_first, p_last, right_points)

        lower_points = reverse(lower_points)

        convex_hull_lst = [p_first] + upper_points + [p_last] + lower_points

        return convex_hull_lst

    else:
        return ordered_points


def determ(p1, p2, p3):
    """ Helping function for convex_hull() that calculates the determinant of 3 points

        pre: p1, p2, p3 are tuples of the form (x, y) where x represents
             the x-axis location and y represents the y-axis location of the point
             on the cartesian plane
        post: returns the determinant of the three points (p1, p2, & p3)
    """

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return (x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3)


def reverse(lst):
    """ Helping function for convex_hull() that reverses the order of a list

        pre: lst is a python list
        post: returns a list which is a mirror image of lst (lst is reversed)
    """

    new_lst = []

    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])

    return new_lst


def upper_hull(p_first, p_last, points):
    """ Helping function for convex_hull() that returns the points that comprise the
        upper part/hull of the convex hull

        pre: p_first and p_last are points with the lowest and highest x-value. points is
             a list containing tuples of the structure ((x, y), det) where (x, y) is itself a 
             tuple representing a point on the cartesian plane with x and y being the x-axis
             and y-axis values respectively. The det is the determinant of the point (x, y) 
             with p_first and p_last.
        post: returns the points that comprise the upper hull when connected in the
              order they are in the list
    """

    lst_size = len(points)

    if lst_size > 1:
        p_max, max_det = points[0]

        for p, det in points:

            if det > max_det:
                p_max = p
                max_det = det

        determ_lst1 = [determ(p_first, p_max, p) for p, d in points]
        determ_lst2 = [determ(p_max, p_last, p) for p, d in points]
        p_lst1 = [(points[i][0], determ_lst1[i]) for i in range(lst_size) if determ_lst1[i] > 0]        
        p_lst2 = [(points[i][0], determ_lst2[i]) for i in range(lst_size) if determ_lst2[i] > 0]

        left_half = upper_hull(p_first, p_max, p_lst1)
        right_half = upper_hull(p_max, p_last, p_lst2)

        left_half.append(p_max)
        left_half.extend(right_half)

        return left_half

    else:

        if points == []:
            return points

        else:
            return [points[0][0]]


def lower_hull(p_first, p_last, points):
    """ Helping function for convex_hull() that returns the points that comprise the
        lower part/hull of the convex hull

        pre: p_first and p_last are points with the lowest and highest x-value. points is
             a list containing tuples of the structure ((x, y), det) where (x, y) is itself a 
             tuple representing a point on the cartesian plane with x and y being the x-axis
             and y-axis values respectively. The det is the determinant of the point (x, y) 
             with p_first and p_last.
        post: returns the points that comprise the lower hull when connected in the
              order they are in the list after the list is reversed
    """

    lst_size = len(points)

    if lst_size > 1:
        p_max, max_det = points[0]

        for p, det in points:

            if det < max_det:
                p_max = p
                max_det = det

        determ_lst1 = [determ(p_first, p_max, p) for p, d in points]
        determ_lst2 = [determ(p_max, p_last, p) for p, d in points]
        p_lst1 = [(points[i][0], determ_lst1[i]) for i in range(lst_size) if determ_lst1[i] < 0]        
        p_lst2 = [(points[i][0], determ_lst2[i]) for i in range(lst_size) if determ_lst2[i] < 0]

        left_half = lower_hull(p_first, p_max, p_lst1)
        right_half = lower_hull(p_max, p_last, p_lst2)

        left_half.append(p_max)
        left_half.extend(right_half)

        return left_half

    else:

        if points == []:
            return points

        else:
            return [points[0][0]]


def main():
    """ Allows the user to visualize a convexx hull based on random points. The user
        can choose the number of points.

        post: displays the points on a graphical window as circles, with line segments
              that connect the points that form the convex hull. 
    """
    
    print("This program allows the user to visualize a convex hull of random point")
    print("The user can choose the number of points from which to draw the convex hull,")
    n = int(input("thus enter the number of points: "))
    
    unordered_points = []
    width = 800
    height = 600

    for i in range(n):
        unordered_points.append((randrange(width*0.1, width*0.9), randrange(height*0.1, height*0.9)))
    
    convex_hull_lst = convex_hull(unordered_points)

    win = GraphWin("Convex Hull Implementation", width, height, autoflush=False)
    win.setCoords(0, 0, width, height)
    
    for point in unordered_points:
        Circle(Point(point[0], point[1]), 1.5).draw(win)

    for i in range(len(convex_hull_lst) - 1):
        Line(Point(convex_hull_lst[i][0], convex_hull_lst[i][1]), Point(convex_hull_lst[i + 1][0], convex_hull_lst[i + 1][1])).draw(win)

    Line(Point(convex_hull_lst[0][0], convex_hull_lst[0][1]), Point(convex_hull_lst[-1][0], convex_hull_lst[-1][1])).draw(win)

    message = Text(Point(width/2, height*0.95), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    from graphics import GraphWin, Point, Line, Text, Circle
    from random import randrange
    
    main()