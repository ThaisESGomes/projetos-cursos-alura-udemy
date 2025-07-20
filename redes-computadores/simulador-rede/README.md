# Simulador de Rede

Um simulador simples de rede de computadores desenvolvido em Python para demonstrar conceitos básicos de redes, como ping, traceroute e análise de latência.

## Funcionalidades

- Simulação de ping entre hosts
- Traceroute simulado
- Cálculo de latência de rede
- Análise de perda de pacotes
- Visualização de topologia de rede simples

## Requisitos

- Python 3.6+
- Bibliotecas: `random`, `time`, `json`

## Como usar

1. Execute o script principal:
```bash
python simulador_rede.py
```

2. Escolha uma das opções do menu:
   - Ping simulado
   - Traceroute simulado
   - Análise de latência
   - Visualizar topologia

## Exemplo de uso

```
=== Simulador de Rede ===
1. Ping simulado
2. Traceroute simulado
3. Análise de latência
4. Visualizar topologia
5. Sair

Escolha uma opção: 1
Digite o IP de destino: 192.168.1.100

PING 192.168.1.100: 64 bytes de dados
64 bytes de 192.168.1.100: icmp_seq=1 tempo=23.4ms
64 bytes de 192.168.1.100: icmp_seq=2 tempo=21.8ms
64 bytes de 192.168.1.100: icmp_seq=3 tempo=25.1ms
64 bytes de 192.168.1.100: icmp_seq=4 tempo=22.7ms

--- Estatísticas do ping ---
4 pacotes transmitidos, 4 recebidos, 0% de perda
tempo médio = 23.25ms
```

