import stanfordnlp
stanfordnlp.download('en', force=True)
nlp = stanfordnlp.Pipeline(lang='en')
doc = nlp("Testing sentence goes here or actual mail body")
print(type(doc))

for i, sent in enumerate(doc.sentences):
    print("[Sentence {}]".format(i+1))
    for word in sent.words:
        print("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(\
              word.text, word.lemma, word.pos, word.governor, word.dependency_relation))
    print("")
