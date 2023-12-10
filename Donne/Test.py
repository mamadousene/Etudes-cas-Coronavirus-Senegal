import json
load={}
with open("AllCommunes.json","r") as rf:
    load.update(json.load(rf))
rf.close()
fichier =open("CreateCommune.json","x")
fichier.close()
ville=[]
for key,val in load.items():
    if val.upper() not in ville:
        ville.append(val.upper())
ville.sort()
with open("CreateCommune.json","w") as wf:
    json.dump(ville,wf)
    wf.close()
print(len(load))