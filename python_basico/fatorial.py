num = int(input("Digite numero: "))
if num < 0 :
    print(f"fatorial de {num} não existe")
elif num == 0 :
    fat = 1
    print(f"fatorial de {num} é {fat}")
else : 
    fat = 1
    for i in range(1,num+1):
        fat = fat * i
    print(f"fatorial de {num} é {fat}")

