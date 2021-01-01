Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 16:30:00) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[2,4,6]
>>> print(list1[:])
[2, 4, 6]
>>> print(list1[-1])
6
>>> list=["Ajay","Baby","Mommy","Anil","Roshan","Ammu"]
>>> print(list[::2])
['Ajay', 'Mommy', 'Roshan']
>>> print(list[1::2])
['Baby', 'Anil', 'Ammu']
>>> print(list[2:3:])
['Mommy']
>>> print(list[-1:4:])
[]
>>> archu=[10,20,30,40,50,60,70,80,90]
>>> print(archu[0:8:1])
[10, 20, 30, 40, 50, 60, 70, 80]
>>> print(archu[0:7:2])
[10, 30, 50, 70]
>>> print(archu[-3:])
[70, 80, 90]
>>> print(archu[-2:5])
[]
>>> print(archu[:-3])
[10, 20, 30, 40, 50, 60]
>>> print(archu[1:-3:2])
[20, 40, 60]
>>> print(archu[::-1])
[90, 80, 70, 60, 50, 40, 30, 20, 10]
>>> a=[10,20,30,40,50]
>>> a[:2]=[1,2,3,4,5]
>>> print(a)
[1, 2, 3, 4, 5, 30, 40, 50]
>>> a=[10,20,30,40,50]
>>> a[::2]=[1,1,1,1,1,1,1,1,1]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[::2]=[1,1,1,1,1,1,1,1,1]
ValueError: attempt to assign sequence of size 9 to extended slice of size 3
>>> a=[10,20,30,40,50]
>>> a[::2]=[1,1]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a[::2]=[1,1]
ValueError: attempt to assign sequence of size 2 to extended slice of size 3
>>> a=[10,20,30,40,50,60,70,80,90]
>>> a[::2]=[1,1,1,1,1]
>>> print(a)
[1, 20, 1, 40, 1, 60, 1, 80, 1]
>>> 
>>> 
>>> 
>>> list=["abc","xyz","aba","1221"]
>>> s=0
>>> for i in list:
	if i[0]==i[-1]:
		s+=1
		print(s)

		
1
2
>>> list=["abc","xyz","aba","1221"]
>>> s=0
>>> for i in list:
	if i[0]==i[-1]:
		s+=1
        print(s)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> 
>>> list=["abc","xyz","aba","1221"]
>>> s=0
>>> for i in list:
	if i[0]==i[-1]:
		s+=1

	
>>> print(s)
2
>>> 
>>> list1=[1,2,3,4,5]
>>> list2=[5,6,7,8,9]
>>> r=false
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    r=false
NameError: name 'false' is not defined
>>> r="false"
>>> for i in list1:
	for j in list2:
		if i==j:
			r="true"

			
>>> print(r)
true
>>> 
>>> 
>>> list1=[7,8,120,25,44,20,27]
>>> list2=[x for x in list1 if x%2!=0]
>>> print(list2)
[7, 25, 27]
>>> list3=[x for x in list1 if x%2==0]
>>> print(list3)
[8, 120, 44, 20]
>>> 
>>> 
>>> l=list(input().split())

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    l=list(input().split())
TypeError: 'list' object is not callable
>>> list=["Enjoying","Python"]
>>> list.append["good"]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    list.append["good"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list=["I","Love","Python"]
>>> list2=["it","is","intresting"]
>>> list1=list+list2
>>> print(list1)
['I', 'Love', 'Python', 'it', 'is', 'intresting']
>>> print(list1*2)
['I', 'Love', 'Python', 'it', 'is', 'intresting', 'I', 'Love', 'Python', 'it', 'is', 'intresting']
>>> print(list2)
['it', 'is', 'intresting']
>>> print(list1)
['I', 'Love', 'Python', 'it', 'is', 'intresting']
>>> list1.append("programming skills")
>>> print(list1)
['I', 'Love', 'Python', 'it', 'is', 'intresting', 'programming skills']
>>> 