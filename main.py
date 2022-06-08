import subprocess


ipsValidos = []
arquivoIpsValidos = open('servers.txt', 'a')

for x in range(0, 255, 1):
    for y in range(0, 255, 1):
        resultado = subprocess.run(['ping','-c 1', '-W 0.2', f'192.168.{x}.{y}'], capture_output=True)
        if resultado.returncode == 0:
            ipsValidos.append(resultado.args[3])
            ipsValidos.append('\n')
            print(resultado.args[3])
            arquivoIpsValidos.writelines(ipsValidos)
