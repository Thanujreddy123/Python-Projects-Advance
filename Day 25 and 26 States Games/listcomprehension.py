list1=[1,2,3,4]
newlist=[lis+1 for lis in list1]
print(newlist)
rangelist=[i for i in range(2,6) if i%2==0]

print(rangelist)

sentence = input()

# Using dictionary comprehension
result = {word:len(word) for word in sentence.split()}

print(result)