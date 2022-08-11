title: On why I use Emacs to write TeX
slug: emacs-and-latex
tags: emacs, LaTeX
category: Emacs
date:17-10-2020

An observation I made a while ago while peeking over people's shoulders (with their
consent, of course) is that even when they're writing TeX in a powerful text
editor, like Emacs or Vim, most people don't really harness the extensive
programmability of their text editor (especially MM[^1]). For instance, here's a
non-exhaustive list of things you can program Emacs to do for you, rather than
doing it yourself.

- Begin an environment, and place your cursor in the environment, rather than
  painfully typing out `\begin{<environment>}` and `\end{<environment>}`. For
  more complex environments like `figure`, Emacs can also prompt you
  for the required parameters, and suggest sensible defaults.
- Automatically insert appropriate labels for sections, equations, and
the like.
- Pop up an easily navigable list of labels when you're to reference something. The
list of labels also features some of the text following it so that you can tell at
a glance what each label corresponds to.
- When citing something from a BibTeX file, rather than typing out the label of the
  entry, Emacs lets you fuzzy search by author, words in the abstract, by the
  journal, etc.
- Ensure that you never have unmatched parentheses, quotes, and the TeX variants
  like `\langle` and `\rangle`, `\left(`, and `\right)`, etc.

Some of these features, or approximations thereof, are baked into some of the more
TeX specific editors, like TeXStudio, or the Overleaf editor, but they aren't quite
as powerful as the Emacs version, neither are they customizable. The features
listed above are provided by the packages `AuCTeX`, `RefTeX`, and `smartparens`.
As with most Emacs packages, these are written in Emacs Lisp, and as a result,
their source code is quite easy to understand, and modify.

## Demonstrations
  <table class="image">
<caption align="bottom">Entering a figure environment, and filling in the details. The keyboard shortcut for creating
a new environment is `\e`.</caption>
<tr><td>
 <video width="600" height="600" controls>
  <source src="../../images/emacs-and-latex/part1.webm" type="video/webm">
Your browser does not support the video tag.
</video>
</td></tr>
</table>

  <table class="image">
<caption align="bottom">Creating a new equation: note that it automatically gets labelled as `eq:1`.</caption>
<tr><td>
 <video width="600" height="600" controls>
  <source src="/images/emacs-and-latex/part2.webm" type="video/webm">
Your browser does not support the video tag.
</video>
</td></tr>
</table>


  <table class="image">
<caption align="bottom">Creating a reference to an equation. The popup shows what equation each label corresponds to.</caption>
<tr><td>
 <video width="600" height="600" controls>
  <source src="/images/emacs-and-latex/part3.webm" type="video/webm">
Your browser does not support the video tag.
</video>
</td></tr>
</table>


  <table class="image">
<caption align="bottom">Citing a book/paper. Note that all I needed to specify was that the author was Thurston.</caption>
<tr><td>
 <video width="600" height="600" controls>
  <source src="/images/emacs-and-latex/part4.webm" type="video/webm">
Your browser does not support the video tag.
</video>
</td></tr>
</table>

  <table class="image">
<caption align="bottom">As soon as I write `\langle`, Emacs automatically creates the matching `\rangle`.</caption>
<tr><td>
 <video width="600" height="600" controls>
  <source src="/images/emacs-and-latex/part5.webm" type="video/webm">
Your browser does not support the video tag.
</video>
</td></tr>
</table>

I hope that this video post encourages people to start using Emacs, and writing elisp to customize it. [Happy hacking](https://stallman.org/articles/happy-hacking.html)!

[^1]: If you're reading this, you know what I'm talking about.
