title: A week at Berlin Mathematical School
slug: bms-week
tags: travel, math-talks
category: mathematics
date: 24-2-2018

I spent the last week (18th to 24th February) at Berlin, courtesy Berlin Mathematical School,
who invited me over for the BMS Days (where I had an interview for a PhD position), as well
as the BMS Student Conference which immediately followed the BMS Days. I heard a lot of talks
on very interesting stuff, some of which I want to outline here, just to have an account of it,
if nothing else; this will also serve as a reminder of the areas and results I might want to follow
up on some time in the future.

## The math talks (in no particular order)[^1]

I'll only write about some of the talk; although all of them were fairly interesting,
some were more interesting than others. 

### The computational complexity of query answering under updates (Nicole Schweikardt, HU Berlin)
This talk outlined the idea of analyzing database systems from the point of view
of computational complexity theory, that is to say, prove effective lower bounds on
the time complexity of querying a database (and to be more specific, time complexity
in terms of only the database size for a fixed query, as well as the in terms of the
complexity of the query and the database size). The query language itself was modelled as
a first order language with a fixed number of atomic predicates depending on the type 
of the database (first order language here means that the atomic predicates maybe negated,
conjuncted, and disjuncted, i.e. NOTed, ANDed, and ORed, and one is also allowed to use
existential and universal qualifiers over elements of the database). This was the general
framework: the results in the presentation however looked at the subclass of queries
(the *Conjunctive Queries*) which
only used AND of atomic propositions, and only used the existential qualifiers[^2].

For a fixed query, Nicole described a good algorithm and a data structure for the
database such that existence and enumeration of the entries satisfying the queries could
be done reasonably fast, as well as updating the database. 

### Orbit Closures of Homogeneous Forms (Jesko Hüttenhain, TU Berlin)
This talk was motivated by the difference between the complexity class \#**P** and the
class **NP**, which the speaker roughly described as the difference in difficulty between
computing the permanent and the determinant of a given matrix[^3]. It's however only a belief
and not really known whether the former problem is strictly harder than the latter. The speaker
proposed a possible line of attack via algebraic geometry. Consider the determinant function on
$M_n(\mathbb{C})$. It is a homogeneous polynomial of degree $n$ in $n^2$ complex variables,
and it's therefore a point in the space $\mathbb{C}[x_1, \ldots, x_{n^2}]$. We can now look
at the action of $GL(n, \mathbb{C})$ on this space defined in the following manner.
$$\sigma_A: \det(X) \mapsto \det(AX)$$
The orbit defines a subset of $\mathbb{C}[x_1, \ldots, x_{n^2}]$, and this subset essentially
corresponds to all the polynomials which are as easy to compute as the determinant. Looking
at the orbit of the permanent polynomial under the same action, we would get the set of polynomials
which are as hard to compute as the permanent is. A way to show the permanent is harder to compute than
the determinant would be to show that the two orbits are different. If one looks at the closure
of the orbits, and shows that they are different, then one would have shown that even approximating
the permanent is hard[^4].

Jesko then stated one of his results, which characterized the boundary of one such orbit
closure. He also mentioned that this approach to complexity theory might take a while to
bear significant results, as the foundations of this area are being built up.

### (Some aspects of) Convexity and curvature (Stephen Lynch, FU Berlin)
This talk was a presentation of Stephen's recent work (which is also on the 
[arXiv](https://arxiv.org/abs/1709.09697)). This work generalized convex embeddings
of $S^n$ into $\mathbb{R}^{n+1}$ to higher co-dimension embeddings, where the notion
of convexity does not make sense. This was done by replacing the condition of convexity
by an inequality on the second fundamental form, which is exactly equivalent to convexity
in the case of co-dimension $1$. This sort of inequality, called the pinching condition,
leads to the solution of the mean curvature flow existing for all time, the solution
exhibited further rigidity in the sense that the evolution of time of the sphere is just
homothety.

[^1]: The complete list of BMS Student Conference talks is
	[here](https://bmsstudconf.github.io/2018/talks.html) and the ones given
	at BMS Days are listed [here](https://www.math-berlin.de/academics/bms-days).
[^2]: This kind of restriction is quite reminiscent of monotone circuits, and I wondered
	whether there was any link between presented results, and lower bounds on monotone
	circuits: the speaker however had only chosen this subclass as a simpler problem to tackle
	before tackling the problem over the full first order logic. But maybe the results obtained
	for the full first order logic might not be as good as the ones of only conjunctive queries.
	Perhaps I should have a look at this problem again in the future: some sort of such obstruction
	might turn up, and if I were to be even more optimistic, perhaps a direct correspondence between
	monotone circuits and conjunctive queries, and general circuits and general queries.
[^3]: The former problem is quite hard, as even computing the permanent of a 0-1 matrix is \#**P**-complete,
	and the latter problem is fairly easy, being in the class **P**.
[^4]: This sort of approach is a part of the nascent area of [geometric complexity theory](https://en.wikipedia.org/wiki/Geometric_complexity_theory).
