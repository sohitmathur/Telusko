decorator

def dev(a,b):
    print(a/b)

def smart_dev(func):

    def inner_dev(a,b):
      if (a<b):
        a,b=b,a
        return func(a,b)

    return inner_dev
dev=smart_dev(dev)

dev(4,5)

how to find unique number in two list
1.
def unique_num(l1,l2):
    output=[]
    for i in l1:
        if i not in output:
            output.append(i)
    for i in l2:
        if i not in output:
            output.append(i)
    return output
l1=[1,2,3,4,5,2,6]
l2=[7,2,8,9,1,9,10]
print(unique_num(l1,l2))

2.
list1=[1,2,3,4,5,6]
list2=[7,2,8,9,1,9,10]
new_list=(list1+list2)
unique_element=set(new_list)
print(list(unique_element))
def unique_ele(list1,list2):
    unique_lis=list(set(list1+list2))
    return unique_lis

list1=[1,2,3,4,5,6]
list2=[7,2,8,9,1,9,10]
unique=unique_ele(list1,list2)
print(unique)

def unique_num(numbers):
    unique_list=[]
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
            sorted_num=sorted(unique_list)
    return unique_list
l=[1,2,5,54,1,2,7,3,2,7]
unique=unique_num(l)
print(unique)



def fibi():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f1=fibi()
for i in range(10):
    print(next(f1))


sort list without using sort method


for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>=list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)


l=list(map(int,input("enter the number please:").split()))
print('list is',l)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>=l[j]:
            l[i],l[j]=l[j],l[i]
print('sorted_list',l)

def largest_num(number):
    largest_ele=number[0]
    for num in number:
        if num>largest_ele:
            largest_ele=num
    return largest_ele

l=[12,5,56,4,36,1,22,4]
largest=largest_num(l)
print(f"the largest element in list is {largest}")

def check_prime_no(number):
    count=0
    if number>1:
        for i in range(1,number+1):
            if number%i==0:
                count+=1
        if count==2:
            return f"the given {number} is prime number"
        else:
            return f"the given {number} is not prime number"
user=int(input("enter the number please:"))
prime_no_indentifier=check_prime_no(user)
print(prime_no_indentifier)




n=int(input("enter the number please:"))
a=0
b=1
print(a)
print(b)
for i in range(2,n+1):
    sum=a+b
    print(sum)
    a=b
    b=sum


input='B4A3C12D'
output='ABCD1234'




s='B4A3C12D'
alphabet=[]
digit=[]
for i in s:
    if i.isalpha():
        alphabet.append(i)
    else:
        digit.append(i)
print(alphabet)
print(digit)
concat=" ".join(sorted(alphabet)+sorted(digit))
print(concat)


    input='a4b3c2'
    output='aaaabbbcc'

s = 'a4b3c2'
output = ''

for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + str(x) * d
print(output)


 s='aaaabbbccz'
previous=s[0]
output=''
c=1
i=1
while i<len(s):
    if s[i]==previous:
        c= c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
    if i==len(s)-1:
        output=output+str(c)+previous
    i=i+1
print(output)

def right_rotation(l1, num):
    output = []
    for i in range(len(l1) - num, len(l1)):
        output.append(l1[i])
    for i in range(0, len(l1) - num):
        output.append(l1[i])
    return output


l1 = [1, 2, 3, 4, 5]
num = 3
print(right_rotation(l1, num))


def genrator(n):
    for i in range(1,n+1):
        yield i*i
a=genrator(3)
print("the squre root is",next(a))
print("the squre root is",next(a))
print("the squre root is",next(a))


# Example usage
numbers_list = [1, 1, 3, 3, 4, 2, 7, 4]
result = find_non_repeating(numbers_list)

print("Non-repeating numbers:", result)
def find_non_repeating(numbers_list):
    non_repeating = []

    for number in numbers_list:
        if numbers_list.count(number) == 1:
            non_repeating.append(number)

    return non_repeating

numbers_list = [1, 1, 3, 3, 4, 2, 7, 4]
result = find_non_repeating(numbers_list)
print("Non-repeating numbers:", result)



Write a program to find the sum of 2 indexes from the list is equal to the output variable
x = [11, 13, 17, 18]
y = 35
for i in range(0, len(x)):
    for j in range(i + 1, len(x)):
        if x[i] + x[j] == y:
            print("the sum is right")
            print(i, j)




my_list=['geeks','for','geeks']x`
word='geeks'
n=2
count=0
for i in range(0,len(my_list)):
    if my_list[i]==word:
        count=count+1
    if count==n:
          del my_list[i]
print(my_list)

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizzbuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


fizzbuzz(20)

string manipulation
def string_format(s):
    l = []
    temp = s.split('_')
    for i in temp:
        l.append(i[0].lower() + i[1:].upper())
    s = ".".join(l)
    print(s)


s = 'This_Is_Good'
string_format(s)
o=tHIS.iS.gOOD


class A:
    def funtion1(self):
        print("funtion 1 is working")


class B:
    def funtion2(self):
        print("funtion 2 is working")


class C(A,B):
    def funtion3(self):
        print("funtion 3 is working")


a=A
b=B()
c=C()
c.funtion1()
c.funtion2()
c.funtion3()

open('py.txt') as f:
    s=f.read
    print(s)

f=open('py.txt','r')
s=f.read()
print(s)
f.close()

with open('py.txt') as f:
     content=f.read()
     print(content)

1.
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    without_vowels = ''.join(char for char in input_string if char not in vowels)
    return without_vowels

user_input = input("Enter a string without vowels: ")
result = remove_vowels(user_input)
print("String without vowels:", result)

2.
def duplicate_remover(string):
    vowels='aeiouAEIOU'
    no_vowel_list=''.join([char for char in string if char not in vowels])
    print(no_vowel_list)

    w_vowels=[]
    for char in string:
        if char not in vowels:
            w_vowels.append(char)
    return ''.join(w_vowels)
user_input=input("enter the string please:")
result=duplicate_remover(user_input)
print(result)



def remove_zero(lis):
    output=[]
    for num in lis:
        num=str(num)
        new_str=num.split('0')
        output.append (int("".join(new_str)))
    return output
    my_list=[201,510,10,500,807,9010]
find=remove_zero(my_list)
print(find)

for key,val in{'name':'aman','age':27,'city':'nagpur'}.items():
    print(key ,'----->', val)

        s="A3G4B2"
        o="ADGKBD"
output=''

for i in s:
    if i.isalpha():
        output=output+i
        temp=i
    else:
        output=output+chr(ord(temp)+int(i))
print(output)


s = 'a4k3b2'
# output:aeknbd
output = ''
for ch in s:
    if ch.isalpha():
        output = output + ch
        temp = ch
    else:
        d = int(ch)
        output = output + chr(ord(temp) + d)
print(output)

def check_leap_year():
    year = int(input("enter the year please:"))
    if (year % 400 == 0) and (year % 100 == 0):
        print(f"the given year {year} is a leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"the given year {year} is a leap year")
    else:
        print(f"the given year {year} is not a leap year")


check_leap_year()



try:
    # Code that may raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2

except ValueError:
    # Handle ValueError if the user enters a non-integer value
    print("Please enter valid integers.")

except ZeroDivisionError:
    # Handle ZeroDivisionError if the user tries to divide by zero
    print("Cannot divide by zero.")

else:
    # This block executes if no exception occurs in the try block
    print("Division result:", result)

finally:
    # This block always executes regardless of whether an exception occurred or not
    print("This block always executes.")

def sum(*args):
    total=0
    for i in args:
        total=total+i
    print(total)
sum(1,5,8,9)

def show(**kwargs):
    print(kwargs)
show(a=1,b=2)

def prime_num(num):
    count = 0
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1
        if count == 2:
            print(num)


print("the prime number from 1 to 50 ")
for num in range(1, 51):
    prime_num(num)

import time
def check_prime_number(n):
    t1 = time.time()
    count = 0
    if n > 1:
        for i in range(1, n + 1):
            if n % i == 0:
                count = count + 1

        if count == 2:
            print(n)
    print(time.time() - t1)


for i in range(1, 51):
    check_prime_number(i)

print(is_palindrome("iamabhishekonacallwithsohit"))
print(is_palindrome("hello"))

s = [["a", "b", "c"], [1, 2, 3]]
output={'A': 1, 'B': 2, 'C': 3}
o = dict(zip(s[0], s[1]))
print(o)

num=int(input("enter the number please:"))
count=0
for i in range(1,num):
    if i*i==num:
        count=1
        break
if count==1:
    print("its perfect square")
else:
    print("its not perfect square")

def move_zeros_to_right(l1):
    non_zeros = [i for i in l1 if i != 0]
    zeros = [i for i in l1 if i==0]
    return non_zeros + zeros

l1 = [1, 0, 0, 2, 3, 4, 0, 5]
result = move_zeros_to_right(l1)
print(result)

def string_replace(string,ch):
    output=''
    for i in string:
        if i==" ":
            output+=ch
        else:
            output+=i
    return output
text = "D t C mpBl ckFrid yS le"
ch="a"
print(string_replace(text,ch))

# 2.
import re
my = "We are looking for Python Candidate"
x = re.sub(" ", "wow", my)
print(x)

# 3.
my = "We are looking for Python Candidate"
y = my.replace(" ", "wow")
print(y)


def find_missing(input_list):
    sum_of_elements = sum(input_list)

    # There is exactly 1 number missing
    n = len(input_list) + 1
    actual_sum = (n * (n + 1)) / 2

    return int(actual_sum - sum_of_elements)


list_1 = [1, 5, 6, 3, 4]

find_missing(list_1)
# 2


def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string equals its reverse
    return cleaned_string == cleaned_string[::-1]


# Test the function
test_strings = ["racecar", "A man, a plan, a canal, Panama!", "hello", "12321"]

for test_string in test_strings:
    print(f'"{test_string}" is a palindrome:', is_palindrome(test_string))


n=[1,2,3,4,5,6,4,6,6]
print(n[1::2])

def infinate_num_genrator():
    number=0
    while True:
        yield number
        number +=1
genrator=infinate_num_genrator()
for i in range(10):
    print(next(genrator))


reverse the dictionery
dic={'animal':'dog','flower':'daisay','colour':'pink'}
l=list(dic.items())
dic2=dict(l[::-1])
print(dic2)

print me fibonaci number using recurastion upto 10

def recour(n):
    if (n<=1):
        return n
    else:
        return(recour(n-1)+recour(n-2))
n=10
for i in range(10):
    print(recour(i))

sort dictioney without using sorted



dict1={'rahul':28,'yadav':23,'abhi':24}

d=list(dict1.items())
for i in range(0,len(d)):
    for j in range(i+1,len(d)):
        if d[i]>d[j]:
            d[i],d[j]=d[j],d[i]
print(d)


input='hello,world,nitin'
print(','.join(input.split(',')[::-1]))


s='helloworld'
print(s[5::])
print(s[:5:])



multiple 2 variable with any predefined method
a=int(input("enter the number please:"))
b=int(input("enter the number please:"))
num=0
for i in range(1,b+1):
    num+=a
print(num)

s='the sun is yellow'
output=' '.join(s.split()[::-1])
print(output)


def find_anagrams(words):
    output={}
    for word in words:
        sorted_words=tuple(sorted(word))
        print(sorted_words)
        if sorted_words in output:
            output[sorted_words].append(word)
        else:
            output[sorted_words]=[word]
    return list(output.values())
input_words = ["cat", "dog", "tac", "god", "act"]
find=find_anagrams# input_words =(input_words)
print(find)

reverse list using decorator
def reverse(lis):
    if lis==[]:
        return []
    else:
        return [lis.pop()]+reverse(lis)
l1=[9,8,7,6,5,4]
find=reverse(l1)
print(find)

with open('hello.txt', 'r') as f1, open('hello2.txt', 'w') as f2:
    for line in f1:
        if 'nitin' in line:
            f2.write(line)


def str_replace(string,ch):
    output=''
    for i in string:
        if i==' ':
            i=ch
        output += i
    return output
user_input=input("enter the string please:")
ch='wow'
find=str_replace(user_input,ch)
print(find)



l1 = [{"Shirish": "Python"}, {"Shirish": None}, {"Ajay": "AWS"}, {"Ajay": None}]
l2 = {}

for d in l1:
    for key, value in d.items():
        print(key, value)

        if key not in l2 or value is not None:
            l2[key] = value

print(l2)





import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

# Create a thread
t = threading.Thread(target=print_numbers)

# Start the thread
t.start()

def most_reptating_num(numbers):
    count=0
    frequency=None
    for num in set(numbers):
        temp=numbers.count(num)
        if temp>count:
            count=temp
            frequency=num
    return frequency
nums = [1, 2, 2, 3, 3, 3,3,3,4,4,4,4]
print(most_reptating_num(nums))

def string_manipulation(string):
    words = string.split(' ')  # Split the string into words
    output = ''

    for word in words:
        for i, char in enumerate(word):
            # Check if the index is odd or even
            if i % 2 == 0:
                output += char.lower()  # Even index (0-based) -> lowercase
            else:
                output += char.upper()  # Odd index (0-based) -> uppercase
        output += ' '  # Add a space after each word

    return output.strip()  # Remove any trailing spaces


st = 'hello world'
print(string_manipulation(st))





def second_largestt(num):
    largest=float('-inf')
    second_largest=float('-inf')
    for i in num:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
    return second_largest
l1=[12,5,6,3,2,7]
print(second_largestt(l1))


def recor(n):
    if n>50:
        return
    print(n)
    recor(n+1)
recor(1)


How can you create a custom exception in Python?

class AgeError(Exception):
    "Raised exception if the person is less than 18"
    pass
try:
    age=int(input("enter the age:"))
    if age<18:
        raise AgeError
except AgeError:
    print("person is not eligiable to vote")
else:
    print("person is eligiable to vote")

arr = [1, 3, 5, 2, 3, 6, 5, 1]
def find_duplicate(numbers):
    output=[]
    for num in set(numbers):
        if numbers.count(num)>1:
            output.append(num)
    return output
print(find_duplicate(arr))

def anagram():
    str1 = input("enter the string please:")
    str2 = input("enter the string please:")

    if len(str1) != len(str2):
        print("the given string is not an anagram")
    else:
        if sorted(str1) == sorted(str2):
            print(f"the given string is an anagram")
        else:
            print(f"the given string is not an anagram")


anagram()

def sum_array(lis):
    found = False
    for i in range(0, len(lis)):
        for j in range(i + 1, len(lis)):
            if lis[i] + lis[j] == y:
                print(i, j)
                found = True

    if not found:
        print(-1, -1)


l1 = [14, 5, 6, 7, 8, 4]
y = 56
sum_array(l1)


def convert_string(s):
    vowels='aeiouAEIOU'
    if len(s)%2==0:
        mid=len(s)//2
        print(mid)
        s=s[mid:]+s[:mid]
    else:
        s=s[::-1]
    result=''.join('*'if char in vowels else char for char in s)
    return result
user_input=input("enter the string please:")
print(convert_string(user_input))

Given a string s, return the longest palindromic substring in s.
Example:
Input: s = "babad"
Output: "bab" (or "aba")
Solution Approach:
Use the center expansion method to check for palindromes by expanding around each character and pair of characters.

def function(string):
    vowels = 'aeiouAEIOU'
    # Remove vowels from the input string
    no_vowels = ''.join([i for i in string if i not in vowels])
    # Split the string into desired groups
    output = [no_vowels[:1], no_vowels[1:3], no_vowels[3:]]
    return output

input_string = 'sedrabst'
print(function(input_string))
output=['s', 'dr', 'bst']



 

def flatten_list(lst):
    output=[]
    for item in lst:
        if isinstance(item,list):
            output.extend(flatten_list(item))
        else:
            output.append(item)
    return output

def count_frequency(flatten_list):
    count={}
    for i in flatten_list:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
l1=[1,5,1,2,5,4,5,1]

x=flatten_list(s)
result=count_frequency(x)
print(result)


