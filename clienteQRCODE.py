#antes de tudo instalar:

#instalar python (no python .org) no PATH (Add Python to PATH)
#instalar biblioteca de qr code (no terminal do vs code digitar: pip install qrcode[pil])
#instalar biblioteca do PyWhatKit (no terminal do vs code digitar: pip install pywhatkit)

#logar no whatsapp web no navegador padrão do pc

import qrcode
import pywhatkit as kit
from datetime import datetime

# entrada dos dados
print("--- Sistema de Roteiro Turístico ---")
nome = input("Nome do Cliente: ")
nascimento = input("Data de Nascimento: ")
destino = input("Cidade Destino: ")
data_ida = input("Data da ida: ")
data_volta = input("Data da volta: ")
telefone = input("Telefone (Ex: +5511999999999): ")

# logica da "ia" (roteiro)
# saudacao com base na hora do computador
hora_atual = datetime.now().hour
if hora_atual < 12:
    saudacao = "Bom dia"
elif hora_atual < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# o texto final
roteiro_final = f"""
{saudacao}, Sr(a). {nome}!

Aqui está o seu roteiro para {destino}:
 Saída: {data_ida} | Retorno: {data_volta}

 Principais Pontos Turísticos:
- Centro Histórico e Museus
- Parques Naturais e Gastronomia Local

 O que levar:
- Roupas confortáveis e adequadas ao clima de {destino}
- Documentos e carregadores

Obrigado por viajar conosco!
"""

# gerar o qrcode
img = qrcode.make(roteiro_final)
nome_arquivo_qr = "roteiro_cliente.png"
img.save(nome_arquivo_qr)

# exibicao e envio
print("\n" + "="*30)
print(roteiro_final)
print("="*30)
print(f"\n QR Code salvo como: {nome_arquivo_qr}")

# enviar pelo WhatsApp (vai abrir o navegador e espera 40 segundos)
print("Enviando para o WhatsApp... aguarde o navegador abrir.")
kit.sendwhatmsg_instantly(telefone, roteiro_final, 40, True, 10)