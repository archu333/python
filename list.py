Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 16:30:00) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5]
>>> print(l[2])
3
>>> print(l[3])
4
>>> print(l[7])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(l[7])
IndexError: list index out of range
>>> list=[11,22,33,44,55]
>>> print(list[0:3])
[11, 22, 33]
>>> print(list[:5])
[11, 22, 33, 44, 55]
>>> print(list[:4])
[11, 22, 33, 44]
>>> print(list(0:2)]
SyntaxError: invalid syntax
>>> print(list[0:2])
[11, 22]
>>> list1=[11,22]
>>> list2=[33,44]
>>> list3=list1+list2
>>> print(list3)
[11, 22, 33, 44]
>>> list3=list1*2
>>> print(list3)
[11, 22, 11, 22]
>>> list3=list2*2
>>> print(list3)
[33, 44, 33, 44]
>>> list=[1,2,3,4,5]
>>> print(2 in list)
True
>>> print(33 in list)
False
>>> print(43 not in list)
True
>>> print(3 not in list)
False
>>> list=[1,2,3,4,5]
>>> for i in list:
	print(i.end=" ")
	
SyntaxError: keyword can't be an expression
>>> trav=[1,2,3,4,5]
>>> for i in trav:
	print(i,end=' ')

	
1 2 3 4 5 
>>> for i in trav:
	print(i,end=',')

	
1,2,3,4,5,
>>> cop=[10,20,30,40,50]
>>> print(len(cop))
5
>>> print(min(cop))
10
>>> print(max(cop))
50
>>> print(sum(cop))
150
>>> lmr=[10,20,40,50,60,43,8,93,50,50]
>>> lmr.append(30)
>>> print(lmr)
[10, 20, 40, 50, 60, 43, 8, 93, 50, 50, 30]
>>> print(lmr.count(50))
3
>>> ext=[3,4,5,6]
>>> lmr.extend(ext)
>>> print(lmr)
[10, 20, 40, 50, 60, 43, 8, 93, 50, 50, 30, 3, 4, 5, 6]
>>> print(lmr.index(50))
3
>>> lmr.insert(2,30)
>>> print(lmr)
[10, 20, 30, 40, 50, 60, 43, 8, 93, 50, 50, 30, 3, 4, 5, 6]
>>> lmr.reverse()
>>> print(lmr)
[6, 5, 4, 3, 30, 50, 50, 93, 8, 43, 60, 50, 40, 30, 20, 10]
>>> lmr.sort()
>>> print(lmr)
[3, 4, 5, 6, 8, 10, 20, 30, 30, 40, 43, 50, 50, 50, 60, 93]
>>> lmr.pop(7)
30
>>> print(lmr)
[3, 4, 5, 6, 8, 10, 20, 30, 40, 43, 50, 50, 50, 60, 93]
>>> del list[10])
SyntaxError: invalid syntax
>>> del list[10]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    del list[10]
IndexError: list assignment index out of range
>>> del lmr[10]
>>> print(lmr)
[3, 4, 5, 6, 8, 10, 20, 30, 40, 43, 50, 50, 60, 93]
>>> del lmr[11]
>>> print(lmr)
[3, 4, 5, 6, 8, 10, 20, 30, 40, 43, 50, 60, 93]
>>> lmr.remove(11)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    lmr.remove(11)
ValueError: list.remove(x): x not in list
>>> list.remove(lmr)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list.remove(lmr)
ValueError: list.remove(x): x not in list
>>> list.remove(3)
>>> list.remove(4)
>>> list.remove(5)
>>> list.remove(6)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list.remove(6)
ValueError: list.remove(x): x not in list
>>> list.remove(20)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list.remove(20)
ValueError: list.remove(x): x not in list
>>> 
>>> list.remove(3)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    list.remove(3)
ValueError: list.remove(x): x not in list
>>> print(lmr)
[3, 4, 5, 6, 8, 10, 20, 30, 40, 43, 50, 60, 93]
>>> lmr.remove(3)
>>> print(lmr)
[4, 5, 6, 8, 10, 20, 30, 40, 43, 50, 60, 93]
>>> lmr.remove(30)
>>> print(lmr)
[4, 5, 6, 8, 10, 20, 40, 43, 50, 60, 93]
>>> lmr.remove(20)
>>> print(lmr)
[4, 5, 6, 8, 10, 40, 43, 50, 60, 93]
>>> del lmr
>>> aa=[x for x in range(10)]
>>> print(aa)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> aa=[x*x for x in range(20)]
>>> print(aa)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
>>> aa=[x for x in range(20) if x%2==0]
>>> print(aa)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> list=[10,22,24,-23]
>>> sum=0
>>> for x in list:
	sum+=x
	print(sum)

	
10
32
56
33
>>> list=[3,1,2,3]
>>> p=1
>>> for i in list:
	p*=i
    print(p)
    
SyntaxError: unindent does not match any outer indentation level
>>> list=[3,1,2,3]
>>> p=1
>>> for i in list:
	p*=i
	print(p)

	
3
3
6
18
>>> 