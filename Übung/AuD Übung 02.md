---
tags:
  - Übung
  - Hausaufgabe
  - AuD
  - SoSe_24
createdAt: 2024-04-16
---
[PDF](t02.pdf)
## 3 ADT Pair
### 1.
```
type Pair =
  sorts:
	  T1, T2, Pair
  
  functions:
    create: T1 x T2 -> Pair
    getFirst: Pair -> T1
    getSecond: Pair -> T2
    setFirst: Pair x T1 -> Pair
    setSecond: Pair x T2 -> Pair
end.
```

### 2.
```python
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def set_first(self, value):
        self.first = value
        return self

    def set_second(self, value):
        self.second = value
        return self
```

### 3.
```python
class Pair:  
    def __init__(self, first, second):  
        self.first = first  
        self.second = second  
  
    def get_first(self):  
        return self.first  
  
    def get_second(self):  
        return self.second  
  
    def set_first(self, value):  
        self.first = value  
        return self  
  
    def set_second(self, value):  
        self.second = value  
        return self  

	def empty():
		return Pair(null, null)
  
  
class Sequence:  
    def __init__(self):  
        self.sequence = Pair.empty()
  
    def insert(self, x, p):
		if p == 0:
			return Pair(x, self.sequence)
		return Pair(self.sequence.get_first(), self.insert(self.sequence.get_second(), x, p-1))
		    
  
    def delete(self, p):  
        # Delete the element at position 'p', adjusting the index because lists are 0-indexed.  
        if 0 <= p - 1 < len(self.sequence):  
            del self.sequence[p - 1]  
        else:  
            raise IndexError('Position out of bounds')  
  
  
# Demonstration of usage  
seq = Sequence()  
seq.insert(Pair('a', 1), 1)  # Here we are using a Pair as an element for the sequence.  
seq.insert(Pair('b', 2), 2)  
seq.delete(1)  # Deletes the first element ('a', 1).  
```

## 4 ADT Menge
### 1.
```
type Menge =
	sorts: 
		T, bool, menge
		
	functions:
		empty: -> menge
		isEmpty: menge -> bool
		contains: T x menge -> bool
		add: T x menge -> menge
		remove: T x menge -> menge
end.
```

### 2.
```
T: I(T) Datentyp des Grundtypen
   I(bool) = {true, false}
   I(menge) = P(I(T)) # Potenzmenge
            = \{\{x \in I(T) \mid \text{es gilt } H(x)} \text{ Für eine Bedingung H \}\} \cup \{\emptyset\}
```

## Zusatzaufgabe
### 2.
```python
def getFirstR(xs):
	if xs[0] == ():
		return xs[1]
	return getFirstR(xs[0])
```

### 3.

