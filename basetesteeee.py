def base10Men310(string):
    string=string.lower()
    a=['0 ',"1?!%/:&=,'.-_",'2abc','3def','4ghi','5jkl','6mno','7pqrs','8tuv','9wxyz']
    string=[chr for chr in string]
    j=''
    for i in string:
        z=0
        
        while z<10:
            if i in a[z]:
                j=j+str(z)
                z=10
            z=z+1
            if z==10:
                j=j+str(i)
    return(j)
print('##############')
with open ('input','r') as file2:
    for line in file2:
        line=line.strip()
        print(base10Men310(line).lower())