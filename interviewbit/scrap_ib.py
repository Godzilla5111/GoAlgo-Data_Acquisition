import os
import time
import re
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

driver = webdriver.Chrome(ChromeDriverManager().install())
stop_words = set(stopwords.words('english'))

urls = []
file1 = open('urls.txt', 'r', encoding='utf-8')
content1 = file1.read()
urls = content1.split('\n')
urls=urls[:-1:]
url=urls[0]
file2 = open('titles.txt','r',encoding='utf-8')
content2=file2.read()
titles=content2.split('\n')
titles=titles[:-1:]
corpus = set()
for i in range(0,1):
    all = []
    url = urls[i]
    title = titles[i]
    driver.get(url);
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # replace with `soup.findAll` if you are using BeautifulSoup3
    for quote in soup.find_all("blockquote"):
        quote.decompose()
    problem = soup.find('div',{"id":"problem-content"})
    problem_text = problem.get_text()
    problem_=str(problem)
    problem_ = problem_.encode("ascii", "ignore")
    problem_ = problem_.decode()
    text = problem_text
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
        corpus.add(wrd)

    question_file = open('C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/interviewbit/questions/problem_'+str(3864+i)+'.html', 'w')
    question_file.write('<html>')
    # question_file.write(</title>'+title+'</title>')
    question_file.write(len(title)*'*')
    question_file.write('<h3 class="title">'+title+'</h3>')
    question_file.write(len(title)*'*')
    question_file.write('<body><div>')
    question_file.write(problem_)
    question_file.write('<br><p>Problem URL: <a href='+url+'>'+title+'</a></p>')
    question_file.write('</div></body></html>')
    text_file = open('C:/Users/ANURAG SINGH/Desktop/IIT KGP/Semesters/SEM-5/AI61005/assignment/interviewbit/text/problem_'+str(3864+i)+'.txt','w')
    text_file.write(' '.join(all))

print(sorted(corpus))
driver.quit()
