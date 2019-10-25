import stanfordnlp
import sys

"""
f = open("/home/groups3/testgr/MergerTest/Debug/nlpSuccess.txt","w+")
f.write("SUCCESS\n")
f.close()
"""

# stanfordnlp.download('en', force=True)
nlp = stanfordnlp.Pipeline(lang='en')
doc = nlp(sys.argv[1])
output = ""

for i, sent in enumerate(doc.sentences):
    output = output + ("[Sentence {}]".format(i+1)) + "\n"
    for word in sent.words:
        output = output + ("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(\
              word.text, word.lemma, word.pos, word.governor, word.dependency_relation))
        output = output + "\n"

f = open("/home/groups3/testgr/MergerTest/Debug/nlpOutput.txt","w+")
f.write(output)
f.close()
