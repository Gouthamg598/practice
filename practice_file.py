# n = int(input().strip())
# if n%2!=0:
#     print('Weird')
# else:
#     if n>=0 and n<=5:
#         print('Not Weird')
#     elif n>=6 and n<=20:
#         print('Weird')
#     elif n%2==0 and n>20:
#         print('Not Weird')

# n = int(input('give a value'))
# if n>=0:
#     for i in range(0,n):
#         print(i**2)


# def friend(friends):
#     for frd in friends:
#         print('hi '+frd)
# friend(['gou','tham'])
# friend('gou')
# friend(['gou'])

'''------------------html------------------------------'''
# NETWORKS OF NETWORK
# INTERNET--->INTERNATIONAL NETWORKING SYSTEM OR INTERCONNECTED NETWORKING SYSTEM
# CLIENT COMPUTER----COONECTED TO--->  SERVER COMPUTER
# DEPLOYEEMENTATION MEANS LAUNCHING OF PROJECT IN WWW SERVER
# W3C-->WORLD WIDE WEB CONSORTIUM MAINTAINING THE WWW SERVER
# The World Wide Web Consortium (W3C) is an international community where Member organizations, 
# a full-time staff, and the public work together to develop Web standards.
#  Led by Web inventor and Director Tim Berners-Lee and CEO Jeffrey Jaffe, 
# W3C's mission is to lead the Web to its full potential. Contact W3C for more information.
# a,b,c,d=1,2,3,4,5
# print(a,b,c,d)
'''---------------------------------------------------------------------'''

# def is_leap(year):
#     leap = False
#     if year%400==0: 
#        return True
#     elif year%100==0:
#      return leap
#     elif year%4==0:
#          return True
#     return leap
# year=int(input('year'))
# print(is_leap(year))


# x= int(input('give a number'))#0
# sum=int(input('initialize sum value'))#0
# product=1
# while x>=1:
#     print('not done yet',x,sum,product)
#     sum=sum+x
#     x-=1  
#     product=product*x
   
# # print('completed',x,sum,product)


# from tkinter import N


# start=int(input('s'))
# end=int(input('e'))
# n=start
# while n<=end:
#  print(n)
#  n=n+1

# def intial(names):
#     word=names.split()
#     result=''
#     for name in word:
#         result+=name[0].upper()
#     return(result)
# print(intial('american standard code for information interchange'))
# print(intial('Hyper text markap language'))
# print(intial('casecade style sheet'))

# sentence=str(input('sentence :'))
# b=int(input('number :'))
# if b >0:
#     words=sentence.split()
#     if b<= len(words):
#         print(sentence[b-1])
# print('nothing')

# # def word(sentence,n):
#     # if n>0:
#        words=sentence.split()
#     #     if n<=len(words):
#     #       return words[n-1]
#     # return 'nothing'
# # print(word('this is a first lesson',3))

# list=['apple','banana','water']
# list.append('melon')
# print(list)
# list.insert(0,'mango')
# print(list)
# list.remove('water')
# # list.remove('dfghj')
# print(list)
# list.pop(3)
# print(*list)

# '''modifying'''

# list[2]='value'
# print(*list)
# list.append('blackberry')
# print(*list)


# def skipelement(elements):
#     new_list=[ ]
#     i=0
#     for element in elements:
#         if i%2!=0:
#           new_list.append(element)
#         i=i+1
#     return new_list
# print(skipelement(['a','s','d','e','f','g','h']))

# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())
# ans=[[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1) if x+y+j!=n]
# print(*ans,end=' ')

# print(0.1+0.2)
# a,b=[float(x) for x in input('enter a,b:').split(',')]
# '''palindrome'''
# from audioop import reverse


# def palindrome(names):
#     new=""
#     reverse=""
#     for name in names:
#         if name!=" ":
#             new=new+name.upper()
#             reverse=name.upper()+reverse
#             print(reverse)
#             print(new)
#     if new==reverse:
#             return 'IT IS A PALINDROME'
#     return 'NOT A PALINDROME'

# print(palindrome('Hello'))
# print(palindrome('KAYAK'))


# def re(sentence,old,new):
#     if sentence.endswith(old):
#         i=len(old)
#         print(i)
#         new_sentence=sentence[:-i]+new
#         return new_sentence
#     return False
# print(re('it is raining cats and cats','cats','dogs'))

# def fun():
#     return 55+int(55.55)
# print(fun())

'''capitalize() used to capitalize the first letter remaining is lowecase '''
# print("abc.DEF".capitalize()) 

# list=[5,8,2,5,3,1]
# list.sort()
# l=len(list)
# print(list)
# print(list[l-2])

# a=['rgd','hkhy','uoujuutt','jkwxs']
# char=0
# for i in a:
#     char=char+len(i)
# print(f'len {char} and avg:{char/len(a)}')

'''using enumerate fuction we get index and name in list in sequence'''
# for i ,a in enumerate (a):
#     print(i,a)
# # 0 rgd
# 1 hkhy
# 2 uoujuutt
# 3 jkwxs

# def emails(names):
#     result=[ ]
#     for email,name in names:
#         result.append(f'{email} and {name}')
#     return result
# print(emails([('ads@gmail.com','ads'),('qwe@gmail.com','qwe')]))

# def skip(elements):
#     list=[]
#     for i, element in enumerate(elements) :
#         if i%2==0:
#             list.append(f'{element},{i}')
#     print(*list)
# skip(['a','d','f'])

''' * will removes comas and brackets'''

# multiples=[]
# for x in range(0,11):
#     multiples.append(x*7)
# print(*multiples)#0 7 14 21 28 35 42 49 56 63 70
# print(multiples)#[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70] 
# a=[ x*7 for x in range(0,11) ]
# print(a)#[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# c=[x for x in range(0,10) if x%2!=0]
# d=[x for x in range(0,10) if x%2==0]
# e=[x for x in range(0,10) if x%3==0]
# print(c)
# print(d)
# print(e)



# a=['rgd','hkhy','uoujuutt','jkwxs']
# b=['tttt','uuuu','oooo','ggg']

# list=[ len(name) for name in b ]
from re import X


print(list) #[4, 4, 4, 3]

# a.extend(b) #['rgd', 'hkhy', 'uoujuutt', 'jkwxs', 'tttt', 'uuuu', 'oooo', 'ggg']

# a.clear() #[]

# b.reverse() #['ggg', 'oooo', 'uuuu', 'tttt']
# print(b)

# b.sort()
# print(b)#['ggg', 'oooo', 'tttt', 'uuuu']

# b.sort(reverse=True)
# print(b) #['uuuu', 'tttt', 'oooo', 'ggg']


# def gg(text):
#     say=""
#     words=text.split()
#     for word in words:
#         say+=word[1:]+word[0]+'ay'
#         if word!=words[len(words)-1]:
#             say+=' '
#     return say
# print(gg('gsjhgi fhogs hsgo'))

# def tuple(guests):
#     for guest in guests:  
#      x,y,z=guest
#     print(f'my name is {x} and age {y} my profession {z}')
# tuple([('name',50,'xyz')]) #my name is name and age 50 my profession xyz


# def group(group,user):
#     # members=[]
#     for users in user:
#     #   members.append(users)
#      members=','.join(user)
#     return(f"{group}:{members}")
# print(group('engineers',['nim','kim','dim']))#engineers:nim,kim,dim


# file=['python.py','studio.hpp','sample.hpp']
# new=[]
# for names in file:
#     if names.endswith('hpp'):
#       names=names.replace('hpp','h')
#     #   print(names)
#       new.append(names)
#     else:
#         new.append(names)
# print(new)

                                                                                                                                       
'''dictionary datatype--mutable'''

# x={'key':10}
# print(type(x),x['key']) #<class 'dict'> 10
# x['cfg']=8
# print(x)#{'key': 10, 'cfg': 8}
# x['key']=12
# print(x)#{'key': 12, 'cfg': 8}
# del x['key']
# print(x)#{'cfg': 8}
# print('key' in x)#False

# x={'key':10,'cfh':20,'pyt':30}

# for key in x:
#     print(key)#key
                # cfh
                # pyt

# for key,value in x.items():
#     print(key,value)#key 10
#                     # cfh 20
#                     # pyt 30

# print(x.keys()) #dict_keys(['key', 'cfh', 'pyt'])
# print(x.values()) #dict_values([10, 20, 30])

# for value in x.values():
#     print(value)#10
                #20
                #30

# dic={'name':'goutham','place':'hyd'}
# for key,value in dic.items():
#     print(f'{key} {value}')#name goutham
                        #   place hyd


'''global and local variable'''


'''when we declare the variable outside the function is called global variable
 if the variable inside the function is called local variable'''


'''loacl variable'''
# x = "awesome" #loacl variable
# def myfunc():
#   print("Python is " + x)#Python is  awesome
#   print("Python is ",x)#Python is  awesome
# myfunc()

'''global and local variable'''


# x = "awesome" # global variable

# def myfunc():
#   x = "fantastic" #local varable
#   print("Python is " + x) #python is fantastic

# myfunc()

# print("Python is " + x)#python is awesome

'''using global keywod we can assign the global variable'''

# def key(b):
#     global a
#     a=5
#     c=a+b
#     print(c)
# key(3)
# print(a)


# a=4
# def key(b):
#     global a
#     a=15
#     c=a+b
#     print(c)
# key(3)
# print(a)