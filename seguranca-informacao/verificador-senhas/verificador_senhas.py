#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Verificador de Senhas
Ferramenta para avaliar a força de senhas e gerar senhas seguras
"""

import re
import hashlib
from gerador_senhas import GeradorSenhas
from senhas_comuns import SENHAS_COMUNS

class VerificadorSenhas:
    def __init__(self):
        self.gerador = GeradorSenhas()
        self.criterios = {
            'comprimento_minimo': 8,
            'comprimento_recomendado': 12,
            'maiusculas': True,
            'minusculas': True,
            'numeros': True,
            'especiais': True
        }
    
    def verificar_forca(self, senha):
        """Verifica a força de uma senha"""
        resultado = {
            'senha': senha,
            'pontuacao': 0,
            'forca': 'MUITO FRACA',
            'criterios': {},
            'recomendacoes': []
        }
        
        # Verificar comprimento
        comprimento = len(senha)
        if comprimento >= self.criterios['comprimento_recomendado']:
            resultado['criterios']['comprimento'] = {'status': True, 'pontos': 25, 'descricao': f'Comprimento excelente ({comprimento} caracteres)'}
            resultado['pontuacao'] += 25
        elif comprimento >= self.criterios['comprimento_minimo']:
            resultado['criterios']['comprimento'] = {'status': True, 'pontos': 15, 'descricao': f'Comprimento adequado ({comprimento} caracteres)'}
            resultado['pontuacao'] += 15
        else:
            resultado['criterios']['comprimento'] = {'status': False, 'pontos': 0, 'descricao': f'Muito curta ({comprimento} caracteres)'}
            resultado['recomendacoes'].append(f'Use pelo menos {self.criterios["comprimento_minimo"]} caracteres')
        
        # Verificar letras maiúsculas
        if re.search(r'[A-Z]', senha):
            resultado['criterios']['maiusculas'] = {'status': True, 'pontos': 15, 'descricao': 'Contém letras maiúsculas'}
            resultado['pontuacao'] += 15
        else:
            resultado['criterios']['maiusculas'] = {'status': False, 'pontos': 0, 'descricao': 'Não contém letras maiúsculas'}
            resultado['recomendacoes'].append('Adicione letras maiúsculas')
        
        # Verificar letras minúsculas
        if re.search(r'[a-z]', senha):
            resultado['criterios']['minusculas'] = {'status': True, 'pontos': 15, 'descricao': 'Contém letras minúsculas'}
            resultado['pontuacao'] += 15
        else:
            resultado['criterios']['minusculas'] = {'status': False, 'pontos': 0, 'descricao': 'Não contém letras minúsculas'}
            resultado['recomendacoes'].append('Adicione letras minúsculas')
        
        # Verificar números
        if re.search(r'[0-9]', senha):
            resultado['criterios']['numeros'] = {'status': True, 'pontos': 15, 'descricao': 'Contém números'}
            resultado['pontuacao'] += 15
        else:
            resultado['criterios']['numeros'] = {'status': False, 'pontos': 0, 'descricao': 'Não contém números'}
            resultado['recomendacoes'].append('Adicione números')
        
        # Verificar caracteres especiais
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]', senha):
            resultado['criterios']['especiais'] = {'status': True, 'pontos': 20, 'descricao': 'Contém caracteres especiais'}
            resultado['pontuacao'] += 20
        else:
            resultado['criterios']['especiais'] = {'status': False, 'pontos': 0, 'descricao': 'Não contém caracteres especiais'}
            resultado['recomendacoes'].append('Adicione caracteres especiais (!@#$%^&*)')
        
        # Verificar senhas comuns
        if senha.lower() not in SENHAS_COMUNS:
            resultado['criterios']['nao_comum'] = {'status': True, 'pontos': 10, 'descricao': 'Não está na lista de senhas comuns'}
            resultado['pontuacao'] += 10
        else:
            resultado['criterios']['nao_comum'] = {'status': False, 'pontos': 0, 'descricao': 'Está na lista de senhas comuns'}
            resultado['recomendacoes'].append('Evite senhas comuns e previsíveis')
        
        # Determinar força da senha
        if resultado['pontuacao'] >= 90:
            resultado['forca'] = 'MUITO FORTE'
        elif resultado['pontuacao'] >= 70:
            resultado['forca'] = 'FORTE'
        elif resultado['pontuacao'] >= 50:
            resultado['forca'] = 'MODERADA'
        elif resultado['pontuacao'] >= 30:
            resultado['forca'] = 'FRACA'
        else:
            resultado['forca'] = 'MUITO FRACA'
        
        return resultado
    
    def exibir_resultado(self, resultado):
        """Exibe o resultado da verificação de forma formatada"""
        print("\n" + "="*50)
        print("         ANÁLISE DE SEGURANÇA")
        print("="*50)
        
        # Emoji baseado na força
        emoji_forca = {
            'MUITO FORTE': '🔒',
            'FORTE': '💪',
            'MODERADA': '⚠️',
            'FRACA': '😟',
            'MUITO FRACA': '🚨'
        }
        
        print(f"Senha: {'*' * len(resultado['senha'])}")
        print(f"Força: {resultado['forca']} {emoji_forca.get(resultado['forca'], '')}")
        print()
        
        # Exibir critérios
        for criterio, info in resultado['criterios'].items():
            status_icon = "✅" if info['status'] else "❌"
            print(f"{status_icon} {info['descricao']}")
        
        print()
        print(f"Pontuação: {resultado['pontuacao']}/100")
        
        # Recomendações
        if resultado['recomendacoes']:
            print("\n📋 Recomendações:")
            for i, rec in enumerate(resultado['recomendacoes'], 1):
                print(f"  {i}. {rec}")
        else:
            print("\n🎉 Senha segura! Continue usando boas práticas.")
        
        print("="*50)
    
    def verificar_multiplas_senhas(self):
        """Permite verificar múltiplas senhas"""
        print("\n=== Análise de Múltiplas Senhas ===")
        print("Digite as senhas (uma por linha). Digite 'fim' para terminar:")
        
        senhas = []
        while True:
            senha = input("Senha: ").strip()
            if senha.lower() == 'fim':
                break
            if senha:
                senhas.append(senha)
        
        if not senhas:
            print("Nenhuma senha foi inserida.")
            return
        
        print(f"\n=== Relatório de {len(senhas)} senha(s) ===")
        
        for i, senha in enumerate(senhas, 1):
            resultado = self.verificar_forca(senha)
            print(f"\nSenha {i}: {resultado['forca']} ({resultado['pontuacao']}/100)")
        
        # Estatísticas gerais
        pontuacoes = [self.verificar_forca(senha)['pontuacao'] for senha in senhas]
        media = sum(pontuacoes) / len(pontuacoes)
        
        print(f"\n📊 Estatísticas:")
        print(f"   Pontuação média: {media:.1f}/100")
        print(f"   Melhor pontuação: {max(pontuacoes)}/100")
        print(f"   Pior pontuação: {min(pontuacoes)}/100")
    
    def menu_principal(self):
        """Menu principal da aplicação"""
        while True:
            print("\n" + "="*40)
            print("      VERIFICADOR DE SENHAS")
            print("="*40)
            print("1. Verificar força de senha")
            print("2. Gerar senha segura")
            print("3. Analisar múltiplas senhas")
            print("4. Dicas de segurança")
            print("5. Sair")
            print()
            
            try:
                opcao = input("Escolha uma opção: ").strip()
                
                if opcao == "1":
                    senha = input("Digite a senha para verificar: ")
                    if senha:
                        resultado = self.verificar_forca(senha)
                        self.exibir_resultado(resultado)
                    else:
                        print("Senha não pode estar vazia!")
                
                elif opcao == "2":
                    print("\n=== Gerador de Senhas ===")
                    try:
                        comprimento = int(input("Comprimento da senha (padrão 12): ") or "12")
                        incluir_especiais = input("Incluir caracteres especiais? (s/N): ").lower().startswith('s')
                        
                        senha_gerada = self.gerador.gerar_senha(comprimento, incluir_especiais)
                        print(f"\nSenha gerada: {senha_gerada}")
                        
                        # Verificar a força da senha gerada
                        resultado = self.verificar_forca(senha_gerada)
                        print(f"Força: {resultado['forca']} ({resultado['pontuacao']}/100)")
                        
                    except ValueError:
                        print("Comprimento inválido!")
                
                elif opcao == "3":
                    self.verificar_multiplas_senhas()
                
                elif opcao == "4":
                    self._mostrar_dicas()
                
                elif opcao == "5":
                    print("Encerrando verificador...")
                    break
                
                else:
                    print("Opção inválida! Tente novamente.")
            
            except KeyboardInterrupt:
                print("\n\nEncerrando verificador...")
                break
            except Exception as e:
                print(f"Erro: {e}")
    
    def _mostrar_dicas(self):
        """Mostra dicas de segurança"""
        print("\n" + "="*50)
        print("           DICAS DE SEGURANÇA")
        print("="*50)
        print("🔐 Use senhas únicas para cada conta")
        print("📏 Prefira senhas com pelo menos 12 caracteres")
        print("🔤 Combine letras maiúsculas, minúsculas, números e símbolos")
        print("🚫 Evite informações pessoais (nome, data de nascimento)")
        print("🔄 Troque senhas regularmente")
        print("💾 Use um gerenciador de senhas confiável")
        print("🔐 Ative autenticação de dois fatores quando possível")
        print("👀 Cuidado com phishing e sites suspeitos")
        print("🔒 Nunca compartilhe suas senhas")
        print("📱 Mantenha seus dispositivos atualizados")
        print("="*50)

def main():
    """Função principal"""
    verificador = VerificadorSenhas()
    verificador.menu_principal()

if __name__ == "__main__":
    main()

