
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
    