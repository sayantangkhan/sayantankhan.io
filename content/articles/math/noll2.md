title: Notes on learning Lean (2/?)
slug: learn-lean-2
tags: lean
category: mathematics
date: 2-26-2024
updated: 2-26-2024

## On how Lean gave me the hypotheses I needed to prove a correct theorem

Working my way through [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/C05_Elementary_Number_Theory.html#induction-and-recursion), I came across an exercise that required proving the standard monomial summation identities, e.g. $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$, and $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$.
The easy proof is via the standard induction, which works well enough in Lean, but as an exercise for myself, I decided to prove it via telescoping sums, namely add up the sequence $\sum_{i=1}^{n} i^3 - (i-1)^3$, and relate that to the two identities I was trying to prove.

In Lean, the statement that a telescoping series cancels out looks like this.

    :::lean4
    theorem telescoping_sum (f: ℕ → ℕ) (n : ℕ) : ∑ i in range (n + 1), (f (i + 1) - f (i)) = f (n+1) - f (0) := by
      sorry

For simplicity, we are working with functions from $\mathbb{N}$ to $\mathbb{N}$ instead of to $\mathbb{Z}$ or $\mathbb{R}$.
The proof should be fairly simple, but inducting on the inductive datatype `Finset.sum (range n)`, where the two constructors are `Finset.sum (range 0)`, which is $0$ by definition, and `Finset.sum (range (n+1)) f`, which is `Finset.sum (range n) f + f n`.
Replacing this with `sorry` should finish off the proof.

    :::lean4
    theorem telescoping_sum (f: ℕ → ℕ) (n : ℕ) : ∑ i in range (n + 1), (f (i + 1) - f (i)) = f (n+1) - f (0) := by
      induction' n with n ih
      · rw [Finset.sum_range_succ, Finset.sum_range_zero]
        simp
      · rw [Nat.succ_add, Finset.sum_range_succ, ih, ← Nat.succ_eq_add_one (n+1)]
        rw [add_comm, ← Nat.add_sub_assoc, add_comm, ← Nat.add_sub_assoc, Nat.add_sub_self_left]

However, this does not actually close the goal, and instead introduces a new sub-goals, of the type `f (n+1) ≤ f (n+2)`, and `f 0 ≤ f (n+1)`.
In other words, Lean requires the function $f$ to be non-decreasing in order to believe the proof we have provided.
This is a bit puzzling, since the pen and paper proof of this fact is fairly simple, and involves cancelling out adjacent terms.

It turns out the issue is with performing subtraction on $\mathbb{N}$: recall that we work with functions $\mathbb{N} \to \mathbb{N}$ instead of $\mathbb{N} \to \mathbb{Z}$ for convenience.
The Lean math library definition of subtraction for $a$ and $b$ in $\mathbb{N}$ defines it to be $a - b$ (the usual definition) if $a \geq b$, and $0$ otherwise. 
By this definition of truncated subtraction, the theorem statement we wrote down is actually false: consider the function $f$ defined by the sequence $0, 1, 2, 1, 3$.
The sum of $f(i+1) - f(i)$ is going to be $1 + 1 + 0 + 2 = 4$, but $f(4) - f(0)$ is $3$.
This explains why the compiler refused to accept the proof: the proof was not correct. However, another question one may ask is how did the compiler know that the hypothesis of non-decreasing $f$ was required.

To determine that, we look at the lemma we used to simplify the subtraction, namely `Nat.add_sub_assoc`: this has type `h : k ≤ m → n + m - k = n + (m-k)`.
We used this lemma in the rewrite tactic, but did not actually provide the hypothesis $h$, which is why compiler introduced that as a sub-goal at the end.

With the explained, here's the correct version of the theorem and its proof.

    :::lean4
    theorem telescoping_sum (f: ℕ → ℕ) (f_nondec: ∀ m k, m ≤ k → f (m) ≤ f (k)) (n : ℕ) : ∑ i in range (n + 1), (f (i + 1) - f (i)) = f (n+1) - f (0) := by
      induction' n with n ih
      · rw [Finset.sum_range_succ, Finset.sum_range_zero]
        simp
      · rw [Nat.succ_add, Finset.sum_range_succ, ih, ← Nat.succ_eq_add_one (n+1)]
        rw [add_comm, ← Nat.add_sub_assoc, add_comm, ← Nat.add_sub_assoc, Nat.add_sub_self_left]
        apply f_nondec
        apply Nat.le_succ
        apply f_nondec
        simp




## Some more tactics

- `rcases`: When the goal is a parameterized by an inductive type, this will split up the goal according to the constructors of the inductive type.
- `clear`: Remove hypotheses from context, for cleaner induction, amongst other uses.
- `simp`: Repeatedly rewrite terms in context using simplifying lemmas until the goal is reached.
- `simp_rw`: For rewriting within dependent types. Not sure I understand why though.
- `let`: When defining a constant, or a function within a proof, we can use `let` to give it a name.
- `unfold_let` and `unfold`: For things defined via let, using them in proofs does not automatically unfold them: we need to use `unfold_let`. Just `unfold` is useful for functions definitions(?).

## Other resources

- [Moogle](https://www.moogle.ai/): This seems like an analog of Hoogle, but for mathlib. It's been helpful to find simple enough lemmas, but its utility for fancier math remains to be seen.
- [GPT4](https://openai.com/gpt-4): I was (an still am, to some extent) a skeptic about using GPT for programming, but one thing it seems to be reasonable at is telling me which basic lemma I need from mathlib in order to prove some elementary arithmetic fact.
I don't suppose it will help with finding lemmas for more complicated situations, but while I'm still learning what's where in mathlib, it is a useful tool.