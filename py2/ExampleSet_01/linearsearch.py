'''
Linear Search
The linear search is used to find an item in a list. The items do not have to be in order. To search for an item, start at the beginning of the list and continue searching until either the end of the list is reached or the item is found.

The algorithm is as follows (given a list called 'List' and looking for an item called 'item'):

    position <- 0
    found <- False
    while position < len(List) and not found:
        if List[position] = item:
            found <- True
        position <- position + 1
'''
numberofelement = int(raw_input("How many element to process: "))
arr = []

for n in range(numberofelement):
    print (n)
    arr.append(int(raw_input("Enter number: ")))
    
searchelement = int(raw_input("Enter the number you want to search: "))

def l_search(arr, element):
    for i in range(0,len(arr)):
        if arr[i] == element:
            return i
    else:
        return -1

re = l_search(arr, searchelement)

if ( re == -1):
    print ("The element not available in the list.")
elif (re >= 0):
    print ("The element found at: %s th position." % re) 
    