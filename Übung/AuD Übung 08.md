---
tags:
  - Übung
  - Präsenz
  - SoSe_24
  - AuD
createdAt: 2024-06-02
---
[PDF](t08.pdf)

## 1.
### a)
Minimale Knoten
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {}
    child {node[circle, draw] {}
      child {node[circle, draw] {}
        child {node[circle, draw] {}}
      }
    };
\end{tikzpicture}
\end{document}
```
4 Knoten
### b)
Maximale Knoten
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {}
    child {node[circle, draw] {}
      child {node[circle, draw] {}
        child {node[circle, draw] {}}
        child {node[circle, draw] {}}
      }
      child {node[circle, draw] {}
        child {node[circle, draw] {}}
        child {node[circle, draw] {}}
      }
    }
    child {node[circle, draw] {}
      child {node[circle, draw] {}
        child {node[circle, draw] {}}
        child {node[circle, draw] {}}
      }
      child {node[circle, draw] {}
        child {node[circle, draw] {}}
        child {node[circle, draw] {}}
      }
    };
\end{tikzpicture}
\end{document}
```
$T=\text{Tiefe}=3$
$$\lvert V \rvert = \sum_{i=0}^{T}2^i=\frac{1-2^{3+1}}{1-2}=\frac{1-2^4}{-1}=15$$
### c)
Minimale Blätter
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {}
    child {node[circle, draw] {}
      child {node[circle, draw] {}
        child {node[circle, fill=green, draw] {}}
      }
    };
\end{tikzpicture}
\end{document}
```
### d)
Maximale Innere Knoten

```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, fill=green, draw] {}
    child {node[circle, fill=green, draw] {}
      child {node[circle, fill=green, draw] {}
        child {node[circle, draw] {}}
        child {node[circle, draw] {}}
      }
      child {node[circle, fill=green, draw] {}
        child {node[circle, draw] {}}
        child {node[circle, draw] {}}
      }
    }
    child {node[circle, fill=green, draw] {}
      child {node[circle, fill=green, draw] {}
        child {node[circle, draw] {}}
        child {node[circle, draw] {}}
      }
      child {node[circle, fill=green, draw] {}
        child {node[circle, draw] {}}
        child {node[circle, draw] {}}
      }
    };
\end{tikzpicture}
\end{document}
```

## 2.
### a)
```tikz
\begin{document}
\begin{tikzpicture}[node distance={15mm}, main/.style = {draw, circle}] 
\node[main] (a) {$a$}; 
\node[main] (b) [right of=a] {$b$};
\node[main] (c) [below of=b] {$c$};
\node[main] (d) [left of=c] {$d$};

\draw (a) -- (b);
\draw (a) -- (c);
\draw (a) -- (d);
\draw (b) -- (c);
\draw (b) -- (d);
\draw (c) -- (d);
\end{tikzpicture}
\end{document}
```


| $G$ | $a$ | $b$ | $c$ | $d$ |
| --- | --- | --- | --- | --- |
| $a$ | 0   | 1   | 1   | 1   |
| $b$ | 1   | 0   | 1   | 1   |
| $c$ | 1   | 1   | 0   | 1   |
| $d$ | 1   | 1   | 1   | 0   |
### b)
```tikz
\begin{document}
\begin{tikzpicture}[node distance={15mm}, main/.style = {draw, circle}] 
\node[main] (a) {$a$}; 
\node[main] (b) [right of=a] {$b$};
\node[main] (c) [below of=b] {$c$};
\node[main] (d) [left of=c] {$d$};

\draw (a) -- (b);
\draw (a) -- (c);
\draw (a) -- (d);
\end{tikzpicture}
\end{document}
```


```tikz
\begin{document}
\begin{tikzpicture}[node distance={15mm}, main/.style = {draw, circle}] 
\node[main] (a) {$a$}; 
\node[main] (b) [right of=a] {$b$};
\node[main] (c) [below of=b] {$c$};
\node[main] (d) [left of=c] {$d$};

\draw (a) -- (b);
\draw (b) -- (d);
\draw (d) -- (c);
\end{tikzpicture}
\end{document}
```


```tikz
\begin{document}
\begin{tikzpicture}[node distance={15mm}, main/.style = {draw, circle}] 
\node[main] (a) {$a$}; 
\node[main] (b) [right of=a] {$b$};
\node[main] (c) [below of=b] {$c$};
\node[main] (d) [left of=c] {$d$};

\draw (a) -- (b);
\draw (a) -- (d);
\draw (b) -- (c);
\end{tikzpicture}
\end{document}
```


```tikz
\begin{document}
\begin{tikzpicture}[node distance={15mm}, main/.style = {draw, circle}] 
\node[main] (a) {$a$}; 
\node[main] (b) [right of=a] {$b$};
\node[main] (c) [below of=b] {$c$};
\node[main] (d) [left of=c] {$d$};

\draw (a) -- (c);
\draw (b) -- (d);
\draw (c) -- (d);
\end{tikzpicture}
\end{document}
```

## 3.
### a)

### b)
Maximale Anzahl an Knoten mit Tiefe $T$: $$\lvert V \rvert = \sum_{i=0}^{T}2^i=\frac{1-2^{T+1}}{1-2}=\frac{1-2^{T+1}}{-1}$$

**Induktionsanfang**:
Für $d=0$, Baum besteht nur aus Wurzel

$2^{d+1}-1=2^1-1=2-1=1$ 
gilt für $d=0$

**Induktionsvoraussetzung**:
Angenommen die Gleichung gilt für $d=k$
$2^{d+1}-1$

**Induktionsschritt**:
für $d=k+1$

$$\displaylines{
2^{d+1+1}-1&=&2\cdot2^{d+1}-1\\
2\cdot2^{d+1}-1&\leq&\frac{1-2^{d+1+1}}{-1}\\
&\leq&-1+2^{d+1+1}\\
2\cdot 2^{d+1}-1&=&2\cdot 2^{d+1}-1
}$$


$$\displaylines{
\sum_{i=0}^{d-1}2^i=\frac{1-2^d}{-1}=2^d-1\\
2^d
}$$