title: Notes on learning Lean (4/?)
slug: learn-lean-4
tags: lean
category: mathematics
date: 06-12-2024
updated: 06-12-2024

## Updates on learning Lean

I have now made it all the way to the end of the metric spaces chapter of the [MIL](https://leanprover-community.github.io/mathematics_in_lean/C09_Topology.html#topological-spaces), which means in principle, I should have everything I needed from the book to start the $Out(F_n)$ project.
The last exercise in the section was formalizing a proof that a complete metric space is Baire, a theorem I had not thought about since my undergraduate topology class.
Writing down the proof made clear some of the pain points I'm likely to encounter when proving more substantial results.

1. The `simp` tactic can only do so much: given a goal of the form $A \cap f(n) \subseteq B \cap f(n)$, where $f n$ is an indexed family of sets, and we have amongst our hypotheses $A \subseteq B$, one would expect `simp` to easily close the goal. However, it made no progress, and it's unclear whether it was the indexing on the family `f` that threw it off, or it was something else.
In any case, I will have a lot of 'almost' trivial goals like this, that I'd like to close automatically, but I will have to do them manually, or someone will have to write a more clever tactic.
2. A related pain point is more of an ergonomic one: when diving into proofs of these 'almost' trivial subgoals, I would like to fold their proofs after they're completed, so that they don't clutter the main body of the proof. This would be a fairly simple VS Code plugin, if someone choses to do it. On the other hand, perhaps this is a good thing, encouraging proof/code golfing?
3. I need a good way to find lemmas related to a specific object: GPT is not doing it any more, since it can really only handle the basic lemmas. The search on Mathlib docs is a little slow, plus there does not seem to be a good way to filter down to lemmas using some sort of semantic search/filtering.

## Some more tactics

- `field_simp`: As the name suggests, this simplifies terms living in a field to a normal form.
- `linarith` can be provided helper lemmas to aid in simplification via `linarith [p1, p2, p3]`.
- `trans`: Used to prove goals that are transitive relations. Given a goal `s \sim t`, `trans u` will create two subgoals `s \sim u` and `u \sim t`.
- `intros`: Repeated use of `intro` until quantifiers in goal are gone.
- `constructor`: If the goal is structure with several components, e.g. an AND statement, it will create a goal for each field in the original goal.
- `congr` and `gcongr`: These are congruence tactics, which as far as I understand, are useful when working with group/ring/whatever isomorphisms, and arguments based on applying isomorphisms.
- `aesop`: This is a more powerful version of `simp`, with better proof search algorithms. An example of this is the `continuity` tactic.
- `choose` and `choose!`: These two tactics essentially convert a complex hypothesis asserting existence of objects satisfying certain properties to functions that construct those objects, and hypotheses that the constructed objects must satisfy.
- `Nat.le_induction` and `Nat.strong_induction`: These are alternate recursors for `Nat`, which can be used with the `induction` tactic to start induction at a positive `Nat`, or do strong induction.


## Preparing for the $\mathrm{Out}(F_n)$ project

The first step, before actually writing any code, would be to figure out what's already in mathlib that I will need.

- Groups with presentations: [Presented group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PresentedGroup.html)
- Metric spaces and covering spaces, specifically graphs: [Metric spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Basic.html)
- Group actions on metric spaces via isometries: [Group actions by isometries](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PresentedGroup.html)
- Gromov hyperbolic groups and spaces: Search on Google and Zulip doesn't turn up much, but asking people in the community might help point to some Github repo that has bits of these implemented.
- PL structures: Unclear if [this](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/ChartedSpace.html) will be helpful in defining a PL structure on Outer Space.

### Organizing code

- [Naming conventions](https://leanprover-community.github.io/contribute/naming.html): Refer to this more thoroughly once I start uploading code on Github.
- [Documentation conventions](https://leanprover-community.github.io/contribute/doc.html): Also refer to this when uploading code to Github, as well as sending PRs to mathlib.
- [Library style guidelines](https://leanprover-community.github.io/contribute/style.html)
- [Sections and variables](https://lean-lang.org/lean4/doc/sections.html)
- [Namespaces](https://lean-lang.org/lean4/doc/namespaces.html)

## On typeclass inference

- The syntax `[Group G]` (or similar), isn't exactly a typeclass constraint as much as it is an implicit typeclass argument. The difference between this and implicit arguments of the form `{...}` is that in the `[...]` case, it uses a typeclass resolution algorithm to find the right instance, but it can possibly be provided a custom instance if the right instance is not found.
