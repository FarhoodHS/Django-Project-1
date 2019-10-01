from django.shortcuts import render
import string


def wordlister(txt):
    for l in txt:
        if l in string.punctuation:
            txt = txt.replace(l, '')
    wordlst = txt.split()
    return wordlst

def home(request):

	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = wordlister(fulltext)

	worddict={}

	for word in set(wordlist):
		worddict[word] = wordlist.count(word)

	worddict = sorted(worddict.items(), key=lambda x:x[1], reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'dic':worddict})


def about(request):

	return render(request, 'about.html')