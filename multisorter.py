# multisorter.py
# Multi Sorter Program
# By: Shahzeb Jadoon

def bubble_sort(lst):
    """Sorts a given list using bubble sort algorithm
       
       pre: lst is a list of elements that can be ordered
       post: returns new_lst with elements of lst sorted in increasing order
    """

    lst_size = len(lst)
    
    for i in range(lst_size - 1):

        for j in range(lst_size - 1 - i):

            if lst[j + 1] < lst[j]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def comp_count_sort(unordered_lst):
    """Sorts a list by comparison counting.

       pre: unordered_lst is an unordered list of floating point numbers
       post: sorted_lst which comprises of unordered_lst's elements
             sorted in an increasing order.
    """

    n = len(unordered_lst)

    # create a list of counts, and a list to create a sorted list
    count_lst = []
    sorted_lst = []
    
    # append zeros to count_lst and sorted_lst to make them size n
    for i in range(n):
        count_lst.append(0)
        sorted_lst.append(0)

    # count how many items are smaller/greater for each item
    for i in range(n-1):    

        for j in range(i + 1, n):

            if unordered_lst[i] < unordered_lst[j]:
                count_lst[j] = count_lst[j] + 1

            else:
                count_lst[i] = count_lst[i] + 1

    for i in range(n):
        sorted_lst[count_lst[i]] = unordered_lst[i]

    return sorted_lst


def selection_sort(lst):
    """Sorts a given list by selectioon sort

       pre: lst is a list of elements that can be ordered
       post: returns new_lst with elements of lst sorted in increasing order
    """

    lst_size = len(lst)

    # swap the current item being looped over with the smallest item in lst
    
    for i in range(lst_size - 1):
        min = i

        for j in range(i + 1, lst_size):

            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
        
    return lst


def multisorter():
    """This program lets the user implement multiple sorting algorithms
       (namely Bubble Sort, Comparison Count Sort, & Selection Sort),
       and lets them measure their running time.
    """

    print("Welcome to the Multi Sorter Program\n")
    key_pressed = str(input("Would you like to start? (Y/N) "))
    print()

    while key_pressed[0].lower() == "y":
        # user inputs an int for the list size
        lst_size = int(input("Enter the list size: "))
        print()
        
        # user inputs an int for the number of trials
        trial_num = int(input("Enter the number of trials: "))

        # ask user for the sorting algorithm they want to use
        print("\nWhich sort method would you like to use? (Enter 'Bubble' or 1)")
        print("for Bubble Sort, 'SelSort' or 2 for Selection Sort, or CompSort ")
        method = str(input(" or 3 for Comparison Count Sort, and press enter): "))
        unordered_lst = []
        num = len(list(str(lst_size))) - 1

        # create a (unordered) list of the size provided by user        
        for i in range(lst_size):
            unordered_lst.append(round(random.random() * (10 ** random.randrange(0,num)), 2))
            
        trial_times = []
        print()
        function = ""

        # choose the sorting algorithm based on user input
        if method[0].lower() == "b" or method == "1":
            function = bubble_sort

        elif method[0].lower() == "s" or method == "2":
            function = selection_sort

        elif method[0].lower() == "c" or method == "3":
            function = comp_count_sort

        # raise an error if input to choose algorithm is not valid
        else:
            raise Exception("Invalid Input")

        # this catches any errors in input and restarts the program
        try:
            for i in range(trial_num):
                temp_lst = unordered_lst.copy()
                time_1 = time.time()
                sorted_list = function(temp_lst)
                time_2 = time.time()
                time_taken = time_2 - time_1
                trial_times.append(time_taken)
                print("Trial", str(i+1) + ": ", round(time_taken, 2))
                
            total_trial_time = sum(trial_times)
            average_time = total_trial_time/trial_num
            
            print("Total:   ", round(total_trial_time, 2), "\n")
            print("Average:     ", round(average_time, 2))
            print("Average/n**2:", (str(average_time/(lst_size**2)))[:4] + (str(average_time/(lst_size**2)))[-4:])

            key_pressed = str(input("\nDo you want to try another sorting algorithm? (Y/N) "))
            print()

        except:
            print("Invalid Input\n")
            key_pressed = str(input("Would you like to start again? (Y/N) "))
    
    # end the program with a closing comment
    if key_pressed[0].lower() == "n":
        print("Thank you for using the Multisorter program")

    else:
        raise Exception("Invalid Input")


if __name__ == '__main__':
    import time
    import random

    multisorter()