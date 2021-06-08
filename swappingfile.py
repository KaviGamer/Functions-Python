def swapFileData():
    data_a = open('sample1.txt','r')
    data_b = open('sample2.txt','r')
    a = open('sample1.txt','w')
    a.write(data_b)
    a.close()
    b = open('sample2.txt','w')
    b.write(data_a)
    b.close()

swapFileData();

print("Process Complete!")