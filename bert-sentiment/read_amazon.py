import bz2  
# output_file = codecs.open('text.ft.txt.bz2','w+','utf-8')

source_file = bz2.BZ2File('test.ft.txt.bz2', "r")
count = 0
amazon_positive=[]
amazon_negative=[]

f_train = open("amazon_train.txt", "a")
f_test = open("amazon_test.txt", "a")
for line in source_file:
    if count >= 50 and  count < 100:
        f_test.write(line[10:].decode("utf-8") )
        count +=1
    elif count<50:
        print(line[10:].decode("utf-8"))
        f_train.write(line[10:].decode("utf-8") )
        count +=1
    
source_file.close()