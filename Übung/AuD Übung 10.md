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
        \Return new Node(x)
        \Comment{create new Tree with the value x}
    \EndIf
    \If{t.value == x}
        \Return False
        \Comment{if node already exists, return False}
    \EndIf
    \If{x < t.value}
        \If{t.left == null}
            \State $t.left \gets new Node(x)$
            \State $t.left.parent \gets t$
            \Return True
            \Comment{add new node as left child}
        \Else
            \Return add(x, t.left)
            \Comment{traverse through left side}
        \EndIf
    \Else
        \If{t.right == null}
            \State $t.right \gets new Node(x)$
            \State $t.right.parent \gets t$
            \Return True
            \Comment{add new node as right child}
        \Else
            \Return add(x, t.right)
            \Comment{traverse through right side}
        \EndIf
    \EndIf
    \Return False
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

### 3.
#### rec
```pseudo
\begin{algorithm}
\caption{remove}
\begin{algorithmic}
\Input Wert $x$, Baum $t$
\Output Baum $t$
  \Function{remove}{$x$, $t$}
    \If{$t == null$}
        \Return null
        \Comment{Knoten nicht gefunden}
    \EndIf
    
    \If{$x < content(t)$}
        \State $setLeft(t, remove(x, left(t)))$
    \ElsIf{$x > content(t)$}
        \State $setRight(t, remove(x, right(t)))$
    \Else
        \Comment{Knoten gefunden, Bearbeitung je nach Fall}
        
        \If{$left(t) == null$}
            \Return right(t)
            \Comment{Fall 1: Knoten hat nur ein rechtes Kind oder ist ein Blatt}
        \ElsIf{$right(t) == null$}
            \Return left(t)
            \Comment{Fall 1: Knoten hat nur ein linkes Kind oder ist ein Blatt}
        \Else
            \Comment{Fall 3: Knoten hat zwei Kinder}
            \State $successor \gets findMin(right(t))$
            \State $setContent(t, content(successor))$
            \State $setRight(t, remove(content(successor), right(t)))$
        \EndIf
    \EndIf

    \Return t
  \EndFunction

  \Function{findMin}{$t$}
    \While{$left(t) \neq null$}
        \State $t \gets left(t)$
    \EndWhile
    \Return t
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

#### itter
```pseudo
\begin{algorithm}
\caption{remove}
\begin{algorithmic}
\Input Wert $x$, Baum $t$
\Output Boolean
  \Function{remove}{$x$, $t$}
    \State $current \gets t$
    \State $parent \gets null$
    \State $isLeftChild \gets false$

    \While{$current \neq null$ \textbf{and} $content(current) \neq x$}
        \State $parent \gets current$
        \If{$x < content(current)$}
            \State $isLeftChild \gets true$
            \State $current \gets left(content(current))$
        \Else
            \State $isLeftChild \gets false$
            \State $current \gets right(content(current))$
        \EndIf
    \EndWhile

    \If{$current == null$}
        \Return False
        \Comment{Knoten nicht gefunden}
    \EndIf

    \If{$left(content(current)) == null$ \textbf{and} $right(content(current)) == null$}
        \Comment{Fall 1: Knoten ist ein Blatt}
        \If{$current == t$}
            \Return False
            \Comment{Die Wurzel wird nie entfernt}
        \ElsIf{$isLeftChild$}
            \State $setLeft(parent, null)$
        \Else
            \State $setRight(parent, null)$
        \EndIf
    \ElsIf{$right(content(current)) == null$}
        \Comment{Fall 2: Knoten hat nur ein linkes Kind}
        \If{$current == t$}
            \Return False
            \Comment{Die Wurzel wird nie entfernt}
        \ElsIf{$isLeftChild$}
            \State $setLeft(parent, adress(left(content(current))))$
        \Else
            \State $setRight(parent, adress(left(content(current))))$
        \EndIf
        \State $setParent(left(content(current)), address(parent))$
    \ElsIf{$left(content(current)) == null$}
        \Comment{Fall 2: Knoten hat nur ein rechtes Kind}
        \If{$current == t$}
            \Return False
            \Comment{Die Wurzel wird nie entfernt}
        \ElsIf{$isLeftChild$}
            \State $setLeft(parent, address(right(content(current))))$
        \Else
            \State $setRight(parent, address(right(content(current))))$
        \EndIf
        \State $setParent(right(content(current)), address(parent))$
    \Else
        \Comment{Fall 3: Knoten hat zwei Kinder}
        \State $successor \gets right(content(current))$
        \State $successorParent \gets current$
        \While{$left(content(successor)) \neq null$}
            \State $successorParent \gets successor$
            \State $successor \gets left(content(successor))$
        \EndWhile

        \State $content(current) \gets content(successor)$
        \If{$left(successorParent) == successor$}
            \State $left(successorParent) \gets right(content(successor))$
        \Else
            \State $setRight(successorParent, address(right(content(successor))))$
        \EndIf
        \If{$right(content(successor)) \neq null$}
            \State $setParent(right(content(successor)), address(successorParent))$
        \EndIf
    \EndIf

    \Return True
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

