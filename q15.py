qh=float(input('quanto voce ganha por hora'))
qm=float(input('quantas horas voce trabalha por mes'))
b=qh*qm
IN=b*(11/100)
INSS=b*(8/100)
sindicato=b*(5/100)
l=b-IN-INSS-sindicato
print('salario bruto',b)
print('com desconto IN',IN)
print('com desconto INSS',INSS)
print('com desconto do sindicato',sindicato)
print('salario liquido igual a',l)