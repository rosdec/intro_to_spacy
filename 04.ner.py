import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")

for ent in doc.ents:
    print(ent.text, ent.label_)

spacy.displacy.serve(doc, style="ent")