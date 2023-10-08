from googlesearch import search
import sys
from termcolor import colored
import webbrowser

query = ' '.join(sys.argv[1:])

ita = list(search(query, lang="it", advanced=True))
eng = list(search(query, lang="en", advanced=True))
count = len(eng) * 2
for i, j in zip(reversed(ita),reversed(eng)):
    print(count, end=".   ")
    print(colored(j.title.upper(), 'red',attrs=['bold','underline']), end="\t")
    print(j.url)
    print(colored(j.description,'cyan'))
    print(count-1, end=".   ")
    print(colored(i.title.upper(), 'red',attrs=['bold','underline']), end="\t")
    print(i.url)
    print(colored(i.description,'cyan'))
    count = count - 2
num = input("Che url vuoi aprire? ")
if num != 'q':
    num = int(num)
    if num%2 == 1:
        url = ita[num].url
        webbrowser.open(url, new = 0, autoraise = True)
    if num%2 == 0:
        url = eng[num].url
        webbrowser.open(url, new = 0, autoraise = True)