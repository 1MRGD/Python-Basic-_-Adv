# a = " " 
# print(ord(a))

# Each Character in a string with its own unicode number . That's why string use more memory than the int 

# a = "COLLAGE"
# print(a[0])
# print(a[-1])

# string indexing = its generally two type Negative 
# One is Positive and Negative Indexing
# Generally Positive Starts with 0-n-1
# Negative is just opposite with -1 to -10

#================================================================


# String Slicing 
#---------------
 
# a = 'COLLEGE'

# print(a[3:6:1])

# print(a[::2])

# a1 = "Hello How Are You"

# How

# print(a1[6:9:1])

# #you

# print(a1[14:17:1])

# #Hello

# print(a1[0:5:1])



#==========

#Type Conversion
#---------------


#INT()-> Whole Number
#====================

# a = '12'
# b = int(a)
# print(a)
# print(b)
# print(type(a)) 
# print(type(b))



#In string We Can Only Convert STring if it holds valid integer
#You can convert float values to int

# a = 12.4
# a = int(a)
# print(a) //12
# print(type(a)) //int

#float() -> Decimal Number.
#==========================
 
# a = "12"
# a = float(a) //12.0

# print(a)


#String()
#========

#Anything Can be Converted into String

# a = 123
# b = 34.5
# c = 12 + 34j
# d = True

# a = str(a)
# b = str(b)
# c = str(c)
# d = str(d)

# print(a)
# print(b)
# print(c)
# print(d)


#Bollean
#=======
# a = 123
# b = 34.5
# c = 12 + 34j
# d = True
# e=''
# f="hello"

# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(d))
# print(bool(e))
# print(bool(f))


#In Bool The False appears in 7 Reason 
#False,0,0.0,"",[],(),{}
#Expect that Everything will be True

#Implicit
# a =12
# print(a/2)
#int/int ->FLoat

#Explicit
# a = 12
# a =str(a)
# print(a) # "12"

