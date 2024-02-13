title: Notes on learning Lean (1/?)
slug: learn-lean-1
tags: lean
category: mathematics
date: 2-13-2024
updated: 2-13-2024

Now that I am almost done with my dissertation, I have decided to switch focus and concentrate on doing math that can be formally checked by the [Lean Theorem Prover](https://lean-lang.org/).
The ideal sub-field of math for me to start formalizing would be Teichüller theory, and results on mapping class groups, since that is what my research as a graduate student focused on.
However, it appears that even formalizing complex analysis, which is the behind a lot of classical Teichmüller theory is still a major project in progress (see [the project page](https://alexkontorovich.github.io/PrimeNumberTheoremAnd/web/sect0001.html) for current progress).
Even with a lot of complex analysis formalized, there is still a substantial amount of work to be done in order for "formalized Teichmüller theory" to catch up even with results from the 1970s, and the flavor of the subject has changed a lot since then, after the work of Thurston, Masur, etc.

A more fun and realistic goal for me would be to instead focus on a related sub-field, which is understanding $\mathrm{Out}(F_n)$, and its action on [Outer Space](https://en.wikipedia.org/wiki/Outer_space_(mathematics)).
The results in this field somewhat parallel the results about the mapping class groups actions on Teichmüller space, but on the other hand, most of the proofs use graphs, and their covering spaces, rather than closed surfaces.
Furthermore, a lot of the arguments in the field (based on sporadic attendence of a [course on the subject taught by Alex Wright](https://public.websites.umich.edu/~alexmw/Math636Notes.pdf)) seem to be very combinatorial in nature, which is very amenable to formalization in Lean.
A concrete goal, which ought to be reachable in a year, would be a formalization of the proof of existence of greedy folding paths, which (perhaps?) is the analog of Teichmüller's existence theorem.

However, before I start formalizing results on $F_n$ and Outer Space, I need to learn enough Lean to start proving non-trivial results, which is what this series of blog posts will be documenting.
I am currently working my way through [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/), and hope to get to Chapter 9, which is on topological and metric spaces, in the next few weeks.
Once I cover Chapter 9, I ought to have enough background to start thinking about Outer Space, and then I can either check the Lean Zulip to see if someone else is already working on it, or announce my own project.

## How theorem proving in Lean works

Theorems in Lean have the type `Prop`, and they themselves are types, and a proof of a theorem is a construction of a term of that type (i.e. it uses the [Curry-Howard isomorphism](https://leanprover-community.github.io/mathematics_in_lean/) to map theorems we would like to prove to corresponding types).
In practice, writing a proof as a term of a certain type can get very annoying, so most proofs in Lean (and elsewhere), are written using *tactics*.
Tactics can be thought of as a meta-language that tells the Lean compiler how to build a proof term, but in a manner that is still readable to a human reader: think of macros in Lisp.
A theorem of the form $\forall x \in X, P(x)$ is a type $X \to P(x)$, i.e. a function mapping the type $X$ into the dependent type $P(x)$.
When constructing this function in tactic-mode, the goal is to construct a term of type $P(x)$, and our local context already contains a variable $x$ of type $X$.
Tactics allow us (among other things) do the following.

- Change the current goal, or create a subgoal. For instance, if we have a theorem that says $Q(x) \implies P(x)$, we can use the `suffices` (or `apply`) tactic to change the current goal. Alternatively, if we have a theorem of the form $x = 2y+1$, we can change the goal using the `rw` tactic to $P(2y+1)$.
- Split up the local context into cases: In case the proof of $P(x)$ depends on the value of $x$, we can use the `cases` tactic to split up the cases rather than writing a more complicated proof term.

## Tactics

Here is a list of some of the tactics I have seen and used so far. These are mainly notes for myself in order to remember these tactics better.

- `intro`: When trying to prove a statement of the form $\forall x P(x)$, it will introduce a variable $x$, when trying to prove a statement of the form $P \implies Q$, it will introduce a term of type $P$ in the context, and for any other goal, it will evaluate the goal to its weak head normal form, which informally is just unpacking the definition of the goal: e.g. if the goal is a proposition of the form $A \neq B$, then it will introduce a sub-goal of the form $A = B \implies \text{False}$.
- `cases`: This splits up an inductive type into its contructors: for instance, a hypothesis of the form $P \vee Q$ is an inductive type, and then the goal splits into two subgoals, one of which assumes $P$, and one of which assumes $Q$.
Another instance of applying `cases` to an inductive type is with `Nat`, where rather than using the `induction` tactic, we can use `cases` to split up a `Nat` as `0` or `succ d`.
- `induction`: This has syntax similar to `cases`, except for the cases where data constructors wraps the type itself (e.g. with `Nat`, `succ d` wraps `d` which is `Nat`), it also introduces an inductive hypothesis as an assumption.
- `left` and `right`: This is needed when proving a Proposition that is an OR statement. After possibly splitting up into cases, and landing in a situation where one of the terms of the OR statement is provable, `left` and `right` change the current goal to the left and right terms of the OR statement.
- `use`: This is needed when proving a statement of the form $\exists x, P(x)$. Invoking $\text{use} c$ will change the goal to $P(c)$.
- `contrapose` (and `contrapose!`): Given a theorem where the goal is to prove $Q$ using hypothesis $P$, `contrapose h` will instead change the goal to `\not Q` using the hypothesis `\not P`, and `contrapose! h` will do the same, and apply `push_neg` to both of these types (which simplifies the negation to some extent).
- `nth_rewrite`: A more precise version of the `rw` tactic, which only applies to the $n$th instance. This also uses $1$-based indexing of the rewrite locations.
- `repeat`: Repeatedly apply whatever tactic that follows it until it can be no longer applied. In practice, I usually see this applied to applications of the `rw` tactic.
- `obtain`: It's a combination of `have` and `cases` that I do not fully understand yet (see [this link](https://www.ma.imperial.ac.uk/~buzzard/xena/formalising-mathematics-2022/Part_C/tactics/obtain.html)).
- `decide` (and more generally, algorithms): This is also something I need to learn more about: from what I understand so far, if the goal is a `Decidable` proposition, i.e. in the typeclass of Propositions that can be algorithmically decided (where the algorithm is part of the typeclass instantition for the Proposition family), this tactic runs that algorithm and provides a proof.
- `tauto`: This is useful when either `False` is a hypothesis, or `True` is a goal.
