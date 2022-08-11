title: Cohomology as a measure of local to global failure
slug: cohomology-local-global
tags: cohomology, sheaves, topology
category: mathematics
date: 25-12-2017
updated: 30-12-2017

## Motivation for cohomology
In most introductory algebraic topology courses, cohomology is rather poorly motivated. It's most
commonly seen form in an algebraic topology course is singular cohomology, which arises as a the
homology of the dual of the singular chain complex, but that doesn't really tell you why it's of any
more interest than singular homology, aside from the fact that you get an additional cup product
which you did not have before. However, this approach obscures the geometric meaning of cohomology.

A much more intuitive introduction to cohomology turns out to be De Rham cohomology, often
encountered in introductory differential geometry courses. Loosely speaking, De Rham cohomology
measures in how many different ways can a closed form fail to be exact.

Another cohomology theory we'll look at is sheaf cohomology. Loosely, the cohomology of a sheaf
measures how a certain functor $\Gamma$, which we'll define later fails to be an exact functor.

In the case of De Rham cohomology, we'll interpret the form being closed as a local property, and it
being exact a global property, and the the case of sheaf cohomology, the exactness of the following
sequence (the exact details of which we'll see in a later section) as a local property.  $$0
\rightarrow \mathcal{S}_1 \rightarrow \mathcal{S}_2\rightarrow \mathcal{S}_3 \rightarrow 0$$ The
exactness of the sequence we get by applying $\Gamma$ to the above sequence turns out to be a global
property.

In both the cases, the cohomology measures how the local property fails to translate to the global
one.

## De Rham Cohomology
The De Rham cohomology of a manifold $M$ (of dimension $m$) is the homology of the following of the
following cochain sequence.  $$0 \xrightarrow{d} \Lambda^0(M) \xrightarrow{d} \Lambda^1(M)
\xrightarrow{d} \cdots \xrightarrow{d} \Lambda^m(M) \xrightarrow{d} 0$$ Here, $\Lambda^k(M)$ is the
space of $k$-forms on $M$, and $d$ is the exterior derivative operator.  For a $k$-form $\omega$ to
be closed, $d\omega$ must be $0$. This is a local property, in the sense that $d\omega$ evaluated at
any point $p \in M$ depends only on the value of $\omega$ on any small neighbourhood of $p$.  In
fact, one can say a little more, and claim that $d\omega(p)$ depends only on the *germ* of $\omega$
at $p$.  If we pick a Euclidean neighbourhood $U$ of $p$ which is homeomorphic to the open unit
ball, the Poincaré lemma tells us that there is some $(k+1)$-form $\eta$ defined on $U$ such that
$\omega = d\eta$. In other words, the closed form $\omega$ is locally exact.

The De Rham cohomology class of $\omega$ measures how badly does the property of local exactness
fail to translate to global exactness. We can write $\omega$ as $\gamma + d\zeta$, where $\gamma$ is
the canonical representative of the cohomology class of $\omega$ (more on this in later posts), and
$\zeta$ is a $(k-1)$-form. If we stretch the analogy a bit, we can say $\omega$ misses being
globally exact by $\gamma$ amount. This is the first example of how cohomology measures how badly a
local property fails to be global.

## Sheaf Cohomology
Before we see what sort of local to global failure sheaf cohomology measures, we'll quickly define
sheaves and sheaf cohomology, and look at one example.
### Quick introduction to sheaves
Given a manifold $M$ (whatever we discuss will hold in for Hausdorff spaces, and with a little more
work, can be made to work even for a larger class of spaces like spectra of rings), a sheaf
$\mathcal{S}$ of $K$-modules ($K$ is always assumed to be a commutative ring with identity) over $M$
is a topological space $\mathcal{S}$ with a surjective map $\pi: \mathcal{S} \to M$, such that the
following properties are satisfied.

1. $\pi$ is a local homeomorphism, i.e. for any point $s \in \mathcal{S}$, there's a neighbourhood
of $s$ such that $\pi$ restricted to that neighbourhood is a homeomorphism.
2. $\pi^{-1}(x)$, which we'll denote by $\mathcal{O}_x$, is a $K$-module, for all $x \in
M$. $\mathcal{O}_x$ is called the stalk of $\mathcal{S}$ at $x$.
3. The module operations on the stalk are continuous, i.e. if we look at the stalk with the subspace
topology, the module operations of addition and scalar multiplication are continuous.

Sheaves in some sense a modules parametrized by the space $M$, like vector bundles, but vector
bundles do not satisfy the first condition, unlike sheaves.  The simplest example of a sheaf is the
*constant sheaf* which is just $M \times V$, where $V$ is a $K$-module with the discrete topology.

Another important example is the sheaf of germs of $C^{\infty}$ functions on a manifold $M$. For
each $x \in M$, a point in $\mathcal{O}_x$ is an equivalence class of functions, the equivalence
relation being that $f \sim g$ if $f$ and $g$ agree on some neighbourhood of $x$. This sheaf
deserves a post of its own, and I shall write about it in the future.

The last example, which will be key to our goal, is the *skyscraper sheaf*. We'll describe it by
first describing the stalk at each point, and then putting an appropriate topology on it. Fix a
point $x_0 \in M$.  The stalk $\mathcal{O}_{x_0}$ at $x_0$ will be $K$ as a module over itself. The
stalk at every other point is the zero module. As a set, our sheaf is the following.  $$\mathcal{S}
= K \sqcup \bigsqcup_{x \neq x_0} \{0\}$$ The question is what topology do we put on this space. The
[line with two origins](https://en.wikipedia.org/wiki/Non-Hausdorff_manifold#Line_with_two_origins)
provides a hint. What we do is take $|K|$ copies of the space $M$, and if $x \neq x_0$, we identify
all of those $x$'s, otherwise we do nothing. It's not too hard to check that this defines a sheaf
over $M$ (the local homeomorphism property is the hardest to check, and relies on the fact that
points are closed in Hausdorff spaces). In fact, if $M = \mathbb{R}$ and $K = \mathbb{Z}/2$, then
then skyscraper sheaf at $0$ *is* the line with two origins. The reason this is called the
skyscraper sheaf is because only the stalk at $x_0$ is tall, the stalks everywhere are flat, which
makes it look like a tall structure in an otherwise flat featureless landscape.

We're really interested in is a variant of a skyscraper sheaf with two skyscrapers, i.e. the stalks
at points $x_0$ and $x_1$ are $K$, and otherwise $0$. The topology on this sheaf can be defined
analogously. We'll come back to this example once we've defined sheaf cohomology.

### The category of sheaves of $K$-modules over a space
Just like in the case of a vector bundles over a manifold $M$, where the *right* kind of map between
vector bundles is a smooth map that is a linear map on each fibre, the *right* kind of map between
two sheaves $\mathcal{S}_1$ and $\mathcal{S}_2$ on a space $M$ is a continuous map $f$ such that it
satisfies the following properties.

1. $\pi = \pi \circ f$
2. $f$ restricted to any any stalk $\mathcal{O}_x$ is a $K$-module homomorphism.

Fixing a space $M$, we get the category of sheaves of $K$-modules over $M$, whose objects are
sheaves, and the morphisms are what we just defined, called sheaf homomorphisms. It follows from the
fact that $\pi$ is a local homeomorphism that even sheaf homomorphisms are local homeomorphisms.
This category turns out to be especially nice, sharing many characteristics with the category of
abelian groups and more generally, the category of $K$-modules, such as maps possessing kernels and
cokernels, and possessing a version of the [First Isomorphism
Theorem](https://en.wikipedia.org/wiki/Isomorphism_theorems#First_isomorphism_theorem).  This sort
of category is called an abelian category, and this category is the appropriate category to do
homological algebra in. Coming back to sheaves, the kernel of a sheaf homomorphism $f: \mathcal{S}_1
\to \mathcal{S}_2$ is the set of all points which map to the zero element in the stalk. With a
little bit of work, we can show the image of $f$ is a sheaf in its own right, and subsheaf of
$\mathcal{S}_2$, just like the kernel of $f$ is a subsheaf of $\mathcal{S}_1$ (the definition of a
subsheaf is the most obvious one).

With all these definitions in hand, we can talk about exact sequences of sheaves. Consider a
sequence of sheaves and sheaf homomorphisms of the following kind.  $$\cdots \xrightarrow{d_{i-2}}
\mathcal{S}_{i-1} \xrightarrow{d_{i-1}} \mathcal{S}_{i} \xrightarrow{d_{i}} \mathcal{S}_{i+1}
\xrightarrow{d_{i+1}} \cdots$$ This sequence is exact if $\mathrm{ker}(d_{i}) =
\mathrm{im}(d_{i-1})$.

The next thing we look at is the functor $\Gamma$ from the category of sheaves of $K$-modules over
$M$ to the category of $K$-modules. For each sheaf $\mathcal{S}$, the object $\Gamma(\mathcal{S})$
is the module of sections of $\mathcal{S}$. A section of a sheaf $\mathcal{S}$ is a map $s: M \to
\mathcal{S}$ such that $\pi \circ s = \mathrm{id}$. Clearly, we can add two sections, and we can
also multiply them by a scalar; we therefore have a $K$-module. The functor $\Gamma$ acts on
morphisms by composing them with the section map, i.e. $\Gamma(f) = f \circ s$. The important
question to ask here is whether the functor $\Gamma$ is exact, i.e. does it short exact sequences to
short exact sequences. The answer is no. Consider the following short exact sequence.  $$0
\rightarrow \mathcal{S}_1 \xrightarrow{\alpha} \mathcal{S}_2\xrightarrow{\beta} \mathcal{S}_3
\rightarrow 0 \tag{1}$$ If we apply the functor $\Gamma$ to the sequence, we get something that is
not completely exact.  $$0 \rightarrow \Gamma(\mathcal{S}_1) \xrightarrow{\Gamma(\alpha)}
\Gamma(\mathcal{S}_2) \xrightarrow{\Gamma(\beta)} \Gamma(\mathcal{S}_3) \rightarrow 0 \tag{2}$$ This
sequence is exact only exact at $\Gamma(\mathcal{S}_1)$ and $\Gamma(\mathcal{S}_2)$.

Suppose some $s \in \Gamma(\mathcal{S}_1)$ maps to $0$ in $\Gamma(\mathcal{S}_2)$. That tells us
that $\Gamma(\alpha)(s) = 0$. But that by definition means that $\alpha \circ s = 0$. But $\alpha$
is injective, which means $s = 0$. This shows exactness at $\Gamma(\mathcal{S}_1)$.

Showing exactness at $\Gamma(\mathcal{S}_2)$ is a little more involved. Consider an element $s \in
\Gamma(\mathcal{S}_2)$ which gets mapped to the zero section in $\Gamma(\mathcal{S}_3)$. That means
for all $m \in M$, $\beta(s(m)) = 0$.  By exactness at $\mathcal{S}_2$, we can find for each $m$, an
element $s'(m)$ of $\mathcal{S}_1$ such that $\alpha(s'(m)) = s(m)$.  Furthermore, because the
original short exact sequence is exact at $\mathcal{S}_1$, the element $s'(m)$ is uniquely defined
(this is where the argument fails to work for $\Gamma(\mathcal{S}_3)$). All we need to show now is
that the map $m \mapsto s'(m)$ is a continuous map. This is where we use the fact that sheaf
homomorphisms are local homeomorphisms. For any $m$, pick a small enough neighbourhood $U$ around
$s'(m)$ such that $\alpha$ is a local homeomorphism on $U$. Then $s'^{-1}(U)$ is given by
$s^{-1}(\alpha(U))$, which is open since $s$ is a continuous section.

Notice that the exactness of sequence $(1)$ is a purely local property; it suffices to check whether
the sequence on each stalk is exact. On the other hand, showing exactness at $\Gamma(\mathcal{S}_3)$
would be a global property. This is because given any section $s \in \Gamma(\mathcal{S}_3)$, the
best we can do is construct sections $s_U$ on open subsets $U$ of $M$. It might so happen that these
sections defined on different subsets of $M$ cannot be patched together consistently to get a
continuous section. The cohomology of the sheaf will measure how badly the functor $\Gamma$ fails to
be exact; to be more precise, the cohomology will tell us how extend sequence $(2)$ to get an exact
sequence. We'll leave the precise details of this for a later post, and satisfy ourselves with an
example of when exactness fails to happen at $\Gamma(\mathcal{S}_3)$.

To show this, we will exhibit a surjective sheaf homomorphism $f$ such that $\Gamma(f)$ is not a
surjective module map. Consider a connected space $M$, and let $\mathcal{S}_1$ be the constant sheaf
on $M$. Recall that this means $\mathcal{S}_1$ is $M \times K$, with the discrete topology on
$K$. Let $\mathcal{S}_2$ be the skyscraper sheaf on $M$ with two skyscrapers, which means the stalk
is $K$ at points $x_0$ and $x_1$ and zero otherwise.  On the stalk at point which is not $x_0$ or
$x_1$, the homomorphism is obviously the zero homomorphism. On the stalk at $x_0$ and $x_1$, we let
the homomorphism be the identity homomorphism. It's clear that this sheaf homomorphism, call it $f$
is surjective. But observe that $\Gamma(\mathcal{S}_1) = K$. That's because we picked $M$ to be a
connected manifold, which means the section must the constant section. On the other hand,
$\Gamma(\mathcal{S}_2) = K \oplus K$, since the section can take any value independently at $x_0$
and $x_1$. Which means $\Gamma(f)$ is a map from $K$ to $K \oplus K$, which cannot be surjective in
general.

This tells us that exactness at $\Gamma(\mathcal{S}_3)$ is a global property, and the cohomology
measures (in a loose sense) how the local property of exactness of $(1)$ fails to translate to
exactness of $(2)$.

ADDENDUM: I will add links to similar expositions whenever I find them.

1. Čech cohomology and the Mittag-Leffler problem: The Čech cohomology determines
whether meromorphic functions defined on small open sets can be patched together to
get a globally defined meromorphic function satisfying certain properties. 
([Link](https://toperkin.mysite.syr.edu/talks/sheaves_and_more_cohomology.pdf) to article)
