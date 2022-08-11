title: The most overloaded word in math
slug: overloaded-word
tags: nomenclature
category: mathematics
date: 14-10-2018

Last Wednesday, the conversation in my office veered towards the words we hated the most in
math. Not surprisingly, the list included the usual suspects like *normal*, *simple*, and *regular*.
It's probably the same reason that these words also make it to the top five of [this MathOverflow
post](https://mathoverflow.net/questions/7389/what-are-the-most-overloaded-words-in-mathematics). These
words are overloaded to the point of meaning something different to mathematicians working in
different areas of math. On the other hand, we all agreed that some overloading of words was
actually fairly useful: for instance, it makes sense to call a normal covering space normal since it
actually corresponds to a normal subgroup of the fundamental group.  That means calling a cover
normal and calling a subgroup normal isn't really a bad thing, since it shows that those two notions
are related.

We thought we'd do something similar for all the possible meanings of the word normal: we'd define
an equivalence relation between two different meanings if there is some result, deep or otherwise,
that links the two notions. Then the number of equivalence classes we get would be a much better
metric of the overloaded-ness of the word *normal*.

Here's a list of the meanings of *normal* (taken from Wikipedia), along with some additions.

- **Normal subgroup**: A subgroup which is invariant under conjugation action.
- **Normal cover**: A covering space whose deck transformation group acts transitively.
- **Normal field extension**: A field extension such that every irreducible polynomial in the base
   field splits into linear factor, or is irreducible.

These three uses of normal are really the same, since they all talk about an associated subgroup
being a normal subgroup. In the case of the normal cover, the fundamental group of the cover is a
normal subgroup of the fundamental group of the base space. When it comes to field extensions,
consider the following field extension: $E \subset F \subset G$, where $G$ is Galois over $E$.  In
this case, $F$ is a normal extension iff it corresponds to a normal subgroup of $\mathrm{Gal}(E/G)$.

A few different meanings of the word normal(ize) show up often in algebraic geometry.

- **Normal domain**: An integral domain which is integrally closed in its field of fractions.
- **Normal varieties**: A variety $X$ such that any finite birational map from any variety $Y$ to
  $X$ is an isomorphism.
- **Noether normalization**: The Noether normalization lemma states that for any finitely generated
  $k$-algebra $A$, there exist $\{y_1, \ldots, y_d\} \in A$ such that $A$ is a finitely generated
  module over $k[y_1, \ldots, y_d]$.

These seemingly different notions actually are somewhat equivalent. As it turns out, a variety is
normal if the local ring at every point is integrally closed. And while normal varieties are
varieties which have maps from "nice" varieties, a geometric interpretation of Noether normalization
is that every $d$-dimensional affine variety is a ramified cover of $\mathbb{A}^d$, which is a "nice"
variety.

Another meaning of the word normal comes from the geometric notion of being perpendicular. This
gives us a lot of different meanings of the word normal which we can collapse to one equivalence
class.

- **Normal bundle**: The normal bundle of an embedded submanifold is the vector bundle such that the
  fibre over each point consists of vectors perpendicular to the tangent space.
- **Normal coordinates**: Given a vector bundle with an affine connection, the normal coordinates
  around a point are coordinates such that the Christoffel symbols of the connection vanish at the
  point.
- **(Ortho)normal basis**: A basis of an inner product space such that each vector is of norm $1$ and
  every pair is perpendicular.
- **Normal operator**: An operator which commutes with its Hermitian conjugate.
- **Normal modes**: (Taken from wikipedia) A normal mode of an oscillating system is a pattern of
  motion in which all parts of the system move sinusoidally with the same frequency and with a fixed
  phase relation.

Normal bundle literally comes from the original meaning of the word normal in the sense of being
perpendicular. Normal coordinates also come from the same source: in the case of the Levi-Civita
connection, one gets a set of normal coordinates by applying the exponential map to an orthonormal
basis of the tangent space.

The reason why a normal operator is called a normal operator is that we know from the spectral
theorem that its eigenvalues form an orthonormal basis. That is also the source of normal modes. The
"normal" in normal modes comes from the fact that the vibrations are the eigenvectors of a certain
differential operator, which happens to be self-adjoint, hence normal. That means all the normal
modes literally form an orthonormal basis of solutions to the associated PDE.

The above words were some of the different cases of the usage of the word *normal* that we were able
to collapse.  And below are the ones we couldn't collapse to anything else, so they sit all by
themselves (for now) in their own equivalence class.

- **Normal family**: A pre-compact family of holomorphic functions.
- **Normal space**: A topological space which satisfies the $T_4$ axiom. [Here's a bad pun](http://brownsharpie.courtneygibbons.org/comic/i-used-to-confuse-regular-and-normal/) involving this.
- **Normal forms**: These are a whole class of ways to write matrices of linear operators in a nice form,
  e.g. Jordan normal form, Smith normal form, etc.
- **Normal distribution**: The distribution that most sums of random variables converge to, thanks to the
  Central limit theorem.
- **Normal forms part deux**: All the normal forms that crop up in formal language theory and
  computability, e.g. conjunctive normal form, disjunctive normal form, Chomsky normal form, etc.

We started off with 18 different meanings of the word *normal*, and now, after constructing the
equivalence relation, we are left with only 8 different equivalence classes (maybe fewer, if someone
discovers some deep result linking normal operators to normal subgroups). That makes one think: maybe
it's not so ab*normal* for mathematicians to overuse normal after all.
