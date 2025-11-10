from collatex import *

with open('witnesses/V1_16_09_24.txt') as f:
    premiere_version = " ".join(f.readlines())
with open('witnesses/V2_14_11_24.txt') as f:
    derniere_relecture = " ".join(f.readlines())

collation = Collation()
collation.add_plain_witness("V1", premiere_version)
collation.add_plain_witness("V2", derniere_relecture)


tei_output = collate(collation, output="xml", segmentation=False, near_match=False)

with open("collation.xml", "w") as output:
    output.write(tei_output.replace("<app>", "\n<app>"))