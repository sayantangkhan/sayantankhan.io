title: Setting up GitLab to automatically generate PDFs from committed LaTeX files
slug: latex-gitlab-ci
tags: gitlab, LaTeX
category: LaTeX
date: 17-1-2018

I had been meaning to get started with GitLab's continuous integration
to generate PDFs of my assignments and notes, rather then generating the
PDFs offline and committing them to the repository as well, but I always
kept delaying the migration because of the lack of sufficient documentation
on the matter. This morning I finally got around to doing it, and I thought
I'll document it for anyone who wishes to do the same in the future.

## Outline of GitLab's continuous integration service
On receiving a commit to a repository hosted on GitLab, it
checks whether the repository has a file named `.gitlab-ci.yml`
in the root directory. This file contains the commands to be executed
by whatever computer is running the continuous integration service.
In GitLab's parlance, these are called [Runners](https://docs.gitlab.com/runner/).
These runners can be any computer, from a server running in your room, to a short lived
VM on the cloud. For the free tier, GitLab provides access to runners on 
[AWS](https://aws.amazon.com/), but with the restriction of having only 2000
minutes of compute time per month.

For these free runners, there's no configuration to be done from our side; all we need
to do is push a `.gitlab-ci.yml` to our repository, and GitLab takes care of
running it on a runner. There is one thing to watch out for though. The free runners
are usually short lived, and one can't install software on them, which means
we can't do a `sudo apt install texlive-full` as a command that runs on the runner.
Luckily, the runners do have 
[docker](https://www.docker.com/)[[2](http://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)]
installed on them, which means we can use some image from which has all the
necessary software (i.e. `texlive-full`) installed on it already.

## Configuring the runner to compile LaTeX
A cursory google search for a suitable configuration turned up the following
[configuration](https://github.com/aufenthaltsraum/stuff/wiki/Using-GitLab-CI-for-Building-LaTeX),
which is rather rudimentary, but is good guide for creating
our configuration.
```
compile_pdf:
  image: aergus/latex
  script:
    - latexmk -pdf my_file.tex
  artifacts:
    paths:
      - my_file.pdf
```
Let's go over this line by line. The first line describes the name of the job that
will be run. There can be several jobs described in a configuration file, and they
will usually be run asynchronously unless some job is listed as a dependency of another.
The next line describes what docker image to fetch: `aergus/latex` is Debian Testing
with `texlive-full` already installed. The next two lines describe the script that
will be run: these scripts are run from the root directory of the repository. In
this case, that means `latexmk -pdf` is being run on `my_file.tex` which is
at the root directory of the repository. It's possible to upload a shell script
or a Makefile to the repository and run that instead (I ended up doing the latter).
However, the files generated during the build process are discarded, which is not
quite what I wanted. I would like to keep the generated PDFs; the artifacts line
does exactly that. The artifacts can later be browsed or downloaded via the GitLab
web interface.

In my case however, the setup is a bit more complex. I do not keep all my TeX files
in the root directory, but rather organize them by course and assignment number.
So the TeX file for the fourth assignment for a topology course will have the following
location: 
```
Math/MA232\ Topology/assignments/04/assignment_04.tex
```
What I would like is to make sure the generated PDF for this TeX file is
placed in the following location.
```
Math/MA232\ Topology/assignments/assignment_04.pdf
```
I'd also like my thesis to be compiled on each commit; the location
of my thesis in the repository is the following.
```
Math/UM400\ Undergraduate\ Project/thesis/thesis.tex
```
I wrote up a `Makefile` that does all the compilation work, and places the PDFs
in appropriate locations.
```
assignments:
	cd Math/MA339\ Geometric\ Analysis/assignments; \
	latexmk -pdf */assignment_*.tex 

thesis:
	cd Math/UM400\ Undergraduate\ Project/thesis; \
	latexmk -pdf thesis.tex
```
And the `.gitlab-ci.yml` file I finally ended up using was this.
```
stages:
  - build
compile_pdf:
  image: aergus/latex
  script:
    - make assignments
    - make thesis
  stage: build
  artifacts:
    paths:
      - "Math/MA339 Geometric Analysis/assignments/assignment_*.pdf"
      - "Math/UM400 Undergraduate Project/thesis/thesis.pdf"
```
Adding these two files to the root directory of the repository does the trick.
One issue I came up against was the spaces in filenames shouldn't be escaped
with a backslash, but rather the whole file name should be enclosed in quotes.

The generated artifacts can be browsed by visiting the following link.
```
https://gitlab.com/<username>/<repo-name>/-/jobs/artifacts/master/browse?job=compile_pdf
```

It seems that compiling all the files after a commit takes up four to five minutes on 
the runner, the majority of the time being spent fetching the docker container.
That translates to roughly 400 compiles in a month, which is a reasonable enough
limit, if one or two people are committing files to the repository, but might
be a problem if a large group of people are committing a large number of files
to the repository.

The point of this whole exercise was to let me get rid of a LaTeX installation
on the devices I carry to class to make notes, which is an extremely
space constrained Nexus 7 tablet. All I now have installed on the tablet is git and
Emacs, after uninstalling texlive (also, compiling PDFs locally on the tablet would
take upwards of a minute on the under powered CPU it had).
