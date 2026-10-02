#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gerador de Senhas
Módulo para gerar senhas seguras
"""

from secrets import SystemRandom
import string
import secrets

rng = SystemRandom()

class GeradorSenhas:
    def __init__(self):
        self.letras_minusculas = string.ascii_lowercase
        self.letras_maiusculas = string.ascii_uppercase
        self.numeros = string.digits
        self.especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Palavras para senhas memoráveis
        self.palavras_base = [
            "Casa", "Gato", "Sol", "Mar", "Lua", "Flor", "Rio", "Paz",
            "Arte", "Vida", "Amor", "Luz", "Fogo", "Agua", "Terra", "Ar",
            "Azul", "Verde", "Ouro", "Prata", "Forte", "Livre", "Novo", "Bom"
        ]
    
    def gerar_senha(self, comprimento=12, incluir_especiais=True):
        """Gera uma senha aleatória segura"""
        if comprimento < 4:
            raise ValueError("Comprimento mínimo é 4 caracteres")
        
        # Garantir pelo menos um caractere de cada tipo
        caracteres = []
        tipos_caracteres = []
        
        # Adicionar pelo menos uma letra minúscula
        caracteres.append(secrets.choice(self.letras_minusculas))
        tipos_caracteres.append(self.letras_minusculas)
        
        # Adicionar pelo menos uma letra maiúscula
        caracteres.append(secrets.choice(self.letras_maiusculas))
        tipos_caracteres.append(self.letras_maiusculas)
        
        # Adicionar pelo menos um número
        caracteres.append(secrets.choice(self.numeros))
        tipos_caracteres.append(self.numeros)
        
        # Adicionar caractere especial se solicitado
        if incluir_especiais:
            caracteres.append(secrets.choice(self.especiais))
            tipos_caracteres.append(self.especiais)
        
        # Preencher o resto da senha
        todos_caracteres = self.letras_minusculas + self.letras_maiusculas + self.numeros
        if incluir_especiais:
            todos_caracteres += self.especiais
        
        for _ in range(comprimento - len(caracteres)):
            caracteres.append(secrets.choice(todos_caracteres))
        
        # Embaralhar os caracteres
        rng.shuffle(caracteres)
        
        return ''.join(caracteres)
    
    def gerar_senha_memoravel(self, num_palavras=3, incluir_numeros=True, incluir_especiais=True):
        """Gera uma senha memorável usando palavras"""
        palavras = rng.sample(self.palavras_base, num_palavras)
        
        # Modificar algumas palavras
        for i in range(len(palavras)):
            palavra = palavras[i]
            
            # Algumas modificações aleatórias
            if rng.choice([True, False]):
                palavra = palavra.upper()
            
            if incluir_numeros and rng.choice([True, False]):
                palavra += str(rng.randint(0, 99))
            
            palavras[i] = palavra
        
        # Conectar palavras
        conectores = ['-', '_', '.'] if incluir_especiais else ['']
        conector = rng.choice(conectores)
        
        senha = conector.join(palavras)
        
        # Adicionar caracteres especiais no final se solicitado
        if incluir_especiais:
            senha += rng.choice(self.especiais)
            senha += str(rng.randint(10, 99))
        
        return senha
    
    def gerar_multiplas_senhas(self, quantidade=5, comprimento=12, incluir_especiais=True):
        """Gera múltiplas senhas"""
        senhas = []
        for _ in range(quantidade):
            senha = self.gerar_senha(comprimento, incluir_especiais)
            senhas.append(senha)
        return senhas
    
    def gerar_passphrase(self, num_palavras=4, separador='-'):
        """Gera uma passphrase usando palavras aleatórias"""
        palavras = rng.sample(self.palavras_base, num_palavras)
        
        # Adicionar números aleatórios
        for i in range(len(palavras)):
            if rng.choice([True, False]):
                palavras[i] += str(rng.randint(1, 999))
        
        return separador.join(palavras)
    
    def validar_entropia(self, senha):
        """Estimativa idealizada; não mede a força real de senhas humanas ou passphrases"""
        charset_size = 0
        
        if any(c in self.letras_minusculas for c in senha):
            charset_size += len(self.letras_minusculas)
        
        if any(c in self.letras_maiusculas for c in senha):
            charset_size += len(self.letras_maiusculas)
        
        if any(c in self.numeros for c in senha):
            charset_size += len(self.numeros)
        
        if any(c in self.especiais for c in senha):
            charset_size += len(self.especiais)
        
        if charset_size == 0:
            return 0
        
        import math
        entropia = len(senha) * math.log2(charset_size)
        return entropia

