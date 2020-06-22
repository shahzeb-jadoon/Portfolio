# heap_sort.py
# Heap Sort
# By: Shahzeb Jadoon

def heapify(lst, index, lst_size):
    """ Helping function for build_heap() that makes sure the items in the position
        of index are where they are supposed to be

        pre: lst is a list of items that is not sorted in nondecreasing order. lst_size
             is the size of the lst provided. index is the position of item which is
             being verified whether it is in the correct position in the heap
        post: places the item in position index in its correct place
    """

    k = (2 * (index + 1)) - 1

    if k < lst_size:

        if k + 1 < lst_size:

            if lst[2 * (index + 1)] > lst[k]:
                k = 2 * (index + 1)

            if lst[k] > lst[index]:
                lst[k], lst[index] = lst[index], lst[k]
                heapify(lst, k, lst_size)

        else:

            if lst[k] > lst[index]:
                    lst[k], lst[index] = lst[index], lst[k]
                    heapify(lst, k, lst_size)

def build_heap(lst, lst_size):
    """ Builds a heap from a provided lst

        pre: lst is a list of items that is not sorted in nondecreasing order. lst_size
             is the size of the lst provided
        post: converts the lst into a heap (in-place algorithm)
    """

    for index in range((lst_size//2) - 1, -1, -1):
        heapify(lst, index, lst_size)

def heap_sort(lst):
    """ Sorts the give lst using heap sort algorithm

        pre: lst is a list of items that is not sorted in nonddecreasing order
        post: sorts lst after converting it into a heap.
    """

    lst_size = len(lst)
    build_heap(lst, lst_size)
    
    while lst_size > 0:
        lst[0], lst[lst_size - 1] = lst[lst_size - 1], lst[0]
        lst_size -= 1
        heapify(lst, 0, lst_size)


def main():
    """ This program demonstrates how heap sort works

        post: prints the unsorted and sorted list
    """

    print("This program allows the user to visualize heap sort on a list of a size")
    lst_size = int(input("provided by the user, thus, enter list size: "))
    
    lst = []

    for i in range(lst_size):
        lst.append(randrange(0, 5000))

    print("\nThe list is:\n", lst, "\n")
    
    key_pressed = str(input("Would you like to see a heap made from this list? (Y/N) "))

    if key_pressed[0].lower() == "y":
        build_heap(lst, lst_size)
        print("\nThe heap is:\n", lst, "\n")

    heap_sort(lst)

    key_pressed = str(input("Press <enter> to see the sorted list"))

    print("\nThe sorted list is:\n", lst)

if __name__ == "__main__":
    from random import randrange
    
    main()