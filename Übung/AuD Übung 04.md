---
tags:
  - Übung
  - Hausaufgabe
  - SoSe_24
  - AuD
  - Präsenz
createdAt: 2024-04-29
---
[PDF](t04.pdf)

## 6
### 1
	a) ja
	b) ja
	c) nein
	d) ja

```tikz
\begin{document}
  \begin{tikzpicture}[domain=1:5] % Default domain for all plots unless overridden
    \draw[thin,color=gray] (0,0) grid (3.9,3.9);
    \draw[->] (-0.2,0) -- (4.2,0) node[right] {};
    \draw[->] (0,-0.2) -- (0,4.2) node[above] {};
    
    % Quadratic function (red line)
    \draw[ultra thick, color=red] plot[domain=0:2] (\x,{\x^2}) node[right] {$B(x) = x^2$};
    
    % Linear function (blue line)
    \draw[ultra thick, color=orange] plot[domain=0:4] (\x,\x) node[above right] {$A(x) = x$};
    
    % Logarithmic function (green line)
    \draw[ultra thick, color=green] plot[domain=1:4] (\x,{log2(\x)}) node[right] {$C(x) = \log_2(x)$};
  \end{tikzpicture}
\end{document}
```

## 7
### Array
- **Empty**: O(1)
- **Length**: O(1)
- **Insert**: O(n)
- **Delete**: O(n)
- **Get**: O(1)
- **Concat**: O(n+m)

### einfach verkettete Liste
- **Empty**: O(1)
- **Length**: O(n)
- **Insert**: O(n)
- **Delete**: O(n)
- **Get**: O(n)
- **Concat**: O(1)

### doppelt verkettete Liste
- **Empty**: O(1)
- **Length**: O(n)
- **Insert**: O(n)
- **Delete**: O(n)
- **Get**: O(n)
- **Concat**: O(1)

### Summary
Arrays:
- schneller Zugriff
- ineffiziente Größenänderungen


Einfach verkettete Liste:
- schnelles einfügen/entfernen
- ineffizienter Zugriff
- benötigt mehr Speicherplatz


Doppelt verkette Liste:
- schnelles einfügen/entfernen
- schneller als Einfach verkettete Liste bei umgekehrter Reihenfolge
- ineffizienter Zugriff
- benötigt mehr Speicherplatz