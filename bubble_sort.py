def bubble_sort(unsorted_list=None):
    """
    Algorithm name : Bubble Sort
    This Method is used for the sorting the list in ascending order
    """
    if unsorted_list:
        for index in range(0, len(unsorted_list)):
            for index2 in range(0, len(unsorted_list) - 1):
                if unsorted_list[index2] > unsorted_list[index2 + 1]:
                    unsorted_list[index2+1], unsorted_list[index2] = unsorted_list[index2], unsorted_list[index2+1]
        print("Sorted List Using Bubble Sort :: ", unsorted_list)


unsorted_list = [7, 8, 5, 2, 4, 6, 3]
bubble_sort(unsorted_list)
