from collatex import *

with open('witnesses/V1.txt') as f:
    premiere_version = " ".join(f.readlines())
with open('witnesses/V2.txt') as f:
    premiere_relecture = " ".join(f.readlines())
with open('witnesses/V3.txt') as f:
    derniere_relecture = " ".join(f.readlines())

collation = Collation()
collation.add_plain_witness("V1", premiere_version)
collation.add_plain_witness("V2", premiere_relecture)
collation.add_plain_witness("V3", derniere_relecture)


tei_output = collate(collation, output="xml", segmentation=True, near_match=False)

with open("collation.xml", "w") as output:
    output.write(tei_output.replace("<app>", "\n<app>"))