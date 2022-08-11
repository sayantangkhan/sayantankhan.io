title: An algebraic definition of the cotangent space
slug: algebraic-cotangent-space
tags: differential-geometry, algebraic-geometry
category: mathematics
date: 30-06-2018

I'm almost a week into the algebraic geometry workshop now, and I've learnt a
lot.  I've learnt a few things about varieties, and also a bit of commutative
algebra, but the most important takeaway for me from the first week was the
sheaf theoretic way of looking at smooth manifolds (and also algebraic
varieties). I'll talk a bit about this approach of looking at things, and then
outline a definition of cotangent space using this formalism, and see how that
lets us define a cotangent space on algebraic varieties. Finally, we'll have some sanity
checks on the defined cotangent space to see if some properties carry over to
the category of algebraic varieties.

## The sheaf of regular functions on a topological space
Let's consider a specific example: consider some smooth manifold $M$. For any
open subset $U$, consider the set $\mathcal{O}(U)$ of all smooth functions from
$U$ to $\mathbb{R}$.  We have such a collection for each open subset of $M$. But
that's not all - we have relations between the various $\mathcal{O}(U)$. If $U
\subset V$, then there's a natural map from $\mathcal{O}(V)$ to
$\mathcal{O}(U)$, which is the restriction map. Now recall that we are working
with smooth functions: one property of smoothness is that it's a local
property. To put it more concretely, if we have *any* map from an open set $U$
to $\mathbb{R}$ such that its restriction to each open subset $U_i$ is smooth,
where $\{U_i\}$ is some collection of open subsets that covers $U$, then we know
that $U$ is actually smooth. Phrasing this in terms of the $\mathcal{O}(U)$
formalism, it just means that if the restriction of a function $f$ to each $U_i$
is contained in $\mathcal{O}(U_i)$, then $f$ is actually in $\mathcal{O}(U)$.

These two properties make the collection $\{\mathcal{O}(U)\}$ into
a sheaf. Furthermore, the set $\mathcal{O}(U)$ can be given the structure
of an algebra, because the maps are all into a ring, and hence the functions can
be added and multiplied pointwise, and multiplied by elements of the ring
$R$. And if we vary the space $X$, the ring $R$, and the sets $\mathcal{O}(U)$,
we end up getting various familiar spaces and maps. For instance, if we keep $X$
as a manifold, and $R$ as $\mathbb{R}$, but require $\mathcal{O}(U)$ to the
collection of $C^1$ functions, we end up getting a $C^1$ manifold. If we set $X$
as a some affine variety over a field $k$, set $R$ as $k$, and set
$\mathcal{O}(U)$ as the ratio of polynomials where the denominator does not
vanish on the set $U$, we get the regular functions of affine varieties.

Sheaves are a nice way of capturing functions which satisfy some property
*locally*, whether it is being smooth, being holomorphic, or being ratios of
polynomials.

## Sheaves capture local properties
Consider a topological space $X$ and the sheaf of regular functions
$\mathcal{O}$ to a field $k$, and some point $p \in X$.  With the sheaves, we
have a way of looking at the *germ* of any function $f$ at the point $p$.  It's
clear that the germ of $f$ will capture all the local information of $f$ at that
point.  For instance, when the regular functions are smooth functions, the germ
of $f$ will contain the information about all the derivatives of $f$. If the
regular functions are holomorphic functions, the germ contains even *global*
information about the function because of analytic continuation.  The collection
of the germs of all the functions defined around $p$, called the stalk at $p$, is
again a $k$-algebra. It is much more, in fact. It's a local ring (which we'll
call $\mathcal{O}_p$), whose only maximal ideal is the set of germs of all the functions
which vanish at $p$.

Another way of getting local information at the point $p$ is to look at tangent vectors
at the point $p$. What do tangent vectors mean in this context though? A tangent vector
$v$ at $p$ is a $k$-linear map from the set of all functions defined in some open set
around $p$ to $k$ such that for any two functions $f$ and $g$, the
product rule holds.
\begin{align*}
v(fg) = f(p) \cdot v(g) + v(f) \cdot g(p)
\end{align*}
It's not quite clear from the definition whether the action of the tangent vector
on a function $f$ depends only the germ of $f$. In fact, even the relation between
the tangent space, and the local ring at $p$ is not very clear from this definition.
We need some way to link the two notions. And that's where the cotangent space comes
in. We shall define the cotangent space in purely algebraic terms, i.e. in terms of the
local ring, and then show that the space of tangent vectors $T_p$ is actually the dual of
the cotangent space, thus exhibiting the link between the local ring at $p$, to the
tangent space at $p$.

### Construction of the algebraic cotangent space
Let $\mathfrak{m}$ be the maximal ideal of $\mathcal{O}_p$. It consists of the
germs of all the functions which vanish at $p$. We define the cotangent space at
$p$ to be the set $\frac{\mathfrak{m}}{\mathfrak{m}^2}$ considered as a $k$
vector space. I won't outline the motivation behind picking this as the
cotangent space, because I myself am not completely sure why, so let's take for
granted that this is a reasonable candidate for the definition of cotangent
space. We need to show that $T_p$ is the dual of the space
$\frac{\mathfrak{m}}{\mathfrak{m}^2}$.

First we'll show every element of $T_p$ is indeed a linear functional acting on
$\frac{\mathfrak{m}}{\mathfrak{m}^2}$. Take any element $v \in T_p$. It acts
on an element $m + \mathfrak{m}^2$, and returns $v(m)$. This map is well defined,
because for any other representative $m'$, $m - m' \in \mathfrak{m}^2$, i.e. it is
of the form $m_1 m_2$ for $m_1$ and $m_2$ in $\mathfrak{m}$. Using the identity
for tangent vectors, $v(m_1m_2)$ is given by $m_1(p)v(m_2) + v(m_1)m_2(p)$, and
both the terms are $0$, since elements of $\mathfrak{m}$ evaluate to $0$ at $p$.

Now we'll show any linear functional $w$ acting on
$\frac{\mathfrak{m}}{\mathfrak{m}^2}$ gives a tangent vector $t_w$. We define
the action of $t_w$ on any function $f$ as the value of the functional $w$ on
the function $\overline{f}(x) = f(x) - f(p)$. The function $\overline{f}$ vanishes at $0$, and hence it
belongs to $\mathfrak{m}$. All we need to do is check whether it satisfies the
product rule.
\begin{align*}
t_w(f(x)g(x)) &= w(\overline{f(x)g(x)}) \\
&= w(f(x)g(x) - f(p)g(p)) \\
&= w(f(x)g(x) - f(x)g(p) + f(x)g(p) - f(p)g(p)) \\
&= w(f(x)(g(x) - g(p))) + g(p) w(f(x) - f(p)) \\
&= w((f(x) - f(p))(g(x) - g(p)) + f(p)(g(x) - g(p))) + g(p) w(f(x) - f(p)) \\
&= 0 + f(p)t_w(g) + t_w(f)g(p)
\end{align*}

This proves the duality, and gives us a link between the tangent space and the local ring.
In the case of smooth manifolds, this tells us that the cotangent space defined using the local
ring is really the same as the cotangent space defined in the usual differential geometric way.
What isn't immediately clear is how the cotangent bundle is defined, and this is something I'll
come back to later. The advantage of this construction is that the same construction goes through
for algebraic varieties. Whether this is a useful notion or not in the case of algebraic varieties
is a question that needs to be answered. But before that, we should do a sanity check. In the case
of smooth manifolds, we had the dimension of the cotangent space at every point to be the dimension
of the manifold. It's reasonable to expect that this also happens in the case of algebraic manifolds.
And that is indeed the case, and we'll see a simple proof of the fact.

### Dimension of cotangent space is the same as the dimension of algebraic variety
Before we prove the result, let's qualify the statement a little more. First of
all, it suffices to prove the result for affine varieties, since both the
cotangent space and the dimension of the variety are essentially local
properties. Secondly, varieties can have bad points, i.e. singularities, where
they intersect themselves, or there's a sharp bend of some sort (e.g. the
variety in $\mathbb{A}^2_{\mathbb{C}}$ defined by $X^3 - Y^2$). We want to avoid
those points. Thankfully, there's a nice algebraic description of the
non-singular points. A point $p$ is non-singular if the local ring
$\mathcal{O}_p$ at $p$ is regular, i.e. the maximal ideal is generated by $d$
elements, where $d$ is the dimension of the variety. With this algebraic description in hand,
our task now reduces to proving the following proposition.

**Proposition.** Suppose $A$ is a Noetherian $k$-algebra, which is also a local ring whose
maximal ideal $\mathfrak{m}$ is generated by $d$ elements $\{f_1, \ldots, f_d\}$, where $d$
is the Krull dimension of the $k$-algebra. Then the dimension of the $k$-vector space
$\frac{\mathfrak{m}}{\mathfrak{m}^2}$ is also $d$.

**Proof.** Consider any element $g$ in the ideal $\mathfrak{m}$. Since it's Noetherian and local, we can
write $g$ in the following manner,
\begin{align*}
g = \sum_j c_j (f_1)^{p_{1j}} \cdots (f_d)^{p_{dj}}
\end{align*}
where $c_j$ don't belong to the ideal $\mathfrak{m}$, and for all $j$, some $p_{ij}$ some greater
than $0$. Quotienting by $\mathfrak{m}^2$, all the terms with the higher powers of $f_i$ become $0$,
and the representative in the quotient looks like the following.
\begin{align*}
\overline{g} = \sum_{i}^{d} c_i f_i
\end{align*}
With this expression, it's easy to see what the map to the space $k^d$ is. Send $\overline{g}$ to the vector
$(c_1(p), c_2(p), \ldots, c_d(p))$. But is this map well defined? What if we also have another
representative $\overline{g}' = \sum c_i'f_i$. But in that case, each of $c_i - c_i'$ must belong
to $\mathfrak{m}$, hence $c_i(p) = c_i'(p)$.

Let's now construct a map from $k^d$ to $\frac{\mathfrak{m}}{\mathfrak{m}^2}$. Send the vector
$(c_1, \ldots, c_d)$ to the element $\sum c_i f_i$. It's easy to see this map is well defined,
and the inverse of the previous map. This proves the result.
$\blacksquare$

The cotangent space manages to pass at least this rudimentary sanity check, which makes it a little easier
to believe that this is the right notion of the cotangent space on a variety.
