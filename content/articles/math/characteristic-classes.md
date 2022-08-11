title: Construction of Chern classes
slug: chern-classes
tags: differential-geometry, vector-bundles
category: mathematics
date: 20-04-2018

## Characteristic classes

Given a manifold $M$, one way to study vector bundles over $M$ is to use the theory of
characteristic classes. A characteristic class is a way of assigning to each vector bundle over $M$
an element of the cohomology ring $H^{\ast}(M, G)$. This assignment is not just any arbitrary
assignment; it has to satisfy a *naturality* condition. If $(F, N, \pi_2)$ is a vector
bundle, $f: M \to N$ is a smooth map, (E, M, \pi_1) is the [pullback bundle](https://en.wikipedia.org/wiki/Pullback_bundle),
and $c(E)$ and $c(F)$ are the cohomology classes assigned to $E$ and $F$ by the characteristic class
$c$, then the pullback of $c(F)$ along the map $f$ is $c(E)$.
\begin{align*}
c(E) = f^{\ast}(c(F))
\end{align*}
The naturality condition is what makes characteristic classes so useful: it tells us that
characteristic classes are an invariant of vector bundles over a manifold. If two vector
bundles are isomorphic, they'll get assigned the same characteristic class.

The first step in studying characteristic classes is to construct interesting examples of them.
Its definition is certainly not of much help in actually constructing any examples. In fact,
constructing characteristic classes is not entirely trivial, and requires some work. We'll look
at one way of constructing characteristic classes, called Chern classes. This construction
is quite non-trivial, and requires the use of differential geometric machinery. The advantage of this
construction however, is that it gives an explicit way of constructing characteristic classes over
a lot of familiar vector bundles.

## Connections on vector bundles

Given a rank $k$ vector bundle $(E, M)$, a connection on the vector bundle is a bundle map $\nabla$ from
$E$ to $E \otimes T^{\ast}M$ which satisfies the following condition for all smooth real-valued functions $f$.
\begin{align*}
\nabla(fv) = v \otimes df + f (\nabla v)
\end{align*}
If we pick local coordinates and a trivialization around some point in $M$, then the connection
$\nabla$ can be described by a $k \times k$ matrix of $1$-forms, which we'll denote
$A$, where the $i$<sup>th</sup> column
denotes what $\nabla e_i$ goes to, where $\{e_i\}$ is the local frame for the vector bundle.
The matrix $A$ is often called a [connection form](https://en.wikipedia.org/wiki/Connection_form).
Using the matrix $A$, we can construct another matrix, this one consisting of $2$-forms, which we'll call
the curvature form[^1].
\begin{align*}
\Omega = dA + A \wedge A
\end{align*}
The curvature form will be the key tool we'll use to construct the Chern classes.

## Constructing globally defined forms using curvature

The nice thing about the curvature form is that it transforms in a particularly
nice manner when one changes the trivialization for the vector bundle. If $\Omega$
is the curvature matrix in the old trivialization, and the new trivialization is given
by multiplying by an invertible matrix $g$, then in the new trivialization, the curvature
matrix is given by $g\Omega g^{-1}$.

Consider the trace of the curvature matrix defined on some open set. The trace will be
a locally defined $2$-form. Now recall that for any matrix $M$, $\mathrm{tr}(M) = \mathrm{tr}(gMg^{-1})$.
This means that we can defined a "trace" of the curvature form globally (using a partition of unity argument),
and this gives us a globally defined $2$-form. In fact, this can be done for any homogeneous
polynomial in the entries of a matrix
which is conjugation invariant, e.g. the determinant. Doing this for the determinant will give
us a globally defined $2k$-form. We now have a way of constructing globally defined forms
using the curvature form.

Let's take a pause here to recall our goal. We want to associate to each vector bundle over $M$
an element of $H^{\ast}(M)$. What we have done so far is to associate to each vector bundle $E$
and a choice of connection $\nabla$ on that bundle a collection of differential forms. If we manage to show
that the differential form is actually closed, we'll have an assignment of $(E, \nabla)$ to an element
of $H^{\ast}_{DR}(M)$. Furthermore, if we show that the assignment to the cohomology class
is independent of which connection we pick, we'll have constructed a characteristic class. In the following
sections, we'll do both of the mentioned things, i.e. show that the globally defined forms are closed,
and their cohomology class is independent of the connection chosen.

### The globally defined forms are closed

To show that the globally defined forms are closed, we'll need a systematic way of taking
their exterior derivative. The first step in that direction would be to simplify the expression
for the connection form $A$ by picking a nice trivialization. In fact, we can pick a trivialization
in which the connection matrix $A$ is $0$ at a point. The proof of this fact is outlined in these
[notes](http://www.math.iisc.ac.in/~vamsipingali/6Feb2018.pdf) (and some formulae used are derived in these
[notes](http://www.math.iisc.ac.in/~vamsipingali/1Feb2018.pdf)). We'll call this trivialization a *normal trivialization*.

This result already tells us that the $2$-form defined by taking the trace of the curvature is
closed. Pick a normal trivialization around $p$; this makes $A$ vanish at $p$. Then at that point, the curvature
matrix is just $dA$. The exterior derivative of the trace of this is the same as the trace of $d^2A$
(because the trace is a homogeneous degree $1$ polynomial in the entries of the matrix),
which is $0$.

To extend this idea to homogeneous polynomials of higher degrees, we need some way "linearizing" them,
so that we can take their exterior derivative easily. We do this by *polarizing* them. The polarization
of a degree $j$ homogeneous polynomial $f$ in the entries of the matrix is a function $\phi$ that takes $j$
matrix arguments, and outputs an element of the algebra over which the matrices are defined. The function $\phi$
is linear in each of its arguments, is symmetric in the order of its arguments, and is conjugation invariant, i.e.
it satisfies the following identity for all invertible matrices $g$.
\begin{align*}
\phi(A_1, \ldots , A_j) = \phi(gA_1g^{-1}, \ldots , gA_jg^{-1})
\end{align*}
Furthermore, $\phi$ must also satisfy the following polarization identity for all matrices $A$.
\begin{align*}
\phi(A, \ldots , A) = f(A)
\end{align*}
This last equality is why $\phi$ is called the polarization of $f$.
Constructing the polarization of a homogeneous degree $j$ polynomial isn't too hard.
The first step is to just construct a multilinear function that satisfies the polarization
identity. One does that by taking each monomial in the expression for $f$, and replacing
the $i$<sup>th</sup> factor by the corresponding factor in the $i$<sup>th</sup> argument.

This is best illustrated by a simple example. Suppose we are working with $2 \times 2$ matrices,
and the polynomial we want to polarize is the determinant polynomial. Its expression is given
in the following manner.
\begin{align*}
f(\{a_{ij}\}) = a_{11}a_{22} - a_{12}a_{21}
\end{align*}
Its polarization $\phi$ must have two arguments. We'll denote the entries of the first
argument by superscript $1$ and the second by superscript $2$. Then the first step would
be two write the following expression.
\begin{align*}
a^1_{11}a^2_{22} - a^1_{12}a^2_{21}
\end{align*}

Whatever we get in the previous step certainly is multilinear in the arguments and satisfies the
polarization identity. The next step is to symmetrize it. That can be easily done by taking
all permutations of the arguments and taking an average over them. This continues to satisfy
the polarization identity and is multilinear and symmetric. The only thing to do now is to make
$\phi$ conjugation invariant. But as it turns out, $\phi$ is already conjugation invariant,
because $f$ is conjugation invariant. The proof of this fact is a little tricky,
and is outlined in the next few paragraphs.

**Lemma.** If $f$ is a conjugation invariant degree $j$ polynomial in the entries 
of a matrix, and $\phi$ is its symmetric and multilinear polarization, then $\phi$
is also conjugation invariant (which we'll also call basis invariant).

**Proof:**     We'll prove this lemma by inducting on the number of distinct matrices in the arguments of
    $\phi$. Observe that $\phi$ can have at most $j$ distinct matrices as arguments. What we'll show
    is that the following equality holds, when $\left\{ A_1, A_2, \ldots, A_j\right\}$ contain at
    most $m$ distinct matrices for each $1 \leq m \leq j$.
    \begin{align*}
      \phi\left(gA_1g^{-1}, gA_2g^{-1}, \ldots, gA_jg^{-1}\right)  = \phi\left(A_1, A_2, \ldots, A_j\right)
    \end{align*}
    Let's start with the base case of $m=1$. This follows from the hypothesis that $f$ is basis
    invariant, since $\phi$ with all identical arguments is just the function $f$. Now suppose we
    have shown the result for some $m < j$. We now need to show $\phi$ is basis invariant when
    supplied with at most $m+1$ different arguments. Pick any set of $m+1$ matrices
    $\left\{A_1, A_2, \ldots, A_{m+1}\right\}$, and any invertible matrix $g$. We want to show the
    following equality (with some of arguments repeated possibly, if $m+1 < j$).
    \begin{align*}
      \phi\left(gA_1g^{-1}, gA_2g^{-1}, \ldots, gA_{m+1}g^{-1}\right)  = \phi\left(A_1, A_2, \ldots, A_{m+1}\right)
    \end{align*}
    Consider the following expression, for $t \in \mathbb{C}$.
    \begin{align}
      \phi\left( A_1 + tA_{m+1}, A_1 + tA_{m+1}, \ldots, A_1 + tA_{m+1}, A_2, \ldots, A_m \right) \label{eq:1}
    \end{align}
    Here, $A_1 + tA_{m+1}$ is repeated $j -m$ times. Since expression $\ref{eq:1}$ has at most $m$
    distinct arguments, we can use the induction hypothesis to conclude that expression \ref{eq:1}
    would be the same if we conjugated all arguments with $g$. In fact, expression \ref{eq:1} can be
    expanded out to be written as a univariate polynomial $P$ in $t$, with coefficients in $R$. The
    coefficient $c_j(P)$ of $t^j$ in the polynomial is the following.
    \begin{align*}
      c_j(P) = \binom{j-m}{j} \phi\left( A_1, \ldots, A_1, A_{m+1}, \ldots, A_{m+1}, A_2, \ldots, A_m\right) 
    \end{align*}
    Here $A_1$ is repeated $j-m - j$ times, and $A_{m+1}$ repeated $j$ times. Similarly, consider
    the polynomial $P'$ one gets by expanding out the conjugated version of expression
    \ref{eq:1}. The coefficient $c_j(P')$ of $t^j$ in $P'$ is given by a similar expression.
    \begin{align*}
      c_j(P') = \binom{j-m}{j}
      \phi\left( gA_1g^{-1}, \ldots, gA_1g^{-1}
      , gA_{m+1}g^{-1}, \ldots, gA_{m+1}g^{-1}, gA_2g^{-1}, \ldots, gA_mg^{-1}\right) 
    \end{align*}
    Recall again that by the induction hypothesis, the polynomials $P$ and $P'$ are the same. Which
    means their coefficients must also be the same. But the coefficients being equal means that even
    if $\phi$ has $m+1$ different entries, it's still conjugation invariant, hence proving the
    induction step, and the lemma. $\blacksquare$

The upshot of proving that every homogeneous polynomial can be polarized is that now we
have an easy way of taking exterior derivative. If $f$ is the degree $j$ homogeneous polynomial, and $\phi$ its
polarization, then the exterior derivative of $f(\Omega)$ is given by the following expression.
\begin{align*}
df(\Omega) = j \cdot \phi(d\Omega, \Omega, \Omega, \ldots , \Omega)
\end{align*}
Using normal coordinates, and exploiting the multilinearity of $\phi$, we see that every global
$2$-form obtained from the curvature form by applying the polynomial $f$ is actually closed,
and hence an element of the cohomology ring. We thus have a way associating a vector bundle
and a connection on it to an element in the cohomology ring. The next step is to show
this assignment is independent of the connection chosen.

### Independence from choice of connection

Given a homogeneous polynomial $f$, and two connections $\nabla_0$ and $\nabla_1$ on the vector
bundle, we need to show the associated forms $f(\Omega_0)$ and $f(\Omega_1)$ differ by an exact
form. Consider the form $\eta_t = f((1-t)\Omega_0 + (t)\Omega_1)$. This defines a path in the
space of forms between f(\Omega_0) and $f(\Omega_1)$. If we show $\frac{d}{dt} \eta_t$ is exact,
that will show what we wanted to prove. In fact, the exterior derivative of the following
form is precisely $\frac{d}{dt}\eta_t$.
\begin{align*}
j \phi \left( A_1 - A_0, \Omega_t, \Omega_t, \ldots, \Omega_t \right)
\end{align*}
Here $A_i$ is the connection form of the connection $\nabla_i$, and $\Omega_t$ the curvature
form of the connection $\nabla_t$. If one takes the exterior derivative of this expression, using
the normal coordinates, one can see that it's the same as $\frac{d}{dt} \eta_t$. This proves that 
the choice of connection doesn't matter[^2].


## The Chern class

Now that we have seen how to construct characteristic classes using the curvature form, we'll
construct a specific example, these are the ones that are called the Chern classes. Let
$E$ be a rank $k$ vector bundle, and let $\Omega$ be the curvature of a chosen connection on $E$.
Consider the following polynomial in $t$, where $t \in \mathbb{R}$.
\begin{align*}
\det(t\Omega + I) = \sum_{i=1}^{k} f_i(\Omega) t^i
\end{align*}
Each of the $f_i(\Omega)$ are homogeneous degree $i$ polynomials in $\Omega$. Because
the left hand side is conjugation invariant, so is each of the $f_i(\Omega)$. That means
each $f_i(\Omega)$ defines an element (of degree $2i$) in the cohomology ring of the base space $M$.
The $i$<sup>th</sup> Chern class of the vector bundle $E$ is defined to be $f_i(\Omega)$. The previous part 
shows that this is well defined independent of the connection chosen.

The Chern classes satisfy several nice properties, including a product formula
for the Whitney sum of two vector bundles, naturality, etc. The Wikipedia [page](https://en.wikipedia.org/wiki/Chern_class#Construction_of_Chern_classes)
provides a good description, as well as references for further reading.


[^1]: The reason why this is called the curvature form is that in the case of the Levi-Civita
connection on a Riemannian manifold, this definition reduces to the standard Riemann curvature
endomorphism. [See this](https://en.wikipedia.org/wiki/Curvature_form#Curvature_form_in_a_vector_bundle). 

[^2]: This proof of independence from the connection was taken from the problem set [here](http://math.iisc.ac.in/~vamsipingali/HW43392018.pdf).
