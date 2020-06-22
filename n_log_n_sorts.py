# n_log_n_sorts.py
# n log n Sorting Algorithms
# By: Shahzeb Jadoon

def mergesort(unordered_lst):
    """ Sorts a list in nondecreasing order using recursive mergesort algorithm

        pre: unordered_lst is a lst that needs to be sorted
        post: In-place algorithm, therefore the same list is altered to be nondecreasing
    """

    lst_size = len(unordered_lst)

    if lst_size > 1:
        first_half = unordered_lst[:lst_size//2]
        second_half = unordered_lst[lst_size//2:]
        mergesort(first_half)
        mergesort(second_half)
        merge(first_half, second_half, unordered_lst)


def merge(first_half, second_half, lst):
    """ Helping function for mergesort

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


def insertion_sort(unordered_lst):
    """ Sorts a list using insertion sort algorithm

        pre: unordered_lst is a list that needs to be sorted in nondecreasing order
        post: in-place sort, so it does not return anything, but sorts the unordered_lst
    """
    
    lst_size = len(unordered_lst)

    for i in range(1, lst_size):
        v = unordered_lst[i]
        j = i - 1

        while j >= 0 and unordered_lst[j] > v:
            unordered_lst[j + 1] = unordered_lst[j]
            j -= 1
        unordered_lst[j + 1] = v

def quicksort(unordered_lst, left_most, right_most):
    """ Sorts a list using median of three quicksort algorithm. Finds the median by first
        sorting them using insertion sort, and then selecting the middle value

        pre: unordered_lst is a list that needs to be sorted in nondecreasing order.
             left_most and right_most are the index of the left most and right_most 
             items of the list
        post: in-place sort, so it does not return anything, but sorts the unordered_lst
    """

    if left_most < right_most:
        s = partition(unordered_lst, left_most, right_most)
        quicksort(unordered_lst, left_most, s - 1)
        quicksort(unordered_lst, s + 1, right_most)

def partition(unordered_lst, left_most, right_most):
    """ Helping function for quicksort() that utilizes the median of three algorithm.
        The median of three algrithm chooses the partition element by selecting the median
        of the first, last, and middle element of a list

        pre: unordered_lst is a list that needs to be sorted in nondecreasing order.
             left_most and right_most are the index of the left most and right_most 
             items of the list
        post: partially sorts the list so that at the partition which is the index returned
              by this function, every element is lower than the element at the partition
              and every element after the partition is higher than the partition element
    """

    list_mid = (right_most + left_most)//2

    lmr_list = [unordered_lst[left_most], unordered_lst[list_mid], unordered_lst[right_most]]
    insertion_sort(lmr_list)

    unordered_lst[left_most] = lmr_list[1]
    unordered_lst[list_mid] = lmr_list[0]
    unordered_lst[right_most] = lmr_list[2]

    p = unordered_lst[left_most]
    i = left_most; j = right_most + 1

    while True:

        while True:
            i += 1

            if unordered_lst[i] >= p:
                break

        while True:
            j -= 1

            if unordered_lst[j] <= p:
                break
        
        unordered_lst[i], unordered_lst[j] = unordered_lst[j], unordered_lst[i]

        if i >= j:
            break

    unordered_lst[i], unordered_lst[j] = unordered_lst[j], unordered_lst[i]
    unordered_lst[left_most], unordered_lst[j] = unordered_lst[j], unordered_lst[left_most]

    return j


def n_log_n_sort():
    """ This program lets the user implement multiple n log n sorting algorithms
        (namely MergeSort & QuickSort), and lets them measure their running time.
        Allows users to sort lists of size provided by the user.

        post: posts the unordered and unordered lists
    """

    print("Welcome to the n log n Sort Program\n")
    key_pressed = str(input("Would you like to start? (Y/N) "))
    print()

    while key_pressed[0].lower() == "y":
        # user inputs an int for the list size
        lst_size = int(input("Enter the list size: "))
        print()
        
        # user inputs an int for the number of trials
        trial_num = int(input("Enter the number of trials: "))

        # ask user for the sorting algorithm they want to use
        print("\nWhich sort method would you like to use? (Enter 'Merge' or 1) for MergeSort")
        method = str(input(" or 'Quick' or 2 for QuickSort, and press enter): "))
        unordered_lst = []
        num = len(list(str(lst_size))) - 1

        # create a (unordered) list of the size provided by user        
        for i in range(lst_size):
            unordered_lst.append(round(random.random() * (10 ** random.randrange(0,num)), 2))
            
        trial_times = []
        print()
        function = ""

        # choose the sorting algorithm based on user input
        if method[0].lower() == "m" or method == "1":
            function = mergesort

        elif method[0].lower() == "q" or method == "2":
            function = quicksort

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

            print("Now would you like to see how the algorithm performs on double the")
            key_pressed = str(input("input? (Y/N) "))

            if key_pressed[0].lower() == "y":
                unordered_lst = []
                trial_times = []

                for i in range(lst_size * 2):
                    unordered_lst.append(round(random.random() * (10 ** random.randrange(0,num)), 2))
                
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

            try:

                for i in range(trial_num):
                    temp_lst = unordered_lst.copy()
                    time_1 = time.time()
                    sorted_list = function(temp_lst, 0, lst_size - 1)
                    time_2 = time.time()
                    time_taken = time_2 - time_1
                    trial_times.append(time_taken)
                    print("Trial", str(i+1) + ": ", round(time_taken, 2))
                
                total_trial_time = sum(trial_times)
                average_time = total_trial_time/trial_num
            
                print("Total:   ", round(total_trial_time, 2), "\n")
                print("Average:     ", round(average_time, 2))
                print("Average/n**2:", (str(average_time/(lst_size**2)))[:4] + (str(average_time/(lst_size**2)))[-4:])

                print("Now would you like to see how the algorithm performs on double the")
                key_pressed = str(input("input? (Y/N) "))

                if key_pressed[0].lower() == "y":
                    unordered_lst = []
                    trial_times = []

                for i in range(lst_size * 2):
                    unordered_lst.append(round(random.random() * (10 ** random.randrange(0,num)), 2))
                
                for i in range(trial_num):
                    temp_lst = unordered_lst.copy()
                    time_1 = time.time()
                    sorted_list = function(temp_lst, 0, lst_size * 2 - 1)
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

    n_log_n_sort()