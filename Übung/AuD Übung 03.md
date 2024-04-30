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

### 3
insert
```pseudo
\begin{algorithm}
\caption{Insert Element}
\begin{algorithmic}
\Function{insert}{$list$, $element$, $position$}
\State $newNode \gets new(element)$
\If{$position = 0$}
\State $newNode.setNext(list.head)$
\If{$list.head \neq \text{null}$}
\State $list.head.setPrev(newNode)$
\EndIf
\State $list.head \gets newNode$
\Else
\State $current \gets list.head$
\For{$i \gets 1$ \textbf{to} $position-1$}
\State $current \gets current.getNext()$
\EndFor
\State $newNode.setNext(current.getNext())$
\State $newNode.setPrev(current)$
\If{$current.getNext() \neq \text{null}$}
\State $current.getNext().setPrev(newNode)$
\EndIf
\State $current.setNext(newNode)$
\EndIf
\EndFunction
\end{algorithmic}
\end{algorithm}

```

delete
```pseudo
\begin{algorithm}
\caption{Delete Element}
\begin{algorithmic}
\Input nicht leere DLL $list$, index $position$
\Output DLL $list$ without elm at position
\Function{delete}{$list$, $position$}
\If{$position = 0$}
\State $temp \gets list.head$
\State $list.head \gets list.head.getNext()$
\If{$list.head \neq \text{null}$}
\State $list.head.setPrev(\text{null})$
\EndIf
\Else
\State $current \gets list.head$
\For{$i \gets 1$ \textbf{to} $position$}
\State $current \gets current.getNext()$
\EndFor
\State $current.getPrev().setNext(current.getNext())$
\If{$current.getNext() \neq \text{null}$}
\State $current.getNext().setPrev(current.getPrev())$
\EndIf
\EndIf
\EndFunction
\end{algorithmic}
\end{algorithm}
```


concat
```pseudo
\begin{algorithm}
\caption{Concat Lists}
\begin{algorithmic}
\Input DLL $list1$, DLL $list1$
\Output DLL $list$ concatenated $list1$ and $list2$
\Function{concat}{$list1$, $list2$}
\If{$list1.tail \neq \text{null}$}
\State $list1.tail.setNext(list2.head)$
\EndIf
\If{$list2.head \neq \text{null}$}
\State $list2.head.setPrev(list1.tail)$
\EndIf
\State $list1.tail \gets list2.tail$
\return $list1$
\EndFunction
\end{algorithmic}
\end{algorithm}
```
