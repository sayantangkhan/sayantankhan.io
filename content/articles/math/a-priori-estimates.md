title: What is an "a priori estimate"?
slug: a-priori-estimates
tags: analysis
category: mathematics
date: 18-12-2018

One of the things a math major learns in their first proof based course is that one must
prove existence of objects before going on to prove any properties about them. After a few years,
this becomes almost second nature, and most pure mathematicians are wary of making claims about any
object without first proving its existence. In practice, physicists and applied mathematicians
aren't held back by such restrictions: they often assume the existence of, say, a solution to a PDE,
and prove results about the solutions, e.g. prove bounds on the size, smoothness, etc. and it often
turns out that the solutions do exist, and satisfy those properties. A priori estimates are the
bounds on the solution one gets before one actually knows the solution exists. Under certain conditions,
one can then use these bounds on the solution to show that a solution exists. Informally, the chain of
logic looks something like the following.
\begin{align*}
(\text{Solution exists} \implies \text{Solution bounded by } C ) \implies \text{Solution exists}
\end{align*}
The first implication is the a priori estimate, and the second implication follows from a general
fixed point theorem. We'll see how it works out in practice, but before we see a real example, we'll
see a pseudo-example from algebra which looks similar to an a priori estimate.

### Normality is local
Let $R$ be a normal ring. This means that $R$ is an integral domain such that for any $\theta \in \text{Frac}(R)$,
if $\theta$ is a root of a monic polynomial in $R[x]$, then $\theta$ actually belongs to $R$. We want to prove
the following result.

**Theorem:** If $R$ is a normal ring, and $f$ is a non-zero element of $R$, then the localization $f^{-1}R$
is also normal.

Suppose $\theta$ is some element in $\text{Frac}(f^{-1}R)$ which satisfies a monic polynomial
in $f^{-1}R[x]$. Notice that $\text{Frac}(f^{-1}R) = \text{Frac}(R)$, so $\theta$ can be thought
of belonging to $\text{Frac}(R)$. Elements of $f^{-1}R$ are of the form $\frac{r}{f^k}$, where $r \in R$,
and we can also assume $k$ is the minimal exponent, i.e. $r$ is not a multiple of $f$ in $R$. One can think
of the exponent $k$ as a kind of norm on elements of $f^{-1}R$. Let $\theta$ be a root of the following
monic polynomial.
\begin{align*}
x^n + \frac{r_{n-1}}{f^{k_{n-1}}}x^{n-1} + \cdots + \frac{r_{1}}{f^{k_{1}}}x + \frac{r_{0}}{f^{k_{0}}}
\end{align*}
We need to show that this equation has a solution in $f^{-1}R$, in particular, $\theta \in f^{-1}$.
In the spirit of a priori estimates, let's assume that $\theta$ is a solution that actually lies
in $f^{-1}R$. We'll try to get a bound on the norm of $\theta$, i.e. an a priori estimate. Let $\theta$
be of the form $\frac{\alpha}{f^k}$. We want to plug $\frac{\alpha}{f^k}$ into the given polynomial and get
a monic polynomial in $R[\alpha]$, since $R$ is normal. If we plug in $\frac{\alpha}{f^k}$, we get the following.
\begin{align*}
	\frac{1}{f^{nk}}\alpha^{n} + \frac{r_{n-1}}{f^{k_{n-1} +nk - k}} \alpha^{n-1} +
	\frac{r_{n-2}}{f^{k_{n-2} +nk - 2k}} \alpha^{n-2} + \cdots +  \frac{r_{1}}{f^{k_{1} +nk - (n-1)k}} \alpha^{1} +
	\frac{r_0}{f^{k_0}} = 0
\end{align*}
If we want to clear denominators, and still retain a monic polynomial, our $k$ must satisfy the following inequalities
for all $1 \leq j \leq n$.
\begin{align*}
	k \geq \frac{k_{n-j}}{j}
\end{align*}
These inequalities are our a priori estimates. We assumed that the solution existed, and we then bounded its norm below
by a fixed quantity. Now we need to show that this implies a solution exists. Notice that after clearing the denominator,
we get a monic polynomial in $R[x]$ which is satisfies by $\alpha = f^k \theta$ which belongs to $\text{Frac}(R)$. Since
$R$ is normal, $\alpha \in R$, and hence $\theta = \frac{\alpha}{f^k}$ is in $f^{-1}R$.

This pseudo-example served two purposes: the first one was elucidate the key idea behind using a priori estimates without
getting bogged into analytic technicalities. The second purpose was to illustrate that the idea of boundedness implying
existence might be a very broad principle that applies in a lot of contexts. Now we'll see an actual example of
using an priori estimate. This is Example 2 from Chapter 9 of Evans' *Partial Differential Equations*.

### A quasilinear elliptic PDE
Consider a region $U$ in $\mathbb{R}^n$ with a smooth boundary $\partial U$. We want to solve
the following PDE.
\begin{align*}
	- \Delta u + \mu u = -b(Du)
\end{align*}
Additionally, we have that $u$ must be $0$ on the
boundary. In the above equation, $\Delta$ is the Laplacian, $\mu$ some number greater than $0$, $b$
is a Lipschitz function, and $D$ is a first order partial differential operator. We want to show
that for a large enough $\mu$ there exists a solution $u \in H^2(U) \cap H^1_0(U)$, where $H^2$ and
$H^1_0$ are the appropriate Sobolev spaces (if you don't know what Sobolev spaces are, think of
these spaces as functions whose derivatives are bounded).

For any $w \in H^1_0(U)$, define $f_w$ to be the function $-b(Dw)$. Since $b$ is Lipschitz, $f_w$ is in $L^2$.
If we plug in $f_w$ instead of $-b(Du)$ in the PDE, we have the following linear PDE (after fixing $w$).
\begin{align*}
	- \Delta u + \mu u = f_w
\end{align*}
By general PDE theory, linear elliptic PDEs have unique
solutions. Let the solution we get be denoted by $u_w$.  By more general nonsense (i.e. elliptic
regularity and similar statements), we have that $u_w$ is in $H^2(U)$.  We thus have a map that
takes $w \in H^1_0(U)$ to a $u_w$ in $H^2$. This can also be thought of as a non-linear continuous
map from $H^1_0(U)$ to $H^1_0(U)$. We call this map $A$, and we can bound the $H^2$ norm of $A$. The
Rellich lemma tells us that $A$ takes bounded sets to pre-compact sets in $H^1_0$. After some more
analysis, which we'll skip, we can show that for a large enough $\mu$, the following set is bounded.
\begin{align*}
SFP = \{ w \in H^1_0(U)\ |\ w = \lambda A(w) \text{ for some $\lambda \in [0,1]$} \}
\end{align*}
Observe that any $w$ such that $w = A(w)$ will be a solution of our original PDE. That means
we would like to show that $A$ has fixed points. What we have from our analysis so far is
that the set of scaled fixed points $SFP$ is bounded. This is our a priori estimate. The second
step is applying Schaefer's fixed point theorem to the map $A$, which requires the set $SFP$ be bounded,
and gives us that the map $A$ has a fixed point, and hence our original PDE has a solution.

In both the examples, the idea of the proof was guided by the following principle: pretend a solution exists to get
bounds, and after obtaining those bounds, show that a solution actually exists.
