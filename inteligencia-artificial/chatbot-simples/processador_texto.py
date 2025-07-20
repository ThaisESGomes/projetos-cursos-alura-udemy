#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Processador de Texto
Funções para processamento e análise de texto
"""

import re
import string

class ProcessadorTexto:
    def __init__(self):
        self.palavras_irrelevantes = {
            'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
            'de', 'da', 'do', 'das', 'dos', 'em', 'na', 'no', 'nas', 'nos',
            'para', 'por', 'com', 'sem', 'sobre', 'entre', 'até', 'desde',
            'e', 'ou', 'mas', 'porém', 'contudo', 'entretanto',
            'que', 'qual', 'quais', 'quando', 'onde', 'como', 'porque',
            'é', 'são', 'foi', 'foram', 'ser', 'estar', 'ter', 'haver',
            'eu', 'tu', 'ele', 'ela', 'nós', 'vós', 'eles', 'elas',
            'me', 'te', 'se', 'nos', 'vos', 'lhe', 'lhes',
            'meu', 'minha', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas',
            'seu', 'sua', 'seus', 'suas', 'nosso', 'nossa', 'nossos', 'nossas',
            'este', 'esta', 'estes', 'estas', 'esse', 'essa', 'esses', 'essas',
            'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'isso', 'aquilo'
        }
    
    def limpar_texto(self, texto):
        """Remove pontuação e normaliza o texto"""
        # Converter para minúsculas
        texto = texto.lower()
        
        # Remover pontuação, mas manter espaços
        texto = re.sub(r'[^\w\s]', ' ', texto)
        
        # Remover espaços extras
        texto = re.sub(r'\s+', ' ', texto).strip()
        
        return texto
    
    def extrair_palavras_chave(self, texto):
        """Extrai palavras-chave relevantes do texto"""
        palavras = texto.split()
        
        # Filtrar palavras irrelevantes e muito curtas
        palavras_chave = [
            palavra for palavra in palavras 
            if palavra not in self.palavras_irrelevantes 
            and len(palavra) > 2
        ]
        
        return palavras_chave
    
    def calcular_similaridade(self, texto1, texto2):
        """Calcula similaridade básica entre dois textos"""
        palavras1 = set(self.extrair_palavras_chave(self.limpar_texto(texto1)))
        palavras2 = set(self.extrair_palavras_chave(self.limpar_texto(texto2)))
        
        if not palavras1 or not palavras2:
            return 0.0
        
        intersecao = palavras1.intersection(palavras2)
        uniao = palavras1.union(palavras2)
        
        return len(intersecao) / len(uniao)
    
    def detectar_sentimento(self, texto):
        """Detecta sentimento básico do texto"""
        palavras_positivas = {
            'bom', 'boa', 'ótimo', 'ótima', 'excelente', 'maravilhoso',
            'fantástico', 'incrível', 'legal', 'bacana', 'feliz', 'alegre',
            'gosto', 'amo', 'adoro', 'perfeito', 'perfeita'
        }
        
        palavras_negativas = {
            'ruim', 'péssimo', 'péssima', 'horrível', 'terrível',
            'triste', 'chato', 'chata', 'odeio', 'detesto',
            'problema', 'erro', 'difícil', 'complicado', 'impossível'
        }
        
        texto_limpo = self.limpar_texto(texto)
        palavras = texto_limpo.split()
        
        pontuacao_positiva = sum(1 for palavra in palavras if palavra in palavras_positivas)
        pontuacao_negativa = sum(1 for palavra in palavras if palavra in palavras_negativas)
        
        if pontuacao_positiva > pontuacao_negativa:
            return 'positivo'
        elif pontuacao_negativa > pontuacao_positiva:
            return 'negativo'
        else:
            return 'neutro'
    
    def extrair_entidades(self, texto):
        """Extrai entidades básicas do texto"""
        entidades = {
            'numeros': re.findall(r'\d+', texto),
            'emails': re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto),
            'urls': re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', texto)
        }
        
        return entidades

