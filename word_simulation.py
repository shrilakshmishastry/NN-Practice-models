# an algorithm and program to generate phonetically similar words
k=0
for i in word:
    print(i,k)
    print(word)
    if i == word[k-1]:
        if(i=="o" ):
            new = word.copy()
            new.pop(k-1)
            print(new)
            new.pop(k-1)
            print(new)
            new.insert(k-1,"u")
            new = ''.join(map(str,new))
            new_word.append(new)
        print(new_word)
        k = k+1
    elif((k<len(word)-1 ) and i+i ==  word[k+1]+i   ):
        new = word.copy()


        print("secons")
        new.pop(k)
        new1 = ''.join(map(str,new))
        new_word.append(new1)
        print(new)
        if (i=='a'or i == 'e'  or  i == 'o'   ):
            print("1")

            new1 = new.copy()
            new1.insert(k+1,i)
            print("new = ",new)
            new1 = ''.join(map(str,new1))
            print("after=",new1)
            new_word.append(new1)

        if (k<(len(word)-1) and k<(len(word)-1) and  word[k+1]=="a")    :
            print(2)
            new1 = new.copy()
            print("new",new)
            new1.insert(k+1,'h')
            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)

        if (k<(len(word)-1) and i == 'e'):
            print("3")
            new1 = new.copy()
            print("new",new)
            new1.pop(k)
            new1.insert(k,'i')
            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)


        print(new_word)

        if(i=="a" and (new[k-1]=='b' or new[k-1]=='c' or new[k-1]=='d'
        or new[k-1]=='f' or new[k-1]=='g' or new[k-1]=='j' or new[k-1]=='k' or
        new[k-1]=='l' or new[k-1]=='m' or new[k-1]=='n' or new[k-1]=='p' or new[k-1]=='q' or
        new[k-1]=='r' or new[k-1]=='s' or new[k-1]=='t' or new[k-1]=='v' or
        new[k-1]=='w' or new[k-1]=='x' or new[k-1]=='y' or new[k-1]=='z' ))    :
            print("4")
            new1 = new.copy()
            print("new",new)
            new1.insert(k,'ha')
            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)
        if(i == "e" and k<(len(word)-1) and new[k+1] == "y")    :
            print("5")
            new1 = new.copy()
            print("new",new)
            new1.pop(k+1)
            new1.insert(k+1,'a')
            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)
        if( i =="y"  and k<(len(word)-1) and  new[k+1] == "e")    :
            print("6")
            new1 = new.copy()
            print("new",new)
            new1.pop(k)

            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)
        if(i == "h" and k<(len(word)-1)and  new[k+1]=="r")    :
            print("7")
            new1 = new.copy()
            print("new",new)
            new1.pop(k)

            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)
        if(i == "h" and k<(len(word)-1) and  new[k+1]=="a")    :
            print("7")
            new1 = new.copy()
            print("new",new)
            new1.pop(k)

            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)
        if(i == "a" and k<(len(word)-1) and  new[k+1]=="i")    :
            print("7")
            new1 = new.copy()
            print("new",new)
            new1.pop(k)

            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)
        if(i == "y")    :
            print("7")
            new1 = new.copy()
            print("new",new)
            new1.pop(k)
            new1.pop(k)
            new1.pop(k-1)
            print(new1)
            new1.insert(k,"a")
            print(new1)
            new1.insert(k,"i")
            print(new1)
            new1.append("a")
            print(new1)
            new1.append("h")
            print("after new",new1)
            new1 = ''.join(map(str,new1))
            print("new str",new1)
            new_word.append(new1)
        if(k<len(word)):
            k = k+1
    else:
        print("third")
        if(k<(len(word)-1) and (i == 'b' or i=="c" or i == "d" or i =="f" or i == "g" or i == "j" or i == "k"   or   i == "p" or i == "q"  or i == "s" or i == "t" or   i == "w"  or i == "x"  or i == "z") and (word[k+1]!="h")):
            new = word.copy()
            print("word=",word)
            new.insert(k+1,"h")
            print("new = ",new)
            new = ''.join(map(str,new))
            print("after=",new)
            new_word.append(new)

        if (i=='a'or i == 'e'   or i == 'o'  ):
            print("1")
            new = word.copy()
            print("word=",word)
            new.insert(k+1,i)
            print("new = ",new)
            new = ''.join(map(str,new))
            print("after=",new)
            new_word.append(new)

        if (k<(len(word)-1) and word[k+1]=="a" and i != "h" and (i != "r" and i != "y" and i!="l" and  i!="v" ) )    :
            print(2)
            print(k)
            new = word.copy()
            print("new",new)
            new.insert(k+1,'h')
            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)

        if (k<(len(word)-1) and i == 'e'):
            print("3")
            new = word.copy()
            print("new",new)
            new.insert(k,'i')
            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)


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
            print("4")

            new = word.copy()
            print("new",new)

            if(word[k-1]==word[k-2]):

                new.pop(k)
                new.pop(k-1)

                print(new)
            new.insert(k,'a')
            new.insert(k,'h')

            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)

        if(i == "e" and k<(len(word)-1) and word[k+1] == "y")    :
            print("5")
            new = word.copy()
            print("new",new)
            new.pop(k+1)
            new.insert(k+1,'a')
            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)

        if( i =="y"  and k<(len(word)-1) and  word[k+1] == "e")    :
            print("6")
            new = word.copy()
            print("new",new)
            new.pop(k)

            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)

        if(i == "h" and k<(len(word)-1) and  word[k+1]=="r")    :
            print("7")
            new = word.copy()
            print("new",new)
            new.pop(k)

            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)

        if(i == "h" and k<(len(word)-1) and word[k+1]=="a")    :
            print("7")
            new = word.copy()
            print("new",new)
            new.pop(k)
            print("lak")
            print(new)
            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)

        if(i == "a" and k<(len(word)-1) and word[k+1]=="i")    :
            print("8")
            new = word.copy()
            print("new",new)
            new.pop(k)

            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)

        if(i == "i"    ):
            print("kkk")
            new = word.copy()
            print("new",new)
            new.pop(k)
            new.insert(k,'e')
            new.insert(k,"e")
            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)
            new = word.copy()
            print("new",new)
            new.pop(k)

            new.insert(k,"y")
            print("after new",new)
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)
        if(i == "y" and (word[k-1]=='b' or word[k-1]=='c' or word[k-1]=='d'or word[k-1]=='f' or word[k-1]=='g' or word[k-1]=='j' or word[k-1]=='k' or word[k-1]=='l' or word[k-1]=='m' or word[k-1]=='n' or word[k-1]=='p' or word[k-1]=='q' or word[k-1]=='r' or word[k-1]=='s' or word[k-1]=='t' or word[k-1]=='v' or word[k-1]=='w' or word[k-1]=='x' or word[k-1]=='y' or word[k-1]=='z' )   ):
            print("7")
            new = word.copy()
            print("new",new)
            new.pop(k)

            print("after new",new)
            new.insert(k,"i")
            new.insert(k,"a")
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)
        if(i == "a" and k<(len(word)-1) and word[k+1]=="u"):
            print("9")
            new = word.copy()
            print("new",new)
            new.pop(k)

            print("after new",new)
            new.insert(k,"o")
            # new.insert(k,"a")
            new = ''.join(map(str,new))
            print("new str",new)
            new_word.append(new)

        if(k<len(word)):
            k = k+1
    # if (word[i])
    print(new_word)
