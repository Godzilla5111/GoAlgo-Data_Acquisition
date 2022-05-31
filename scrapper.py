import os
import time
import re
import sys
from selenium import webdriver
from bs4 import BeautifulSoup

# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
urls = []
file1 = open('spoj/urls.txt', 'r', encoding='utf-8')
content1 = file1.read()
urls = content1.split('\n')
# file2 = open('spoj/titles.txt','r',encoding='utf-8')
# content2=file2.read()
# titles=content2.split('\n')
# titles=titles[:-1:]
# cnt=0
# for url in urls:
# 	driver.get(url)
# 	cnt+=1
# 	time.sleep(5)
# 	html = driver.page_source
# 	soup = BeautifulSoup(html, 'html.parser')
# 	problem = soup.find('div', {"class": "problem-statement"}).get_text()
# 	problem_text = problem_text.encode("utf-8")
# 	problem_text = str(problem_text)
# 	print(problem_text)
# 	# string =  re.sub('[ \n]+', ' ', problem_text).strip()
# 	# string = string[2:-1:]
# 	# arr= list(string.split('\n'))
# 	# print(arr)
# 	file1 = open('codechef/problem'+str(cnt)+'.txt','a')
# 	file1.write(string)
# 	file1.write('\n')


# Import Module
# import os
#
# Folder Path
path = r"C:\Users\ANURAG SINGH\Desktop\IIT KGP\Semesters\SEM-5\AI61005\assignment\spoj\questions"
#
# # Change the directory
os.chdir(path)
#
import nltk

#
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

# word_tokens = word_tokenize(example_sent)

# filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

# filtered_sentence = []
#
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)

# print(word_tokens)
# print(filtered_sentence)
# right = open("C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/spoj/questions/urls.txt", 'a')
# wrong_urls=wrong.read().split('\n')
# wrng=[]
# for uri in wrong_urls:
#     uri='https://www.spoj.com/problems/'+uri
#     wrng.append(uri)

# with open('C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/spoj/urls.txt', "r") as url_file:
#     lines = url_file.readlines()
# with open('C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/spoj/urls.txt', "w") as url_file:
#     for line in lines:
#         if line.strip("\n") not in wrng:
#             url_file.write(line)

# iterate through all file
unique = set()
corp = []
cnt = 0
for file in os.listdir():
    file_path = f"{path}\{file}"
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        table = soup.findAll('div', attrs={"id": "problem-body"})
        for x in table:
            paras = (x.findAll('p'))
            all = []
            for i in range(0, len(paras)):
                text = paras[i].text
                text = re.sub(r'[0-9]+', ' ', text)
                text = text.replace('_', ' ')
                text = text.replace(u'½', u'')
                text = text.replace(u'\xa0', u' ')
                text = text.replace(u'\t', u'')
                text = text.translate('\t')
                text = text.replace(u'\x0c', u'')
                text = text.replace(u'\x1c', '')
                res = re.sub(r'[^\w\s]', " ", text.lower().replace("\n", " "))
                words = [x for x in res.split(" ") if ((x != '') and (len(x) > 2) and (len(set(x)) != 1))]
                # print(words)
                filtered = [w for w in words if w not in stop_words]
                for wrd in filtered:
                    all.append(wrd)

            if len(all) > 0:
                for wd in all:
                    unique.add(wd)
            file = open(
                'C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/spoj/text/problem_' + str(
                    cnt) + '.txt', 'w')
            stri = ' '.join(all)
            file.write(stri)
            # corp.append(stri)
        cnt += 1
#                 right.write('https://www.spoj.com/problems/'+os.path.basename(f.name)[:-5:] + '\n')
#             else:
#                 # wrong = open(
#                 #    'C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/spoj/text/wrong.txt', 'a')
#                 right.write('https://www.spoj.com/problems/'+os.path.basename(f.name)[:-5:] + '\n')
#             cnt+=1
#                 # f.close()
#                 # os.remove(f.name)


# print(sorted(unique))
# file = open(
#     'C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/spoj/keywords.txt', 'a')
# sss = '\n'.join(list(sorted(unique)))
# file.write(sss)

# from rank_bm25 import BM25Okapi
# corp.append("compute sum two numbers first line include two numbers output sum")
# corpus = corp
# tokenized_corpus = [doc.split(" ") for doc in corpus]
#
# bm25 = BM25Okapi(tokenized_corpus)
#
# query = "painter partition problem"
# tokenized_query = query.split(" ")
#
# # doc_scores = bm25.get_scores(tokenized_query)
# results = bm25.get_top_n(tokenized_query, corpus, n=5)
# for result in results:
#     print(result)

#
# file = open('spoj/titleeees.txt', 'a')
# all_ques = [x for x,y in [z.split('.') for z in os.listdir('spoj/questions')]]
# all_urls = [x[30::] for x in urls][:-1:]
# for que in all_ques:
#     if que not in all_urls:
#         print(que)

# for i in range(0,len(all_ques)):
#     if all_urls[i]!=all_ques[i]:
#         print(all_urls[i], all_ques[i])

# for url in all_urls:
#     if url not in all_ques:
#         print(url)
# print(len(all_ques),len(all_urls))
