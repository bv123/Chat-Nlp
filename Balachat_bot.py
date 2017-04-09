# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 14:31:09 2016

@author: BalaVignesh
"""

import re
with open("G://Nlp//baloo.txt", 'r') as content_file:
    content = content_file.read()
    
#content


#Splitting chats into separate chats using "Chat with" as separator
chat_sep=re.split('"\d{1,3}" "Chat with',content)
#print chat_sep[2]
len(chat_sep)

#280 chats


# testing regex
'''
for i in range(len(chat_sep)):
    chat_sep[i]=re.sub("\d{1,2}:\d{1,2}","",chat_sep[i])

for i in range(len(chat_sep)):
    chat_sep[i]=re.sub("Visitor navigated .*","",chat_sep[i])

#for i in range(len(chat_sep)):
#    chat_sep[i]=re.sub("\n"," ",chat_sep[i])

for i in range(len(chat_sep)):
    chat_sep[i]=re.sub("mUniversity .*"," ",chat_sep[i])

for i in range(len(chat_sep)):
    chat_sep[i]=re.sub("Convert to ticket\nName\neg@email.com\nNotes","",chat_sep[i])
    
for i in range(len(chat_sep)):
    chat_sep[i]=re.sub("Name xxxxxxxx\neg@email.com\nPh :12345","",chat_sep[i])
    
for i in range(len(chat_sep)):
    chat_sep[i]=re.sub("(Mo(n(day)?)?|Tu(e(sday)?)?|We(d(nesday)?)?|Th(u(rsday)?)?|Fr(i(day)?)?|Sa(t(urday)?)?|Su(n(day)?)?)","",chat_sep[i])

for i in range(len(chat_sep)):
    chat_sep[i]=re.sub("(January|February|March|April|June|July|August|September|October|November|December).*","",chat_sep[i])
'''

#m = re.search(' (.+?)\n,', chat_sep[1])
#if m:
#    found = m.group(1)
#found

for i in range(len(chat_sep)):
    chat_sep[i]=re.sub("\d{1,2}:\d{1,2}","",chat_sep[i])
    chat_sep[i]=re.sub("Visitor navigated .*","",chat_sep[i])
    chat_sep[i]=re.sub("mUniversity .*"," ",chat_sep[i])
    chat_sep[i]=re.sub("Convert to ticket\nName\neg@email.com\nNotes","",chat_sep[i])
    chat_sep[i]=re.sub("Name xxxxxxxx\neg@email.com\nPh :12345","",chat_sep[i])
    chat_sep[i]=re.sub("(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)","",chat_sep[i])
    chat_sep[i]=re.sub("(January|February|March|April|June|July|August|September|October|November|December).*","",chat_sep[i])
    chat_sep[i]=re.sub('"\n\nVisitor has ended the chat.\n"',"",chat_sep[i])
    #m = re.search(' (.+?)\n,', chat_sep[i])
    #if m:
     #   found = m.group(1)    
    #chat_sep[i]=re.sub(found,"Visitor_name",chat_sep[i])
    
    #within_chat=re.split('Visitor_name',chat_sep[i])
chat_sep[1]
for i in range(len(chat_sep)):
    m = re.search(' (.+?)\n,', chat_sep[i])
    if m:
        found = m.group(1)
        chat_sep[i]=re.sub(found,"Visitor_name1",chat_sep[i])
    
    #within_chat=re.split('Visitor_name',chat_sep[i])     #found

#chat_sep[12]
#chat_sep[1]
#within_chat[1]
within_chat=[]
for i in range(len(chat_sep)):
    within_chat.append(re.split('_|\n \n\n',chat_sep[i]))
    
len(within_chat[1])
within_chat[1]
visitor=[]
muni=[]
#muni.append([])
#muni[0].append([])
#muni[0][0]
k=0
l=0
for i in range(len(within_chat)):
    muni.append([])   
    visitor.append([])     
    for j in range(len(within_chat[i])):
        if "name1" not in  within_chat[i][j]:
            #muni.append([])
            k=len(muni)-1
            muni[k].append(within_chat[i][j])
            #k+=1
        else:
            #visitor.append([])
            l=len(visitor)-1
            visitor[l].append(within_chat[i][j])
            #l+=1
        #k+=1
        #l+=1
#muni[1][2]
#visitor[1]
#muni[1]

for i in range(len(muni)):
    for j in range(len(muni[i])):
        muni[i][j]=re.sub('Visitor|\n',"",muni[i][j])
    
for i in range(len(visitor)):
    for j in range(len(visitor[i])):
        visitor[i][j]=re.sub('name1|\n|your question.. :|Visitor',"",visitor[i][j])  

#muni[2]
#visitor[2]          


with open("D:\\Study Stuff\\NLP\\BABD FAQs.txt", 'r') as content_file:
    content_faq = content_file.read()

#content_faq

faq_sep=re.split('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',content_faq)
#print faq_sep[0]
len(faq_sep)

questions_faq=faq_sep[0]
qa_faq=faq_sep[1]

#qa_faq
questions_faq=re.sub('Questionnaire:|\d{1,2}-',"",questions_faq)
#questions_faq

questions_faq=re.split('\nQ|\nCLQ',questions_faq)

for i in range(len(questions_faq)):
    questions_faq[i]=re.sub('\n',"",questions_faq[i])

#questions_faq



from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
visitor_stop=list()
#visitor_stop.append(["hello","bala"])
#visitor_stop
#visitor_stop[1].append(["hello","bala"])
#m=0
stop = set(stopwords.words('english'))
stop.update([","])
stop
for i in range(len(visitor)):
    for j in range(len(visitor[i])):
        #visitor_stop[=[None]*len(visitor[i][j])
        m=" ".join([r for r in visitor[i][j].lower().split() if r not in stop])
        #m+=1
        visitor_stop.append(m)
m
visitor_stop
visitor_q=visitor_stop
#print [i for i in sentence.lower().split() if i not in stop]

len(visitor_stop)
visitor_stop[i]
visitor_q=list()
for i in range(len(visitor_stop)):
    #for j in range(len(visitor_stop[i])):
        #for k in len(visitor[i][j]):
    if len(visitor_stop[i])>3:
        visitor_q.append(visitor_stop[i])

visitor_q
cos_sim=list()
for i in range(len(questions_faq)):
    train_set = [visitor_q[4],questions_faq[i]]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix_train=(tfidf_vectorizer.fit_transform(train_set))  #finds the tfidf score with normalization
    cos_sim.append(cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train[1]))  #here the first element of tfidf_matrix_train is matched with other three element

#cos_sim.index(max(cos_sim))


####question by candidate
visitor_q[4]
#questions_faq[cos_sim.index(max(cos_sim))]
#questions_faq


#qa_faq
#answers=[]


answers=re.split('Q\d{1,2}|Q \d{1,2}',qa_faq)
#answers
#corresponding FAQ
answers[cos_sim.index(max(cos_sim))]

