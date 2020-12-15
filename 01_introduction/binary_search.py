import math
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = math.floor((low + high)/2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def main():
    my_list = [1, 3, 5, 7, 9, 21]
    print(binary_search(my_list, 9))
    print(binary_search(my_list, -1))

if __name__ == "__main__":
    main()