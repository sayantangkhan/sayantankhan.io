import json

markdown_cv_path = "./content/pages/CV.md"

with open("CV_data/education.json") as fp:
    education = json.load(fp)

with open("CV_data/research.json") as fp:
    research = json.load(fp)

with open("CV_data/teaching.json") as fp:
    teaching = json.load(fp)

with open("CV_data/awards.json") as fp:
    awards = json.load(fp)

with open("CV_data/talks.json") as fp:
    talks = json.load(fp)

with open("CV_data/mentoring.json") as fp:
    mentoring = json.load(fp)

with open("CV_data/service.json") as fp:
    service = json.load(fp)

with open("CV_data/conferences.json") as fp:
    conferences = json.load(fp)

with open("CV_data/skills.json") as fp:
    skills = json.load(fp)

with open(markdown_cv_path, "w") as writer:
    writer.write(
        """Title: Curriculum Vitae
slug: cv
Priority: 5

[Link to a PDF version](pdfs/cv/cv.pdf) of the CV.

"""
    )

    # Education section
    writer.write("### Education")
    for stage in education:
        result = """
**{university}**
{degree}, {major}, {year}
""".format(
            university=stage["university"],
            degree=stage["degree"],
            major=stage["major"],
            year=stage["year"],
        )
        writer.write(result)
        if "thesis" in stage:
            writer.write("{0}, *{1}*".format(stage["thesis"][0], stage["thesis"][1]))

    # Research section
    writer.write("\n\n### Research\n")
    writer.write("**Research Interests**: {0}\n\n".format(research["interests"]))
    writer.write("#### Papers\n")
    for paper in research["papers"]:
        writer.write("- *{0}* ".format(paper["title"]))
        if "coauthors" in paper:
            writer.write("With {0}. ".format(paper["coauthors"]))
        writer.write(
            "({0}; [{1}]({2}))\n".format(
                paper["journal"], paper["arxiv_id"], paper["arxiv_link"]
            )
        )

    # Teaching section
    writer.write("\n### Teaching\n\n")
    for course in teaching:
        writer.write(
            "- {0} for {1} ({2}) \n".format(
                course["role"], course["course"], course["semester"]
            )
        )

    # Awards section
    writer.write("\n### Awards \n\n")
    for award in awards:
        writer.write("- {0}, {1}\n".format(award["title"], award["duration"]))

    # Talks section
    writer.write("\n### Talks \n\n")
    writer.write("#### Invited Talks\n")
    for talk in talks:
        if talk["type"] == "invited":
            writer.write(
                "- *{0}*. ({1}) \n".format(
                    talk["title"],
                    ", ".join(
                        "{0} ({1})".format(i[0], i[1]) for i in talk["locations"]
                    ),
                )
            )

    writer.write("\n#### Student Seminars\n")
    for talk in talks:
        if talk["type"] == "student-seminar":
            writer.write("- *{0}*\n".format(talk["title"]))

    # Mentorship section
    writer.write("\n### Mentorship\n")
    for thing in mentoring:
        writer.write(
            "- *{0}* ({1}): {2}\n".format(
                thing["title"], thing["semester"], thing["description"]
            )
        )

    # Service section
    writer.write("\n### Service\n")
    for thing in service:
        writer.write("- {0}\n".format(thing))

    # Conferences section
    writer.write("\n### Conferences, summer schools, and workshops attended\n")
    for conference in conferences:
        writer.write("- {0}\n".format(conference))

    # Technical skills
    writer.write("\n### Technical skills\n")
    writer.write(
        "I am proficient in the use of following languages, and technical tools\n\n"
    )
    for skill in skills:
        writer.write("- {0}\n".format(skill))
