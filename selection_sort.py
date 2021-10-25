def selection_sort(unsorted_list=None):
    """
    Algorithm name : Selection Sort
    This Method is used for the sorting the list in ascending order
    """
    if unsorted_list:
        for index in range(0, len(unsorted_list)):
            for index2 in range(index + 1, len(unsorted_list)):
                if unsorted_list[index] > unsorted_list[index2]:
                    unsorted_list[index2], unsorted_list[index] = unsorted_list[index], unsorted_list[index2]
        print("Sorted List Using Selection Sort :: ", unsorted_list)

unsorted_list = [7, 8, 5, 2, 4, 6, 3]
selection_sort(unsorted_list)
