# ##############################     1
# # a=1
# # while a <= 100:
# #     print(a)
# #     a=a+1


# ##############################   2
# # for i in range(1,101):
# #     print(i)

# ##############################   3

# # a=100
# # c=a
# # print(c)
# # b=True
# # while a>=b:
# #     a=a-b
# #     print(c-a)

# ################################  4
# # a=1
# # while True :
# #     print(a)
# #     a+=1
# #     if a>100:
# #         break
# # ##########################################################################################################
# # a=int(input("enter ur number"))
# # b=int(input("enter ur number that number u take multiple"))
# # for i in range(1,a+1):
# #     if i%b==0:
# #         print("multiple of 7 is that:-",i)

# ##############################################
# # a=int(input("enter ur number where are u want the multiple"))
# # b=int(input("enter ur number form want the multiple"))
# # c= int(input("enter the number do u want multiple"))
# # while a<=b:
# #     a+=1
# #     if a%c==0:
# #         print(a)
# ###############################################

# # a=int(input("enter ur number"))
# # c=a
# # # print(c)
# # b=True
# # while a>=b:
# #     a=a-b
# #     d=c-a
# #     # print(d)
# #     if d%7==0:
# #         print(d)

# # ##################################################
# # for i in range(101):
# #     if i%7==0:
# #         print(i)
# ###################################################


# # num = int(input("enter ur number"))
# # sum = 0
# # while(num > 0):
# #     sum += num
# #     num -= 1
# # print("The sum is", sum)
# ####################################
# # a=1
# # sum=0
# # while a<=100:
# #     sum=sum+a
# #     a+=1
# # print(sum)
# ################################
# # a=1
# # sum=0
# # while a<=100:
# #     sum=sum+a
# #     print(sum)
# # #     a+=1
# #################################
# # sum=0
# # for i in range(1,101):
# #     sum=sum+i
# # print(sum)

# ###############################################################################################################

# # a=int(input("dallo number"))
# # sum=0
# # for i in range(1,a+1,1):
# #     i=int(input("enter ur numbers"))
# #     sum=sum+i
# # print(sum)

# # #####################################
# # a=0
# # b=0
# # c=int(input("enter ur number range"))
# # while a<c:
# #     d=int(input("enter ur numbers "))
# #     b=b+d
# #     a+=1
# #     print("total number of sum",b)

# ########################################

# # a=0
# # while a<100:
# #     a+=1
# #     if a%2==0:
# #         print(-a)
# #     else:
# #         print(a)

# ########################################

# # for i in range(1,101):
# #     if i%2==0:
# #         print(-i)
# #     else:
# #         print(i)

# ########################################


# # a=100
# # c=a
# # b=True
# # while a>=b:
# #     a=a-b
# #     d=c-a
# #     if d%2==0:
# #         print(-d)
# #     else:
# #         print(d)

# ########################################
# # a=0
# # for i,y in zip(range(1,10,2),range(2,10,2)):
# #     print(i,-y) 
# # ########################################
# # a=int(input('from where '))
# # b=int(input( 'till how much'))
# # while True:
# #     a+=1
# #     if a%2==0:
# #         print(-a)
# #     else:
# #         print(a)
# #     if a==b:
# #         break
# ############################################

# # a=556
# # while a<656:
# #     b=a-555
# #     a+=1
# #     if b%7==0:
# #         print(b)

# # ###########################################

# # for i in range(557,657,1):
# #     a=i-556
# #     if a%7==0:
# #         print(a)

# # #########################################
# # a=input()
# # b=""                                                  #VICKY
# # for n in a:
# #     if n in "qwertyuiopasdfghjklzxcvbnm":
# #         b+=n
# #     else:
# #         k=ord(n)
# #         i=k-32
# #         print(chr(i))
# ############################################
#                                 #HALF PART#
# # str=input("enter ur string")
# # for i in str:
# #     c=ord(i)
# #     # print(c)
# #     if c>=65 and c<=122:
# #         c+=32
# #         print(chr(c),end="  ")
# ###############################################

# # str=input("enter ur string    ")
# # for i in str:
# #     c=ord(i)
# #     if c>=65 and c<=91:
# #         print(chr(c+32),end=" ")
# #     else:
# #         print(chr(c-32),end=" ")

# ################################################

# # a='abcdefghijklmnopqrstuvwxyz'
# # b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # c=input()
# # for i in c:
# #     if i in a:
# #         d=a.index(i)
# #         print(b[d],end='')
# #     else:
# #         d=b.index(i)
# #         print(a[d],end='')
# # print(' ')

# # ##################################################

# # a = 6
# # for i in range(a):
# #     for j in range(i):
# #         print("#", end=' ')
# #     print('')

# ##################################################

# # for i in range(1,5):
# #     print("#"*i)
# #     i+=1

# #################################################

# # a=1
# # while a<5:
# #     print("#"*a)
# #     a+=1

# ################################################
# # a=input("enter ur number")
# # b=int(input("enter ur number jaha tak"))
# # c=1
# # while True:
# #     print(a*c)
# #     if c==b:
# #         break
# #     c+=1

# ###########################################################################################################

# # a=1
# # while a<100:
# #     a+=1
# #     if a%3==0 and a%7==0:
# #         print("navgurukul",a)

# #     elif a%7==0:
# #         print("gurukul",a)

# #     elif a%3==0:
# #         print("nav",a)
# #     else:
# #         print(a)

# ##########################################

# # a=int(input("enter ur number"))
# # b=int(input("enter ur number kaha tak"))
# # while True:
# #     a+=1
# #     if a%3==0 and a%7==0:
# #         print("navgurukul",a)
# #     elif a%7==0:
# #         print("gurukul",a)

# #     elif a%3==0:
# #         print("nav",a)
# #     else:
# #         print(a)
# #     if a==b:
# #         break


# ##############################################


# # a=100
# # c=a
# # b=True
# # while a>=b:
# #     a=a-b
# #     d=c-a
# #     if d%3==0 and d%7==0:
# #         print("navgurukul",d)
# #     elif d%7==0:
# #         print("gurukul",d)

# #     elif d%3==0:
# #         print("nav",d)
# #     else:
# #         print(d)

# ###############################################


# # for d in range(1,100):
# #         if d%3==0 and d%7==0:
# #             print("navgurukul",d)
# #         elif d%7==0:
# #             print("gurukul",d)

# #         elif d%3==0:
# #             print("nav",d)
# #         else:
# #             print(d)


# #############################################################################################################
# # a=156
# # while a<256:
# #     b=a-155
# #     a+=1
# #     print(b)

# ##################################

# # for i in range(156,256,1):
# #     b=i-155
# #     print(b)

# ###################################

# # a=156
# # while True :
# #     print(a-155)
# #     a+=1
# #     if a>255:
# #         break

# ###################################
# # a=6
# # while a>1:
# #     a-=1
# #     print(str(a)*5)
# # ###################################

# # for i in range(5,0,-1):
# #     print(str(i)*5)

# #####################################



# #########3#######################           NEW LIST                        ################################


# # b=0
# # numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# # for i in numbers:
# #     b+=1
# # print(b)

# ##########################################
# # c=0
# # numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# # while numbers[c:]:
# #     c+=1
# # print(c)
# # ########################################################
# # a=0
# # numbers=[0,50,"", 40, 23, 70, 56, 12, 5, 10, 7,2000000]
# # while numbers:
# #     # print(numbers)
# #     numbers.pop()
# #     a+=1
# # print(a)
    
# # #  ############################################################   
# # a=0
# # numbers=[0,50,"", 40, 23, 70, 56, 17, 5, 10, 7,2000000,9]
# # for i in numbers:
# #     # print(i)
# #     numbers.remove(i)
# #     numbers.append(i)
# #     print((numbers))

# #     a+=1
# # # print(numbers)
# # print(a)
# #############################################################################################################
# # numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# # for i in numbers:
# #     if i>20 and i<40:
# #         print(i)    

# ###########################################################################################################
# # numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# # b=numbers[0]
# # for i in numbers:
# #     if i>b:
# #         b=i
# # print(b)
# # #############################################

# # # numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# # # numbers.sort()
# # # print(numbers[-1])
# # ###########################33################

# # numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# # a=0
# # b=numbers[a]
# # while a<len(numbers):
# #     if numbers[a]>b:
# #         b=numbers[a]
# #     a=a+1
# # print(b)
# #################################################
# # numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# # numbers.sort()
# # print(numbers[-2])

# #####################################################################################################
# # name=["n","i","t","i","n"]
# # b=[]

# # light=len(name)+1
# # for x in range(-1,-light,-1):
# # 	b.append(name[x])
# # print(b)	
# # if name==b:
# # 	print("Palindrome hai")
# # else:
# # 	print("Nahi hai")

# # ######################################################################################
# # size=int(input("enter ur number"))
# # a=[]
# # for i in range(size):
# #     b=int(input("enter number"))
# #     a.append(b)
# # a=[8,5,63,54,52]
# # for i in range(len(a)):
# #     for j in range(len(a)-i-1):
# #         if a[j]>a[j+1]:
# #             c=a[j]
# #             a[j]=a[j+1]
# #             a[j+1]=c
# # print(a)
# #########################################################
# # palindrome
# # a=input("enter ur string")
# # b=input("enter ur string2 ")
# # c=0
# # c1=0
# # for i in range(97,123):
# #     if chr(i) in a and chr(i) in b:
# #         c+=1
# #         print(c)
# #         if a.count(chr(i)) == b.count(chr(i)):
# #             c1+=1
# #             print(c1)
# # if c==c1:
# #     print("its a anagram")
# # else:
# #     print("its not anagram")

# # #####################################3
# # a=input("enter ur number1:-")
# # b=input("enter ur string2:-")
# # c=[]
# # d=[]
# # for i in range(len(a)):
# #     c.append(a[i])
# # for j in range(len(b)):
# #     d.append(b[j])
# #     if len(c)==len(d):
# #         for letter in c:
# #             if letter in d:
# #                 d.remove(letter)
# # if len(d)==0:
# #     print("its a anagram")
# # else:
# #     print("its not a anagram")

# # a=input("enter ur string1:-")
# # b=input("enter ur string2:-")
# # c=""
# # for i in a:
# #     c+=i
# # if (c==b[::-1]):
# #     print("its anagram")
# # else:
# #     print("its not anagram")
# ###########################################################################3
# # binary_number = [1, 0,1]
# # c=0
# # for i in binary_number:
# #     c=2*c+i
# #     print(c)




# # ##############################################################################
# # a=[]
# # for i in range(3):
# #     b=[]
# #     for j in range(3):
# #         j=int(input("enter ur number"))
# #         b.append(j)
# #     a.append(b)
# #     print(a,end=" ")

# # for i in range(3):
# #     for j in range(3):
# #         print(a[i][j],end=" ")
# #     print()
# # sumd1=0
# # sumd2=0
# # for i in range(3):
# #     for j in range(3):
# #         if i==j:
# #             sumd1=sumd1+a[i][j]
# #         if i+j==3-1:
# #             sumd2=sumd2+a[i][j]
# # if sumd1!=sumd2:
# #     f=1
# # else:
# #     for i in range(3):
# #         sumr=0
# #         sumc=0
# #         for j in range(3):
# #             sumr=sumr+a[i][j]
# #             sumc=sumc+a[j][i]
# #         if sumr!=sumd1:
# #             f=1
# #         elif sumc!=sumd1:
# #             f=1
# #         else:
# #             f=0
# # if  f==0:
# #     print("its a magic square")
# # else:
# #     print("its not a magic square")


# # #############################################
# # magic=[[2,7,6],[9,5,1],[4,3,8]]
# # a=[]
# # for x in magic:
# # 	sum=0
# # 	for y in x:
# # 		sum+=y
# # 	a.append(sum)
# # print(a)
# # b=[]
# # for x in range(len(magic)):
# # 	sum=0
# # 	for y in range(len(magic[x])):
# # 		if (y==0 and (x==0 or x==1 or x==2)):
# # 			sum+=magic[x][y]
# # 		elif (y==1 and (x==0 or x==1 or x==2)):
# # 			sum+=magic[x][y]
# # 		else:
# # 			sum+=magic[x][y]				
# # 	b.append(sum)
# # print(b)
# # c=[]
# # sum=0
# # sump=0
# # for x in range(len(magic)):
# # 	for y in range(len(magic[x])):
# # 		if (y==0 and x==2) or (y==1 and x==1) or (y==2 and x==0):
# # 			sum+=magic[x][y]
# # 		if (y==0 and x==0) or (y==1 and x==1) or (y==2 and x==2 ):
# # 			sump+=magic[x][y]
# # c.append(sum)
# # c.append(sump)
# # print(c)
# # g=a==b
# # if g:
# # 	print("This is magic Square")
# # else:
# # 	print("This is not magic Square")



# # # s="navgurukul"
# # # b=0
# # # while b<= len(s):
# # #     if s[b]== "g":
# # #         print(b)
# # #     elif s[b]=="u":
# # #         print(b)
# #     elif s[b]== "u":
# #         print(b)
# #     elif s[b]=="l":
# #         print(b+1)
# #         break
# #     b+=1


# ###################################################################





# # a=[]
# # for i in range(3):
# #     z=[]
# #     for j in range(3):
# #         j=int(input("enter ur number"))
# #         z.append(j)
# #     a.append(z)
# # c=0
# # d=0
# # e=0
# # g=0
# # h=0
# # f=0
# # k=2
# # l=0
# # m=0
# # n=0
# # for i in range(len(a)):
# #     for j in range(len(a[i])):
# #         if i==0:
# #             c+=a[i][j]
# #         if i==1:
# #             d+=a[i][j]
# #         if i==2:
# #             e+=a[i][j]
# #         if i==j:
# #             g+=a[i][j]
# #         if j==k:
# #             # print(a[i][j])
# #             f+=a[i][j]
# #             k-=1
# #         if j==0:
# #             l+=a[i][j]
# #         if j==1:
# #             m+=a[i][j]
# #         if j==2:
# #             n+=a[i][j]
# # if c==d==e==g==f==m==l==n:
# #     print("its a magic square")
# # else:
# #     print("its a not magic square")


# # ######################################################################
# # n=int(input("enter number till now"))
# # a=[]
# # for i in range(n):
# #     z=[]
# #     for j in range(n):
# #         j=int(input("enter ur number"))
# #         z.append(j)
# #     a.append(z)
# # print(a)
# # for i in range(n):
# #     for j in range(n):
# #         print(a[i][j],end=" ")
# #     print()
# # sumd1=0
# # sumd2=0
# # for i in range(n):
# #     for j in range(n):
# #         if i==j:
# #             sumd1=sumd1+a[i][j]
# #         if i+j==n-1:
# #             sumd2=sumd2+a[i][j]
# # if sumd1!=sumd2:
# #     f=1
# # else:
# #     for i in range(n):
# #         sumr=0
# #         sumc=0
# #         for j in range(n):
# #             sumr=sumr+a[i][j]
# #             sumc=sumc+a[j][i]
# #         if sumr!=sumd1:
# #             f=1
# #         elif sumc!=sumd1:
# #             f=1
# #         else:
# #             f=0
# # if  f==0:
# #     print("its a magic square")
# # else:
# #     print("its not a magic square")

# ####################################    UNIVERSAL MAGIC SQUARE  ######################################

# # a=int(input("enter ur number till Now:-"))
# # b=[]
# # for i in range(a):
# #     c=[]
# #     for j in range(a):
# #         j=int(input("enter ur numbers:-"))
# #         c.append(j)
# #     b.append(c)                 
# #                             ###  DAIGONALS
# # sumd1=0
# # sumd2=0
# # for i in range(a):
# #     for j in range(a):
# #         if i==j:
# #             sumd1=sumd1+b[i][j]
# #         if j+1==a-1:
# #             sumd2=sumd2+b[j][i]
# # if sumd1!=sumd2:
# #     f=1
# #                                                          #### ROWS AND COLUMN
                                                        
                            
# # else:
# #     for i in range(a):
# #         sumr=0
# #         sumc=0
# #         for j in range(a):
# #             sumr+=b[i][j]
# #             sumc+=b[i][j]
# #                                                           #### COMPARE BOTH
# #         if sumc!=sumd1:
# #             f=1
# #         if sumr!=sumd1:
# #             f=1
# #         else:
# #             f=0
# # if f==0:
# #     print("its a magic square")
# # else:
# #     print("its not a magic square")

# ###############################################################
# # list1 = [1,2,3,4,5,6]
# # list2 = [2,3,1,0,6,7]
# # c=[]
# # for i in list1:
# #     if i not in list2:
# #         c.append(i)
# # print(c)
# ###################################
# # list1 = [1,2,3,4,5,6]
# # list2 = [2,3,1,0,6,7]
# # for i in list1:
# #     if i not in list2:
# #         print(i)
# ##################################
# # marks = [
# #     [78, 76, 94, 86, 88],
# #     [91, 71, 98, 65, 76],
# #     [95, 45, 78, 52, 49]
# # ]
# # b=0
# # for i in marks:
# #     for j in i:
# #         b+=j
# # print(b)


# # marks = [
# #     [78, 76, 94, 86, 88],
# #     [91, 71, 98, 65],
# #     [95, 45, 78]
# # ]
# # b=0
# # for i in marks:
# #     for j in i:
# #         b+=j
# # print(b)


# # n = [10, 11, 12, 13, 14, 17, 18, 19]
# # a=[]
# # for i in range(len(n)//2):
# #     b=[]
# #     for j in range(len(n)):
# #         if n[j]+n[i]==30:
# #             b.append(n[i])
# #             b.append(n[j])
# #     if len(b)!=0:
# #         a.append(b)
# # print(a)

# # a=[10,11,12,13,14,17,18,19]
# # number=30
# # Matrix=[]
# # for x in range(len(a)-4):
# # 	b=[]
# # 	for y in range(len(a)):
# # 		if a[x]+a[y]==number:
# # 			b.append(a[x])
# # 			b.append(a[y])
# # 			Matrix.append(b)
# # print(Matrix)

# # a=[10,11,12,13,14,17,18,19]
# # for i in range(len(a)//2):
# #     print(i)


# # elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# # even=0
# # odd=0
# # for i in elements:
# #     if i%2==0:
# #         even+=1
# #     if i%2!=0:
# #         odd+=1
# # print("there are odd numbers:-",even)
# # print("there are even numberd:-",odd)

# ##########################################################################
# # elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# # even_sum=0
# # odd_sum=0
# # for i in elements:
# #     if i%2==0:
# #         even_sum+=i
# #     if i%2!=0:
# #         odd_sum+=i
# # print("That is a sum of even numbers:-",even_sum)
# # print("That is a sum of odd numbers:-",odd_sum)

# # ###########################################################################
# # elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# # odd=0
# # even=0
# # even_sum=0
# # odd_sum=0
# # for i in elements:
# #     if i%2==0:
# #         even_sum+=i
# #         even+=1
# #     if i%2!=0:
# #         odd_sum+=i
# #         odd+=1
# # print("there is a average of even numbers:-",even_sum/even)
# # print("there is a average of odd numbers:-",odd_sum/odd)
# #############################################################################
# # kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# # a=0
# # b=0
# # c=0
# # for x in kitna_paisa_hai:
# #     if x > 9999999 and x < 999999999:
# #         a+=1
# #     elif x > 59999 and x < 9999999:
# #         b+=1
# #     else:
# #         c+=1
# # print("corepati:-",a,"lakhpati:-",b,"dilwale:-",c,end="        ")
# #########################################################################################

# # print(char_list[(len(char_list)-1)])
# # a=[1,2,3,4,5,6,78,9]
# # a[2]==100
# # print(a)
# # a=[]
# # for i in char_list:

# # a=[1,2,3,4,5,6]

# # g=0
# # while g<len(a):
# #     print(a[g])
# #     g+=1

# # b=[1,2,3,4,5]
# # b.insert(3, "Dipesh")
# # print(b)

# # a=["dipesh","rangwani","don_no_1","in","chutiya","city","Zebra_arif","ufh"]
# # a.sort()
# # print(a)

# ###########################################################################################

# # char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# # lu=[]
# # vv=[]
# # for i in char_list:
# #     if i not in lu:
# #         lu.append(i)
# #         v=0
# #         for j in char_list:
# #             if i==j:
# #                 v+=1
# #         vv.append([i,v])  
# # print(vv)


# ##########################################################
# # n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# # a=[]
# # for i in n:
# #     if i not in a:
# #         a.append(i)
# # print(a)

# ##################################

# # n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# # a=[]
# # for i in n:
# #     if n.count(i)>1:
# #         n.remove(i)
# #         a.append(i)
# # print(a)

# #######################################################################################################
# # mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# # b=mainStr.replace("over", "on")
# # print(b)

