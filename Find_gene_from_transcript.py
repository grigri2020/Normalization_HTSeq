#!/usr/bin/env python
#Use the mygene library. If not please install it. 
import sys
import mygene

mg = mygene.MyGeneInfo()

names = []
for line in sys.stdin:
    names.append(line.rstrip())

for name in names:
    result = mg.query(name, scopes="ensembl.transcript", fields=["symbol"], species="human", verbose=False)
    ensembl_name = name
    for hit in result["hits"]:
	print (hit)
        #if "symbol" in hit:
         #   sys.stdout.write("%s\t%s\n" % (ensembl_name, hit["symbol"]))
