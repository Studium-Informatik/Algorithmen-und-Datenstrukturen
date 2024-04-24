---
tags:
  - Übung
  - AuD
  - Hausaufgabe
  - SoSe_24
createdAt: 2024-04-23
---
[PDF](t03.pdf)
## 5
### 1
#### a)
```pseudo
\begin{algorithm}
\caption{delete Array}
\begin{algorithmic}
\Input Sequence $S$, index $p$
\Output Sequence $S$
  \Function{delete}{$S$, $p$}
    \While{$p <$ len($S$) - 1}
	    \State $setContent(\alpha_S(p), content(\alpha_S(p)+size(T)))$
		 \State $p \gets p + 1$
    \EndWhile
    \State $len_S \gets len_S - 1$
    \State \textbf{return} $S$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

```pseudo
\begin{algorithm}
\caption{get Array}
\begin{algorithmic}
\Input Sequence $S$, index $p$
\Output Element $e$
  \Function{get}{$S$, $p$}
    \State \textbf{return} $content (\alpha_S(p))$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

```pseudo
\begin{algorithm}
\caption{concat Array}
\begin{algorithmic}
\Input Sequence $S$, Sequence $L$
\Output Sequence $res$
  \Function{concat}{$S$, $L$}
	\State $a \gets \textit{eine geeignete Adresse}$
	\State $res \gets empty(a)$
	\State $len_{res} \gets len_S + len_L$
	\State $c \gets 0$
    \ForAll{$j$ \textbf{in} $S$}
	    \State $setContent(\alpha_S(c), j)$
	    \State $c \gets c + 1$
    \EndFor
    
    \ForAll{$j$ \textbf{in} $L$}
	    \State $setContent(\alpha_L(c), j)$
	    \State $c \gets c + 1$
    \EndFor
    \State \textbf{return} $res$
  \EndFunction
\end{algorithmic}
\end{algorithm}
```

### 2
```
type D-listElement =
	sorts: 
		T, p, le
		
	functions:
		new: T -> le
		getValue: le -> T
		setValue: le x T -> le
		getNext: le -> p
		setNext: le x p -> le
		getPrev: le -> p
		setPrev: le x p -> le
end.
```

```
T: I(T) Datentyp des Grundtypen
   I(p) = {x|x ∈ allokierter Speicher}
   I(le) = I(T) x I(p) x I(p)
```




???
```
type ListElement = 
	sorts:
		T, p, le 
	
	functions:
		new: T -> le 
		getValue: le -> T 
		setValue: le x T -> le 
		getNext: le -> p 
		setNext: le x p -> le 
end.


type D-listElement extends ListElement =		
	functions:
		getPrev: le -> p
		setPrev: le x p -> le
end.
```
### 3