paper = { 'madison' : [10, 14, 37, 38, 39],  'jay' : [2,3,4,5] , 'shared' : [18, 19, 20] , 
         'disputed' : [49, 50 , 51, 52, 53 ,56,57]
         }

def read_files(filename):
    strings=[]
    
    for file in filename:
        with open(f'federalist_{filename}.txt') as f:
            strings.append(f.read())
            
            return('\n'.join(strings))
            
f1={}

for a,files in paper.items():
    f1[a] = read_files(files)

for a in paper:
    print(f1[0] [:100])