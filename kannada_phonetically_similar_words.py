#program to generate phonetically similar words of a given kannada  word

# input_word = input()
# word = list(input_word)
word_set = []
with open("converted_word.txt","r") as cv_file:
    # print(cv_file)
    stripped = (line for line in cv_file)
    # t = stripped.split(",")
    # print(t)
    for k in stripped:
        # print(k.strip("\n"))
        word_set.append(k.strip("\n"))
        # print(type(word))
        # print()
        # word_set.append(word)
    # for i in cv_file:
    #     print(i)
    #     word_set.append(i)

# print(word_set[1])
# print("hello")
new_word = []
label = []
num =0
for w in word_set:
    word = list(w)
    # print(word)
    # print(num)
    k=0
    for i in word:

        if i == word[k-1]:
            if(i=="o" ):
                new = word.copy()
                new.pop(k-1)

                new.pop(k-1)

                new.insert(k-1,"u")
                new = ''.join(map(str,new))
                new_word.append(new)
                label.append(num)

            k = k+1
        elif((k<len(word)-1 ) and i+i ==  word[k+1]+i   ):
            new = word.copy()
            new.pop(k)
            new1 = ''.join(map(str,new))
            new_word.append(new1)
            label.append(num)

            if (i=='a'or i == 'e'  or  i == 'o'   ):


                new1 = new.copy()
                new1.insert(k+1,i)

                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)

            if (k<(len(word)-1) and k<(len(word)-1) and  word[k+1]=="a")    :

                new1 = new.copy()

                new1.insert(k+1,'h')

                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)

            if (k<(len(word)-1) and i == 'e'):

                new1 = new.copy()

                new1.pop(k)
                new1.insert(k,'i')

                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)




            if(i=="a" and (new[k-1]=='b' or new[k-1]=='c' or new[k-1]=='d'
            or new[k-1]=='f' or new[k-1]=='g' or new[k-1]=='j' or new[k-1]=='k' or
            new[k-1]=='l' or new[k-1]=='m' or new[k-1]=='n' or new[k-1]=='p' or new[k-1]=='q' or
            new[k-1]=='r' or new[k-1]=='s' or new[k-1]=='t' or new[k-1]=='v' or
            new[k-1]=='w' or new[k-1]=='x' or new[k-1]=='y' or new[k-1]=='z' ))    :

                new1 = new.copy()

                new1.insert(k,'ha')

                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)

            if(i == "e" and k<(len(word)-1) and new[k+1] == "y")    :

                new1 = new.copy()

                new1.pop(k+1)
                new1.insert(k+1,'a')

                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)

            if( i =="y"  and k<(len(word)-1) and  new[k+1] == "e")    :

                new1 = new.copy()

                new1.pop(k)


                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)


            if(i == "h" and k<(len(word)-1)and  new[k+1]=="r")    :

                new1 = new.copy()

                new1.pop(k)


                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)


            if(i == "h" and k<(len(word)-1) and  new[k+1]=="a")    :

                new1 = new.copy()

                new1.pop(k)


                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)


            if(i == "a" and k<(len(word)-1) and  new[k+1]=="i")    :

                new1 = new.copy()

                new1.pop(k)


                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)


            if(i == "y")    :

                new1 = new.copy()

                new1.pop(k)
                new1.pop(k)
                new1.pop(k-1)

                new1.insert(k,"a")

                new1.insert(k,"i")

                new1.append("a")

                new1.append("h")

                new1 = ''.join(map(str,new1))

                new_word.append(new1)
                label.append(num)


            if(k<len(word)):
                k = k+1
        else:

            if(k<(len(word)-1) and (i == 'b' or i=="c" or i == "d" or i =="f" or i == "g" or i == "j" or i == "k"   or   i == "p" or i == "q"  or i == "s" or i == "t" or   i == "w"  or i == "x"  or i == "z") and (word[k+1]!="h")):
                new = word.copy()

                new.insert(k+1,"h")

                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)



            if (i=='a'or i == 'e'   or i == 'o'  ):

                new = word.copy()

                new.insert(k+1,i)

                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)


            if (k<(len(word)-1) and word[k+1]=="a" and i != "h" and (i != "r" and i != "y" and i!="l" and  i!="v" ) )    :


                new = word.copy()

                new.insert(k+1,'h')

                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)


            if (k<(len(word)-1) and i == 'e'):

                new = word.copy()

                new.insert(k,'i')

                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)


            # if((new_word[len(new_word)]=='a'or new[k] == 'e'  or new[k]== 'i' or new[k]== 'o' or new[k] == 'u')and(k<(len(word)-1) or k<(len(word)-1) )and(i+i == new[k+1]+i or i+i == new[k-1]+i or i+i+i == new[k-1]+i+new[k+1]) ):
            #     print("5")
            #     new = word.copy()
            #     print("new",new)
            #     new.pop(k)
            #     print("after new",new)
            #     new = ''.join(map(str,new))
            #     print("new str",new)
            #     new_word.append(new)
            #     if(new[k]=='e'):
            #         new.insert(k,'i')
            #         print("after new",new)
            #         new = ''.join(map(str,new))
            #         print("new str",new)
            #         new_word.append(new)
            #     if(new[k]==a)    :
            #         new.insert(k,'ha')
            #         print("after new",new)
            #         new = ''.join(map(str,new))
            #         print("new str",new)
            #         new_word.append(new)


            if(i=="a" and (word[k-1]=='b' or word[k-1]=='c' or word[k-1]=='d'
            or word[k-1]=='f' or word[k-1]=='g' or word[k-1]=='j' or word[k-1]=='k' or
             word[k-1]=='m' or word[k-1]=='n' or word[k-1]=='p' or word[k-1]=='q' or
             word[k-1]=='s' or word[k-1]=='t'  or
            word[k-1]=='w' or word[k-1]=='x' or  word[k-1]=='z' ))    :


                new = word.copy()


                if(word[k-1]==word[k-2]):

                    new.pop(k)
                    new.pop(k-1)


                new.insert(k,'a')
                new.insert(k,'h')


                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)

            if(i == "e" and k<(len(word)-1) and word[k+1] == "y")    :

                new = word.copy()

                new.pop(k+1)
                new.insert(k+1,'a')

                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)


            if( i =="y"  and k<(len(word)-1) and  word[k+1] == "e")    :

                new = word.copy()

                new.pop(k)


                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)



            if(i == "h" and k<(len(word)-1) and  word[k+1]=="r")    :

                new = word.copy()

                new.pop(k)


                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)


            if(i == "h" and k<(len(word)-1) and word[k+1]=="a")    :

                new = word.copy()

                new.pop(k)



                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)


            if(i == "a" and k<(len(word)-1) and word[k+1]=="i")    :

                new = word.copy()

                new.pop(k)


                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)


            if(i == "i"    ):

                new = word.copy()

                new.pop(k)
                new.insert(k,'e')
                new.insert(k,"e")

                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)
                new = word.copy()

                new.pop(k)

                new.insert(k,"y")

                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)

            if(i == "y" and (word[k-1]=='b' or word[k-1]=='c' or word[k-1]=='d'or word[k-1]=='f' or word[k-1]=='g' or word[k-1]=='j' or word[k-1]=='k' or word[k-1]=='l' or word[k-1]=='m' or word[k-1]=='n' or word[k-1]=='p' or word[k-1]=='q' or word[k-1]=='r' or word[k-1]=='s' or word[k-1]=='t' or word[k-1]=='v' or word[k-1]=='w' or word[k-1]=='x' or word[k-1]=='y' or word[k-1]=='z' )   ):

                new = word.copy()

                new.pop(k)

                new.insert(k,"i")
                new.insert(k,"a")
                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)

            if(i == "a" and k<(len(word)-1) and word[k+1]=="u"):

                new = word.copy()

                new.pop(k)


                new.insert(k,"o")
                # new.insert(k,"a")
                new = ''.join(map(str,new))

                new_word.append(new)
                label.append(num)

            if(k<len(word)):
                k = k+1

    num = num+1
    # print(num)
        # if (word[i])

print(len(new_word))
t = 0
for k in new_word:
    print(label[t])
    t = t+1
    print(k)
