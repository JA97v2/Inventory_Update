curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]


def sortArray(item: list) -> list:      
    return item[1]                      

def updateInventory(arr1: list, arr2: list) -> list:    
    index = None                                        
    for i in range(len(arr2)):                          
        for j in range(len(arr1)):                      
            if arr1[j][1] == arr2[i][1]:                
                index = (i, j)                          
                break                                   
        if index == None:                           
            arr1.append(arr2[i])                    
            index = None                            
        else:                                       
            arr1[index[1]][0] += arr2[index[0]][0]  
            index = None                            
    arr1.sort(key=sortArray)                            
    return arr1

print(updateInventory(curInv, newInv))                                         