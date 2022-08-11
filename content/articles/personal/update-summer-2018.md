title: Summer 2018 update
slug: update-summer-2018
tags: personal
category: personal
date: 6-2-2018

I'm getting lazy. I thought I would be posting more often once the summer holidays started
but May came and went with nary a post. In my defence, I was fairly busy, dealing with
the usual bureaucratic nonsense that comes with leaving your institution for good and moving
to another country. I also started learning algebraic geometry seriously, and will continue to
focus on it for a major part of the summer. Doing only math gets boring really quick though,
so I'll interleave the math sessions with some coding. I started learning [Rust](https://www.rust-lang.org),
and got sidetracked for a while by Emacs. But before I talk about Rust and Emacs, I'll quickly
outline my math plans for the summer.

### Math in Summer 2018

Given that I'll probably be doing more differential geometry at UMichigan, I figured I'd take
a break from that in the summer. In fact, I decided to stay as far as I can from analysis as well;
in fact, anything that involves taking derivatives, or dealing with inequalities. I considered
studying combinatorics, number theory or algebraic geometry, none of which I know anything about. I was also initially
encouraged by the fact that they seem as far from analysis as possible. That, of course, was astonishing
naïveté and ignorance on my part, because [generating functions](https://en.wikipedia.org/wiki/Generating_function ) 
crop up everywhere in combinatorics, and sooner or later, one would have to show one of these
things converges in some small ball in the complex plane, and then we would be back to doing analysis.
That left number theory and algebraic geometry. Analytic number theory was out of the question, so the choice
essentially boiled down to algebraic number theory or algebraic geometry. The [Wikipedia page](https://en.wikipedia.org/wiki/Algebraic_number_theory)
for algebraic
number theory had one picture, and that was a picture of a textbook. The [page](https://en.wikipedia.org/wiki/Algebraic_geometry) for 
algebraic geometry had three, and they were all images of algebraic varieties. That essentially made my decision.

I started reading Fulton's [book](www.math.lsa.umich.edu/~wfulton/CurveBook.pdf ) on algebraic curves and assumed
that would be enough. However, I learnt of an algebraic geometry summer school happening in IISER Pune, and signed
up for it immediately. But that necessitated a change of pace as they require the attendees to have studied the first chapter of Hartshorne's book
in excruciating detail. Currently, I'm reading both Fulton and Hartshorne
simultaneously and I'll probably also resume doing the exercises in Atiyah-Macdonald's commutative algebra book.

My personal goal is to build up some sort of Rosetta stone like glossary for translating stuff from algebraic
to differential geometry and vice versa. I'll write more about it once I've made some progress. The long term
goal is to learn complex algebraic geometry, where I'll be able to use techniques from both differential and
algebraic geometry. But this will probably take some time, perhaps a year or longer.


### Rust and Emacs
I've been hearing about Rust a lot these days, especially after the release of Firefox Quantum, which
apparently has large parts written in Rust. I thought it would be nice to pick a low level language
like Rust. It's certainly more suitable than Python for writing always running daemons, given that
each individual Python program spins up VM that takes up 20 to 30 megabytes for simple tasks like
scanning log files or fetching mail.

So far, I've learnt the basics of Rust's [ownership model](https://doc.rust-lang.org/book/second-edition/ch04-00-understanding-ownership.html ),
and I seem to get the basic idea, although I'll only know that for sure if I use it build something fairly
complex. I'm racking my brains thinking about what to write: I've considered writing a compression program,
which might be fun, but I'm afraid it might be a bit too ambitious. I guess I'll figure it out sooner or later.

As I mentioned earlier, I got sidetracked for a while by Emacs when I was setting it up as a Rust
environment. As it often happens, instead of just using Emacs as a tool to write code in, I started
playing around with it instead. Of course, the fact that Emacs essentially is a Lisp environment
only got me more distracted. I learnt some Emacs Lisp from this really well written [book](https://www.gnu.org/software/emacs/manual/eintr.html ) 
and it was rather fun. In fact, just a few days ago, I sent out a [pull request](https://github.com/rakanalh/emacs-dashboard/pull/70 ) 
extending an Emacs package I use. I'll be thrilled if it gets accepted. Emacs is really nice this way because
there's practically no barrier between using the editor to examining and changing the source code of the various components
that make up the editor. I cannot imagine doing the same in Vim. I'm really glad I switched.


### Conclusion
That's it for the summer update. I'll post more (and I hope with greater frequency), hopefully stuff related to algebraic
geometry and Rust (and maybe even Emacs).


