import nltk
paper = { 'madison' : [10],  'jay' : [2] , 'shared' : [18] , 
         'disputed' : [49]
         }

def read_files(filename):
    strings=[]
    
    for file in filename:
        with open(f'federalist_{file}.txt') as f:
            strings.append(f.read())
            
            return('\n'.join(strings))
            
f1={}

for a,files in paper.items():
    f1[a] = read_files(files)

for a in paper:
    print(f1[a] [:10])
    
authors = ( 'madison','jay','shared','disputed')
a_tokens = {}
l_distri = {}
for a in authors:
    tokens = nltk.word_tokenize(f1[a])
    a_tokens[a] = ([token for token in tokens if any(c.isalpha() for c in token)])
    token_lengths = [len(token) for token in a_tokens[a]]
    l_distri[a] = nltk.FreqDist(token_lengths)
    l_distri[a].plot(15, title = a)
    
    