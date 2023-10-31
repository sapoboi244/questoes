t=float(input('digite o tamanho do arquivo em mb'))
v=float(input('digite a velocidade do arquvo '))
tm=(t*8)/v
m=tm//60
s=tm%60
printe('o tempo do download desse arquivo e',m,s)