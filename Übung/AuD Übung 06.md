---
tags:
  - Übung
  - Präsenz
  - SoSe_24
  - AuD
createdAt:
---
[PDF](t06.pdf)

## 10
### 1.
```run-python
def find_maximum(arr):
    # Base case: if the array contains only one element, return that element
    if len(arr) == 1:
        return arr[0]
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively find the maximum in both halves
    left_max = find_maximum(left_half)
    right_max = find_maximum(right_half)
    
    # Conquer: return the maximum of the two halves
    return max(left_max, right_max)

# Test the function with the given input
L = [-3, 5, 1, -6, 10, 4, -7, 8]
print(find_maximum(L))  # Output should be 10
```

### 3.
#### a)
