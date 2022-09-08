from nltk.tokenize import sent_tokenize
para = "Hello everyone. It's good to see you. Let's start our text mining class!"

parsed_data = sent_tokenize(para)

#sentence-tokenized(문장 토큰화)




# return = ['Hello everyone.', "It's good to see you.", "Let's start our text mining class!"]
# .이나 !을 기준으로 split해서 보내줌.

def printer (parsed_data):
    for i in parsed_data:
        print("=====================")
        print(i)
    print("=====================")



printer(parsed_data)



