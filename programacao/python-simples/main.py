#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Projeto Python Simples
Demonstra conceitos básicos de programação em Python
"""

def somar_numeros(a, b):
    """Retorna a soma de dois números"""
    return a + b

def verificar_par_impar(numero):
    """Verifica se um número é par ou ímpar"""
    if numero % 2 == 0:
        return f"{numero} é par."
    else:
        return f"{numero} é ímpar."

def mensagem_boas_vindas(nome):
    """Exibe uma mensagem de boas-vindas personalizada"""
    return f"Olá, {nome}! Bem-vindo(a) ao projeto Python Simples."

def main():
    """Função principal do programa"""
    print("=== Projeto Python Simples ===\n")
    
    # Soma de dois números
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = somar_numeros(num1, num2)
        print(f"A soma é: {resultado}\n")
    except ValueError:
        print("Por favor, digite números válidos.\n")
    
    # Verificação par/ímpar
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado_par_impar = verificar_par_impar(numero)
        print(f"{resultado_par_impar}\n")
    except ValueError:
        print("Por favor, digite um número inteiro válido.\n")
    
    # Mensagem de boas-vindas
    nome = input("Digite seu nome: ")
    if nome.strip():
        mensagem = mensagem_boas_vindas(nome)
        print(mensagem)
    else:
        print("Nome não informado.")

if __name__ == "__main__":
    main()

