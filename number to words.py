number=["","one","two","three","four","five","six","seven","eight","nine"]
nty=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
tens=["ten","eleven","twelve","thirtheen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
n=int(input("enter a number"))

if n>99999:
    print("can't solve for more than five digits")

elif n<=99999 and n>0:
    d=[0,0,0,0,0]
    i=0
    while n>0:
        d[i]=n%10
        i+=1
        n=n//10
    num=""
    if d[4]!=0:
        if d[4]==0:
            num+=number [d[3]] + ' thousand '

        else:
            num+=nty [d[4]]+" "+ number[d[3]]+ " thousand "

    else:
        if d[3]!=0:
            num+=number[d[3]]+ " thousand "
    if d[2]!=0:
        num+=number[d[2]]+ " hundred "
    if d[1] !=0:
        if(d[1]==1):
            num+=tens [d[0]]
        else:
            num+=nty [d[1]]+" "+ number [d[0]]
    else:
        if d[0]!=0:
            num+=number [d[0]]
    print(num)
#positive side
elif n==0:
    print('zero')
elif n<-99999:
    print('cant solve for more than five figures in the negative form')
else:
    if n>=-99999:
        m=-n
        d = [0, 0, 0, 0, 0]
        i = 0
        while m > 0:
            d[i] = m % 10
            i += 1
            m = m // 10
        num =" "
        if d[4] != 0:
            if d[4] == 0:
                num += number[d[3]] + ' thousand '

            else:
                num += nty[d[4]] + " " + number[d[3]] + " thousand "

        else:
            if d[3] != 0:
                num += number[d[3]] + " thousand "
        if d[2] != 0:
            num += number[d[2]] + " hundred "
        if d[1] != 0:
            if (d[1] == 1):
                num += tens[d[0]]
            else:
                num += nty[d[1]] + " " + number[d[0]]
        else:
            if d[0] != 0:
                num += number[d[0]]
        print('negative',end="")
        print(num)





















