def convert(str):
    return (str,[1,2,3,4,5])



array = ('linux','windows')
tuplelist=map(convert,array)
print tuplelist

print  tuplelist[0][1][1]




def convert2(str):
    return {str:[1,2,3,4,5]}

tuplelist2=map(convert2,array)
print tuplelist2