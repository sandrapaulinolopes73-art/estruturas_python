age = 22
has_invitation = False
is_vip = True



age = int(input('Digite a idade: '))
has_invitation = False
is_vip = True

if is_vip:
    print('Que bom ver você novamente')    

elif age >= 18 and has_invitation:
    print("Entrada permitida") 

else: 
    print("Entrada não permitida") 

print("Acabou")


