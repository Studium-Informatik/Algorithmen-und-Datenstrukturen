---
tags:
  - Übung
  - Präsenz
  - SoSe_24
  - AuD
createdAt: 2024-06-17
---
[PDF](t10.pdf)
## 16 Suchbäume
### 1.
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {$5$}
    child {node[circle, draw] {$2$}
      child {node[circle, draw] {$1$}}
      child {node[circle, draw] {$4$}
        child {node[circle, draw] {$3$}}
        child {node[circle, draw] {}}
      }
    }
    child {node[circle, draw] {$7$}
      child {node[circle, draw] {$6$}}
      child {node[circle, draw] {$8$}
        child {node[circle, draw] {}}
        child {node[circle, draw] {$9$}}
	  }
    };
\end{tikzpicture}
\end{document}
```


Removing $5$
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {$4$}
    child {node[circle, draw] {$2$}
      child {node[circle, draw] {$1$}}
      child {node[circle, draw] {$3$}}
    }
    child {node[circle, draw] {$7$}
      child {node[circle, draw] {$6$}}
      child {node[circle, draw] {$8$}
        child {node[circle, draw] {}}
        child {node[circle, draw] {$9$}}
	  }
    };
\end{tikzpicture}
\end{document}
```

Removing $1$
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {$4$}
    child {node[circle, draw] {$2$}
      child {node[circle, draw] {}}
      child {node[circle, draw] {$3$}}
    }
    child {node[circle, draw] {$7$}
      child {node[circle, draw] {$6$}}
      child {node[circle, draw] {$8$}
        child {node[circle, draw] {}}
        child {node[circle, draw] {$9$}}
	  }
    };
\end{tikzpicture}
\end{document}
```

Removing 5
...

Removing 2
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {$4$}
    child {node[circle, draw] {$3$}}
    child {node[circle, draw] {$7$}
      child {node[circle, draw] {$6$}}
      child {node[circle, draw] {$8$}
        child {node[circle, draw] {}}
        child {node[circle, draw] {$9$}}
	  }
    };
\end{tikzpicture}
\end{document}
```
Removing 7
```tikz
\begin{document}
\begin{tikzpicture}
  [level distance=1.5cm,
   level 1/.style={sibling distance=4.5cm},
   level 2/.style={sibling distance=2.25cm},
   level 3/.style={sibling distance=1.125cm}]
   
  \node[circle, draw] {$4$}
    child {node[circle, draw] {$3$}}
    child {node[circle, draw] {$6$}
      child {node[circle, draw] {}}
      child {node[circle, draw] {$8$}
        child {node[circle, draw] {}}
        child {node[circle, draw] {$9$}}
	  }
    };
\end{tikzpicture}
\end{document}
```


### 2.
```pseudo
\begin{algorithm}
\caption{add}
\begin{algorithmic}
\Input Node $x$, Tree $t$
\Output Tree $t$
  \Function{add}{$x$, $t$}
    \If{t == null}
	    \Return new Node(node)
	    \Comment{create new Tree}
    \EndIf
    \If{t.value == x}
	    \Return t
	    \Comment{if node allready exsists}
    \EndIf
    \If{x < t.value}
	    \State $t.left \gets add(x, t.left)$
	    \Comment{Traverse throu left side}
    \Else
	    \State $t.right \gets add(x, t.right)$
	    \Comment{Traverse throu right side}
    \EndIf
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

