---
tags:
  - Übung
  - Hausaufgabe
  - SoSe_24
  - Präsenz
  - AuD
createdAt: 2024-06-10
---
[PDF](t09.pdf)

## 14 Heapsort
### 1.
#### a)
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {$11$}
    child {node[circle, draw] {$2$}
      child {node[circle, draw] {$19$}
        child {node[circle, draw] {$2$}}
        child {node[circle, draw] {$38$}}
      }
      child {node[circle, draw] {$3$}}
    }
    child {node[circle, draw] {$0$}
      child {node[circle, draw] {$7$}}
      child {node[circle, draw] {$78$}}
    };
\end{tikzpicture}
\end{document}
```

```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] (1) {$11$}
    child {node[circle, draw] (2) {$2$}
      child {node[circle, draw] (3) {$38$}
        child {node[circle, draw] (4) {$2$}}
        child {node[circle, draw] (5) {$19$}}
      }
      child {node[circle, draw] (6) {$3$}}
    }
    child {node[circle, draw] (7) {$0$}
      child {node[circle, draw] (8) {$7$}}
      child {node[circle, draw] (9) {$78$}}
    };
	\draw[<->, color=red] (3) to (5);
\end{tikzpicture}
\end{document}
```

```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] (1) {$11$}
    child {node[circle, draw] (2) {$2$}
      child {node[circle, draw] (3) {$38$}
        child {node[circle, draw] (4) {$2$}}
        child {node[circle, draw] (5) {$19$}}
      }
      child {node[circle, draw] (6) {$3$}}
    }
    child {node[circle, draw] (7) {$78$}
      child {node[circle, draw] (8) {$7$}}
      child {node[circle, draw] (9) {$0$}}
    };
	\draw[<->, color=red] (7) to (9);
\end{tikzpicture}
\end{document}
```

```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] (1) {$11$}
    child {node[circle, draw] (2) {$38$}
      child {node[circle, draw] (3) {$19$}
        child {node[circle, draw] (4) {$2$}}
        child {node[circle, draw] (5) {$2$}}
      }
      child {node[circle, draw] (6) {$3$}}
    }
    child {node[circle, draw] (7) {$78$}
      child {node[circle, draw] (8) {$7$}}
      child {node[circle, draw] (9) {$0$}}
    };
	\draw[<->, color=red] (2) to (3);
	\draw[<->, color=red] (3) to (5);
\end{tikzpicture}
\end{document}
```


```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] (1) {$78$}
    child {node[circle, draw] (2) {$38$}
      child {node[circle, draw] (3) {$19$}
        child {node[circle, draw] (4) {$2$}}
        child {node[circle, draw] (5) {$2$}}
      }
      child {node[circle, draw] (6) {$3$}}
    }
    child {node[circle, draw] (7) {$11$}
      child {node[circle, draw] (8) {$7$}}
      child {node[circle, draw] (9) {$0$}}
    };
	\draw[<->, color=red] (1) to (7);
\end{tikzpicture}
\end{document}
```

#### b)
```css
[11, 2, 0, 19, 3, 7, 78, 2, 38]
```

## 15 Hashing
### 1.

| 0   | 100                                      |
| --- | ---------------------------------------- |
| 1   | 11                                       |
| 2   | 32                                       |
| 3   | 128 (da 8 schon belegt, linear Sondiert) |
| 4   |                                          |
| 5   |                                          |
| 6   |                                          |
| 7   |                                          |
| 8   | 48                                       |
| 9   | 79                                       |

### 2.
Primzahlen, da 
- Weniger Gemeinsame Teiler
- nicht so häufige Wiederholungen

Sei $n$ die Anzahl der Einträge und $m$ die Tabellengröße, dann:
mit $k\in\mathbb{R}\mid 1.5\leq k\leq 2$
$m\geq \text{nächste Primzahl} \geq k\cdot n$

### 3.
#### a)

| Hash | Key                                                           |
| ---- | ------------------------------------------------------------- |
| 0    | Franz                                                         |
| 1    |                                                               |
| 2    |                                                               |
| 3    | Susi                                                          |
| 4    |                                                               |
| 5    | Ali -> Alfred -> Arno -> Alice -> Kurt -> Alex -> Angy -> Alf |
| 6    | Babsi -> Benno -> Bine                                        |
| 7    | Max                                                           |
| 8    |                                                               |
| 9    |                                                               |

```run-python
names = [ "Ali", "Babsi", "Alfred", "Arno", "Alice", "Benno", "Kurt", "Alex", "Angy", "Bine", "Max", "Franz", "Susi", "Alf"]

def calcHash(name):
	return ord(name[0])

def main():
	print(f"{'Name':<10} {'Hash':<10} {'Mod 10':<10}")
	for n in names:
		name_hash = calcHash(n)
		mod_10 = name_hash % 10

		print(f"{n:<10} {name_hash:<10} {mod_10:<10}")


if __name__ == "__main__":
	for i in names:
		print(f"{i}: {ord(i[0])}, {ord(i[-1])}")
	main()
```

#### b)

| Hash | Key                           |
| ---- | ----------------------------- |
| 0    | Ali                           |
| 1    | Babsi -> Alex                 |
| 2    | Alfred -> Angy                |
| 3    | Alice -> Max -> Franz -> Susi |
| 4    | Kurt -> Bine -> Alf           |
| 5    |                               |
| 6    | Arno                          |
| 7    | Benno                         |
| 8    |                               |
| 9    |                               |

```run-python
names = [ "Ali", "Babsi", "Alfred", "Arno", "Alice", "Benno", "Kurt", "Alex", "Angy", "Bine", "Max", "Franz", "Susi", "Alf"]

def calcHash(name):
	return (ord(name[0]) % 5), (ord(name[-1]) % 7)

def main():
	print(f"{'Name':<10} {'Hash':<20}")
	for n in names:
		first_hash, second_hash = calcHash(n)

		print(f"{n:<10} {first_hash:<10} + {second_hash:<10} = {first_hash + second_hash:<10}")


if __name__ == "__main__":
	main()
```


### 4.
#### a)
Summe der Suchschritte = $1 + 1 + 2 + 3 + 4 + 2 + 5 + 6 + 7 + 3 + 1 + 1 + 1 + 8 = 45$

#### b)
Summe der Suchschritte = $1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 2 + 2 + 3 + 4 + 3 = 25$

### 5.
Pro:
- Bessere Verteilung
- Bessere Effizienz bei der suchen

Contra:
- Höherer Berechnungsaufwand
- Mehr Speicherbedarf