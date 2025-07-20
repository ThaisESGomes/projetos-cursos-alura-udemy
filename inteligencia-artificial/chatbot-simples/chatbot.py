#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Chatbot Simples
Um chatbot básico que utiliza processamento de linguagem natural simples
"""

import re
import random
from datetime import datetime
from base_conhecimento import BaseConhecimento
from processador_texto import ProcessadorTexto

class ChatBot:
    def __init__(self):
        self.nome = "ChatBot Simples"
        self.base_conhecimento = BaseConhecimento()
        self.processador = ProcessadorTexto()
        self.historico = []
        self.contexto = {}
        
    def processar_entrada(self, entrada):
        """Processa a entrada do usuário e retorna uma resposta"""
        entrada_limpa = self.processador.limpar_texto(entrada)
        palavras_chave = self.processador.extrair_palavras_chave(entrada_limpa)
        
        # Salvar no histórico
        self.historico.append({
            'timestamp': datetime.now(),
            'usuario': entrada,
            'palavras_chave': palavras_chave
        })
        
        # Verificar padrões específicos
        resposta = self._verificar_padroes(entrada_limpa, palavras_chave)
        
        if not resposta:
            resposta = self._buscar_resposta_base(palavras_chave)
        
        if not resposta:
            resposta = self._resposta_padrao()
        
        return resposta
    
    def _verificar_padroes(self, entrada, palavras_chave):
        """Verifica padrões específicos na entrada"""
        entrada_lower = entrada.lower()
        
        # Saudações
        if any(palavra in entrada_lower for palavra in ['oi', 'olá', 'ola', 'hey', 'bom dia', 'boa tarde', 'boa noite']):
            return random.choice(self.base_conhecimento.saudacoes)
        
        # Despedidas
        if any(palavra in entrada_lower for palavra in ['tchau', 'bye', 'até logo', 'adeus', 'sair']):
            return random.choice(self.base_conhecimento.despedidas)
        
        # Perguntas sobre o bot
        if any(palavra in entrada_lower for palavra in ['seu nome', 'quem é você', 'que você é']):
            return f"Meu nome é {self.nome}. Sou um chatbot simples criado para demonstrar conceitos básicos de IA!"
        
        # Como está
        if any(palavra in entrada_lower for palavra in ['como está', 'como vai', 'tudo bem']):
            return random.choice(self.base_conhecimento.estados)
        
        # Piadas
        if any(palavra in entrada_lower for palavra in ['piada', 'engraçado', 'humor', 'rir']):
            return random.choice(self.base_conhecimento.piadas)
        
        # Ajuda
        if any(palavra in entrada_lower for palavra in ['ajuda', 'help', 'socorro']):
            return self._mostrar_ajuda()
        
        # Hora atual
        if any(palavra in entrada_lower for palavra in ['que horas', 'hora atual', 'horário']):
            agora = datetime.now()
            return f"Agora são {agora.strftime('%H:%M:%S')} do dia {agora.strftime('%d/%m/%Y')}"
        
        return None
    
    def _buscar_resposta_base(self, palavras_chave):
        """Busca resposta na base de conhecimento"""
        for palavra in palavras_chave:
            if palavra in self.base_conhecimento.respostas_contextuais:
                return random.choice(self.base_conhecimento.respostas_contextuais[palavra])
        return None
    
    def _resposta_padrao(self):
        """Retorna uma resposta padrão quando não entende"""
        return random.choice(self.base_conhecimento.respostas_padrao)
    
    def _mostrar_ajuda(self):
        """Mostra as opções de ajuda"""
        return """
🤖 Posso ajudá-lo com:
• Conversas básicas (saudações, como está, etc.)
• Contar piadas
• Informar a hora atual
• Responder perguntas simples sobre tecnologia
• Falar sobre programação e IA

Digite 'sair' para encerrar nossa conversa.
        """
    
    def iniciar_conversa(self):
        """Inicia a conversa com o usuário"""
        print("🤖 " + self.nome + ": Olá! Eu sou um chatbot simples. Como posso ajudá-lo hoje?")
        print("(Digite 'sair' para encerrar a conversa)")
        print()
        
        while True:
            try:
                entrada = input("Você: ").strip()
                
                if not entrada:
                    continue
                
                if entrada.lower() in ['sair', 'exit', 'quit']:
                    print("🤖 " + self.nome + ": Foi um prazer conversar com você! Até logo! 👋")
                    break
                
                resposta = self.processar_entrada(entrada)
                print("🤖 " + self.nome + ": " + resposta)
                print()
                
            except KeyboardInterrupt:
                print("\n🤖 " + self.nome + ": Conversa interrompida. Até logo!")
                break
            except Exception as e:
                print(f"🤖 " + self.nome + ": Desculpe, ocorreu um erro: {e}")

def main():
    """Função principal"""
    chatbot = ChatBot()
    chatbot.iniciar_conversa()

if __name__ == "__main__":
    main()

