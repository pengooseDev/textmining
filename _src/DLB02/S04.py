import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')
paragraph_french = """Je t'ai demandé si tu m'aimais bien, Tu m'a répondu non. 
Je t'ai demandé si j'étais jolie, Tu m'a répondu non. 
Je t'ai demandé si j'étai dans ton coeur, Tu m'a répondu non."""
print(tokenizer.tokenize(paragraph_french))
