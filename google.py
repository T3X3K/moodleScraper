from googlesearch import search
import sys
from termcolor import colored

query = ' '.join(sys.argv[1:])

for i in search(query, lang="it", advanced=True):
    print(colored(i.title.upper(), 'red',attrs=['bold','underline']), end="\t")
    print(i.url)
    print(colored(i.description,'cyan'))
for i in search(query, lang="en", advanced=True):
    print(colored(i.title.upper(), 'red',attrs=['bold','underline']), end="\t")
    print(i.url)
    print(colored(i.description,'cyan'))