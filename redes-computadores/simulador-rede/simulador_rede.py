#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simulador de Rede
Demonstra conceitos básicos de redes de computadores
"""

import random
import time
import json
from datetime import datetime

class SimuladorRede:
    def __init__(self):
        self.topologia = {
            "192.168.1.1": {"nome": "Gateway", "tipo": "router"},
            "192.168.1.100": {"nome": "Servidor Web", "tipo": "server"},
            "192.168.1.101": {"nome": "Servidor DNS", "tipo": "server"},
            "192.168.1.10": {"nome": "PC-01", "tipo": "host"},
            "192.168.1.11": {"nome": "PC-02", "tipo": "host"},
            "10.0.0.1": {"nome": "Router Externo", "tipo": "router"},
            "8.8.8.8": {"nome": "DNS Google", "tipo": "server"}
        }
        
        self.rotas = {
            "192.168.1.0/24": ["192.168.1.1"],
            "10.0.0.0/24": ["192.168.1.1", "10.0.0.1"],
            "8.8.8.8": ["192.168.1.1", "10.0.0.1", "8.8.8.8"]
        }

    def ping_simulado(self, destino, pacotes=4):
        """Simula um comando ping"""
        print(f"\nPING {destino}: 64 bytes de dados")
        
        tempos = []
        pacotes_perdidos = 0
        
        for i in range(1, pacotes + 1):
            # Simula perda de pacotes (5% de chance)
            if random.random() < 0.05:
                print(f"Timeout para icmp_seq={i}")
                pacotes_perdidos += 1
                continue
            
            # Simula latência variável
            latencia = random.uniform(15.0, 35.0)
            tempos.append(latencia)
            
            print(f"64 bytes de {destino}: icmp_seq={i} tempo={latencia:.1f}ms")
            time.sleep(0.5)  # Pausa para simular tempo real
        
        # Estatísticas
        print(f"\n--- Estatísticas do ping ---")
        print(f"{pacotes} pacotes transmitidos, {pacotes - pacotes_perdidos} recebidos, {(pacotes_perdidos/pacotes)*100:.0f}% de perda")
        
        if tempos:
            tempo_medio = sum(tempos) / len(tempos)
            print(f"tempo médio = {tempo_medio:.2f}ms")
            print(f"tempo mín/máx = {min(tempos):.1f}/{max(tempos):.1f}ms")

    def traceroute_simulado(self, destino):
        """Simula um comando traceroute"""
        print(f"\nTraceroute para {destino}")
        print("Máximo de 30 saltos:\n")
        
        # Rota simulada baseada no destino
        if destino.startswith("192.168.1"):
            rota = ["192.168.1.1", destino]
        elif destino.startswith("10.0.0"):
            rota = ["192.168.1.1", "10.0.0.1", destino]
        else:
            rota = ["192.168.1.1", "10.0.0.1", "203.0.113.1", "8.8.8.8"]
        
        for i, hop in enumerate(rota, 1):
            latencia1 = random.uniform(10.0 + i*5, 25.0 + i*10)
            latencia2 = random.uniform(10.0 + i*5, 25.0 + i*10)
            latencia3 = random.uniform(10.0 + i*5, 25.0 + i*10)
            
            nome = self.topologia.get(hop, {}).get("nome", f"hop-{i}")
            
            print(f"{i:2d}  {hop} ({nome})  {latencia1:.1f}ms  {latencia2:.1f}ms  {latencia3:.1f}ms")
            time.sleep(0.3)

    def analise_latencia(self):
        """Analisa a latência da rede"""
        print("\n=== Análise de Latência da Rede ===")
        
        hosts = ["192.168.1.100", "192.168.1.101", "8.8.8.8", "10.0.0.1"]
        
        for host in hosts:
            nome = self.topologia.get(host, {}).get("nome", "Desconhecido")
            latencia = random.uniform(15.0, 45.0)
            jitter = random.uniform(1.0, 5.0)
            
            status = "Boa" if latencia < 30 else "Moderada" if latencia < 50 else "Alta"
            
            print(f"{host} ({nome}):")
            print(f"  Latência: {latencia:.1f}ms")
            print(f"  Jitter: {jitter:.1f}ms")
            print(f"  Status: {status}")
            print()

    def visualizar_topologia(self):
        """Exibe a topologia da rede"""
        print("\n=== Topologia da Rede ===")
        print()
        
        for ip, info in self.topologia.items():
            tipo_icon = {
                "router": "🔀",
                "server": "🖥️",
                "host": "💻"
            }.get(info["tipo"], "❓")
            
            print(f"{tipo_icon} {ip} - {info['nome']} ({info['tipo']})")
        
        print("\n=== Conexões ===")
        print("192.168.1.0/24 ←→ 192.168.1.1 (Gateway)")
        print("192.168.1.1 ←→ 10.0.0.1 (Router Externo)")
        print("10.0.0.1 ←→ Internet (8.8.8.8)")

    def menu_principal(self):
        """Menu principal do simulador"""
        while True:
            print("\n" + "="*30)
            print("    Simulador de Rede")
            print("="*30)
            print("1. Ping simulado")
            print("2. Traceroute simulado")
            print("3. Análise de latência")
            print("4. Visualizar topologia")
            print("5. Sair")
            print()
            
            try:
                opcao = input("Escolha uma opção: ").strip()
                
                if opcao == "1":
                    destino = input("Digite o IP de destino: ").strip()
                    if destino:
                        self.ping_simulado(destino)
                    else:
                        print("IP inválido!")
                
                elif opcao == "2":
                    destino = input("Digite o IP de destino: ").strip()
                    if destino:
                        self.traceroute_simulado(destino)
                    else:
                        print("IP inválido!")
                
                elif opcao == "3":
                    self.analise_latencia()
                
                elif opcao == "4":
                    self.visualizar_topologia()
                
                elif opcao == "5":
                    print("Encerrando simulador...")
                    break
                
                else:
                    print("Opção inválida! Tente novamente.")
            
            except KeyboardInterrupt:
                print("\n\nEncerrando simulador...")
                break
            except Exception as e:
                print(f"Erro: {e}")

def main():
    """Função principal"""
    simulador = SimuladorRede()
    simulador.menu_principal()

if __name__ == "__main__":
    main()

