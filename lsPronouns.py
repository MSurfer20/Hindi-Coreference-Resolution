import sys
sys.path
sys.path.append('./scripts/ssfapi/')
import ssfAPI_intra as ssf

fl = ssf.folderWalk('./data')
pronouns = set()
reflexives = set()
relatives = set()
thirdPerson = set()
firstPerson = set()
secondPerson = set()
locatives = set()
for rfp in fl:
    doc = ssf.Document(rfp)
    for s in doc.nodeList:
        for c in s.nodeList:
            for n in c.nodeList:
                if n.morphPOS == 'pn':
                    pronouns.add(n.lex)

for p in pronouns:
    