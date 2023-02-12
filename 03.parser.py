import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple, a big  tech company, is looking at buying U.K. startup for $1 billion. Investors are worried about the final price.")

for token in doc:
    print(token.text, token.head)

for token in doc:
    if (token.is_sent_start):
        print(token.text, token.is_sent_start)

displacy.serve(doc, style="dep")
