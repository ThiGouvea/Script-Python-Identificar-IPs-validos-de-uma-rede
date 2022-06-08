import subprocess


ipsValidos = []
arquivoIpsValidos = open('servers.txt', 'a')
rangeInicial = []
rangeFinal = []
inicioIP = 0
meioIP = 0

inicioIP = int(input('Qual o primeiro numero do IP: '))
meioIP = int(input('Qual o segundo numero do IP: '))

print('Digite o range da parte do meio')
rangeInicial.append(int(input('inicio: ')))
rangeInicial.append(int(input('fim: ')))

print('Digite a parte final')
rangeFinal.append(int(input('inicio: ')))
rangeFinal.append(int(input('fim: ')))

for x in range(rangeInicial[0], rangeInicial[1], 1):
    for y in range(rangeFinal[0], rangeFinal[1], 1):
        resultado = subprocess.run(['ping', '-c 1', '-W 0.2', f'{inicioIP}.{meioIP}.{x}.{y}'], capture_output=True)
        if resultado.returncode == 0:
            ipsValidos.append(resultado.args[3])
            ipsValidos.append('\n')
            print(resultado.args[3])

arquivoIpsValidos.writelines(ipsValidos)
