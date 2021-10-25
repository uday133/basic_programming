def insertion_sort(unsorted_list=None):
    """
        Algorithm name : Insertion Sort
        This Method is used for the sorting the list in ascending order
        """
    if unsorted_list:
        for index in range(1, len(unsorted_list)):
            key = unsorted_list[index]
            for index2 in range(index - 1, -1, -1):
                if key < unsorted_list[index2]:
                    previous_element = unsorted_list[index2 + 1]
                    unsorted_list[index2 + 1] = unsorted_list[index2]
                    unsorted_list[index2] = previous_element
                else:
                    break
        print("Sorted List Using Insertion Sort :: ", unsorted_list)

unsorted_list = [7, 8, 5, 2, 4, 6, 3]
insertion_sort(unsorted_list)
