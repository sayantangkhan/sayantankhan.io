title: Notes on learning Lean (3/?)
slug: learn-lean-3
tags: lean
category: mathematics
date: 5-09-2024
updated: 5-09-2024

Now that I'm done writing and defending my thesis (and submitting the associated paper to a journal), I can dive back into Lean full time (for the next few months at least).
I just wrapped up Chapter 5 of [MIL](https://leanprover-community.github.io/mathematics_in_lean/), and the final theorem of the chapter, namely the fact that there are infinitely many primes that are equal to $3$ mod $4$ was a fun one to formalize: and used an inductive type I had not encountered yet, namely `Finset`s.
This chapter also featured the first use of strong induction on `Nat`, which modifies the induction tactic to use strong induction.

Working with `Finset` also led down to the rabbit hole of constructive vs. classical logic.
To filter a `Finset` with some predicate (i.e. a `Prop`) `P`, the the predicate has to be in the `DecidablePred` typeclass.
This would make working with `Finset`s of real numbers quite annoying, since inequalities involving real numbers are not decidable (or semi-decidable, whatever that may mean).
Conveniently, one can convince the Lean compiler to work in classical logic, instead of constructive logic, by opening the `Classical` namespace.
I suppose this namespace has the law of excluded middle (or some equivalent notion) as an axiom, which makes all `Prop` decidable, and makes it possible once again to work with finite sets of reals.
[This article](https://www.andrew.cmu.edu/user/avigad/Teaching/classical.pdf) by Jeremy Avigad on classical vs constructive logic was a fun read.

Going on a tangent, and thinking about Lean as a programming language, I noticed that some of the more general tactics make it seem like tactics form a monad: namely `repeat`, and `<;>` which sequences two tactics, as well as some others.
Another analogy is how we start a tactic proof using the `by` keyword, very much like the `do` notation in Haskell.
It makes sense, since a tactic takes the current proof "state", and applies some operation on it to give a new proof "state".
[Chapter 5 of PIL](https://avigad.github.io/programming_in_lean/writing_tactics.html) confirms this observation.
I am quite pleased to have identified a familiar monad in a new programming language.

## Some more tactics

- `contradiction`: Closes the current goal if there are contradictory or (decidably) false hypothesis in the environment.
- `by_contra h`: If the goal is `p`, it introduces a hypothesis `h : \not p`, and changes the current goal to `False`.
- `repeat'`: Similar to `repeat`, but runs the tactic on the newly produced goals as well, perhaps? The documentation online is somewhat sparse.
- `t1 <;> t2`: This runs the tactic `t1` on the main goal, and then `t2` on the subsequent goals.
- `push_neg at h`: If `h` has type `\not a \leq b`, it creates a new hypothesis `h` with type `a > b`, and so on.
- `interval_cases x : a`: Creates cases for `x` if the `x` is a natural or an integer, assuming it can find in the ambient hypotheses upper and lower bounds for `x`. If so, it splits into cases for each possible value of `x`.
I should try and see if there's a variant of this tactic that splits up cases into sub-intervals.
- `strong_induction_on`: Modifies the `induction'` tactic to use strong induction instead.
- `refine` and `refine'` are generalizations of `exact` and `apply`, where you can provide some of the arguments, and it will turn the missing arguments into new goals.
More specifically, if you are trying to construct an object of a dependent type, it will let you plug in the pieces you already have.
- `ext` tactic: The `ext` tactic applies “extensionality lemmas”. An extensionality lemma says “two things are the same if they are built from the same stuff”. In practice so far, this came up when I was trying to show two sets `A` and `B` are equal: calling `ext x` gave me two cases to deal with: it gave me an `x \in A`, and the goal was to show `x \in B`, and second case was the other way around.
- `tauto` and `tauto!`: These were useful in dealing with goals that were tautologically true, at least the set-theoretic ones, and these tactics closed them immediately. I need to figure out what contexts do these tactics work in.
- `decide`: This tactic is useful if the goal is something that Lean has an algorithm to decide: e.g. equality of `Nat`, primality of `Nat`, etc.
- `let` and `set`: This lets us define new variables in a tactic proof. The `set` variant will also rewrite all of the ambient hypotheses to use the new variable if possible.
- `revert`: This is `intro` backwards.
- `by_cases h`: This creates two new subgoals, one which assumes `h`, and one which assumes `\not h`. This requires that `h` be decidable (but if we are working with classical logic, this is moot).
- `tidy`: This is a meta tactic that helps you find the right tactics to solve the goal. Not sure how useful this is in the mathlib context.
- `norm-num`: If the goal is an arithmetic expression involving the 4 standard operators, equality, and inequalities, this will reduce the expression to a normal form, which is then decidable.

## Reading

- [On how](https://spiral.imperial.ac.uk/bitstream/10044/1/100952/6/Schemes%20in%20Lean.pdf) schemes were formalized, and the perils of universal properties.

## Other small notes

- There is a possibly a typo in Section 5.3 (as of 05/09/2024): the line about `dsimp` is probably stale.
