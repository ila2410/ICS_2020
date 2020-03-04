# SIMPLE BINARY SEARCH ALGORITHM
# OBJECTIVE : FIND A NUMBER FROM A SORTED LIST OF NUMBERS GIVEN BY USER, TELL THEM
# IF IT EXISTS, AND FIGURE OUT IN WHICH INDEX IT IS

# using iterative implementation (I tried to use recursive, but there are still some
# bugs hanging around)
def binarySearch(item_list, item):
    low = 0  # determine the first index
    high = len(item_list) - 1  # find out the last index
    while low <= high:
        mid = low + (high - low) // 2  # determine the middle index
        if item_list[mid] == item:
            return mid
        elif item_list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# asking user to input a set of sorted numbers
item_list = input("Give a sorted list of numbers: ").split()
item_list = [int(x) for x in item_list]

# asking user to give which number they want to know whether it exists or not,
# and if it exists, in which index it is
item = int(input("What are the numbers you're searching for? -> "))

# calling the function
item_index = binarySearch(item_list, item)
if item_index < 0:
    print("Your item was not found!")
else:
    print(
        "Your item was found at index {}! (Remember, index starts from 0)".format(
            item_index
        )
    )

# using recursive (can't quite figure it out what's wrong with this :/)
# def binarySearchRecursive(item_list, item):
#     def recursive(first, last):
#         mid = first + (last - first) // 2
#         if first > last:
#             return None
#         elif item_list[mid] < item:
#             return recursive(mid + 1, last)
#         elif item_list[mid > item]:
#             return recursive(first, mid - 1)
#         else:
#             return mid

#     return recursive(0, len(item_list) - 1)
