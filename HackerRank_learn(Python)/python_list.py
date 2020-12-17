"""
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""

def insertList(i, e, lista):
    lista.insert(i, e)

def printList(lista):
    print(lista)

def removeList(e, lista):
    lista.remove(e)

def appendList(e, lista):
    lista.append(e)

def sortList(lista):
    lista.sort()

def popList(lista):
    lista.pop()

def reverseList(lista):
    lista.reverse()


if __name__ == '__main__':
    N = int(input())

    arr = []
    
    for i in range(N):
        #action, i, e = input().split()
        x = list(map(str, input().split()))
        action = x[0]
        if len(x) == 3:
            i = int(x[1])
            e = int(x[2])
        elif len(x) == 2:
            e = int(x[1])

        if action == "insert":
            
            insertList(i, e, arr)

        elif action == "print":
        
            printList(arr)

        elif action == "remove":
            
            removeList(e, arr)

        elif action == "append":

            appendList(e, arr)

        elif action == "sort":

            sortList(arr)

        elif action == "pop":

            popList(arr)

        elif action == "reverse":

            reverseList(arr)

        else:
            
            pass

