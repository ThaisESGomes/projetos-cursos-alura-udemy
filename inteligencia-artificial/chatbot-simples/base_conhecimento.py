#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Base de Conhecimento do Chatbot
Contém as respostas e conhecimentos do chatbot
"""

class BaseConhecimento:
    def __init__(self):
        self.saudacoes = [
            "Olá! Como posso ajudá-lo hoje?",
            "Oi! É um prazer falar com você!",
            "Olá! Estou aqui para ajudar!",
            "Oi! Como você está?",
            "Olá! Que bom que você veio conversar comigo!"
        ]
        
        self.despedidas = [
            "Até logo! Foi um prazer conversar com você!",
            "Tchau! Espero vê-lo novamente em breve!",
            "Adeus! Tenha um ótimo dia!",
            "Até mais! Cuide-se!",
            "Tchau! Volte sempre que quiser conversar!"
        ]
        
        self.estados = [
            "Estou bem, obrigado por perguntar! Como posso ajudá-lo?",
            "Estou ótimo! Sempre pronto para uma boa conversa!",
            "Estou funcionando perfeitamente! E você, como está?",
            "Muito bem! Adoro conversar com pessoas interessantes como você!",
            "Estou excelente! Pronto para responder suas perguntas!"
        ]
        
        self.piadas = [
            "Por que os programadores preferem o modo escuro? Porque a luz atrai bugs! 😄",
            "O que o Java falou para o C++? Você não tem classe! 😂",
            "Por que o HTML foi ao psicólogo? Porque tinha problemas de estrutura! 🤣",
            "Como você chama um programador que não consegue dormir? Um desenvolvedor insone! 😴",
            "Por que os algoritmos nunca ficam tristes? Porque sempre encontram uma solução! 😊"
        ]
        
        self.respostas_padrao = [
            "Interessante! Pode me contar mais sobre isso?",
            "Hmm, não tenho certeza sobre isso. Pode reformular a pergunta?",
            "Essa é uma pergunta interessante! Infelizmente não sei a resposta.",
            "Desculpe, não entendi completamente. Pode explicar de outra forma?",
            "Não tenho informações suficientes sobre isso. Que tal mudarmos de assunto?",
            "Essa é uma questão complexa! Gostaria de falar sobre algo mais simples?"
        ]
        
        self.respostas_contextuais = {
            "programação": [
                "Programação é uma habilidade incrível! Qual linguagem você está aprendendo?",
                "Adoro falar sobre programação! É como resolver quebra-cabeças lógicos.",
                "A programação é o futuro! Há tantas possibilidades para criar coisas incríveis."
            ],
            "python": [
                "Python é uma linguagem fantástica! Muito versátil e fácil de aprender.",
                "Python é perfeito para iniciantes e também para projetos avançados!",
                "Amo Python! É a linguagem que uso para funcionar. 🐍"
            ],
            "inteligência artificial": [
                "IA é fascinante! Estamos vivendo uma revolução tecnológica.",
                "A inteligência artificial está transformando o mundo!",
                "IA é o campo que me deu vida! É incrível como máquinas podem aprender."
            ],
            "machine learning": [
                "Machine Learning é o coração da IA moderna!",
                "ML permite que computadores aprendam sem programação explícita.",
                "É impressionante como algoritmos podem encontrar padrões nos dados!"
            ],
            "tecnologia": [
                "A tecnologia está sempre evoluindo! É emocionante acompanhar as novidades.",
                "Vivemos na era da informação! A tecnologia conecta o mundo.",
                "Tecnologia é ferramenta para resolver problemas e melhorar vidas!"
            ],
            "computador": [
                "Computadores são máquinas incríveis! Processam informações em velocidades impressionantes.",
                "Os computadores revolucionaram nossa forma de trabalhar e viver.",
                "É fascinante como os computadores executam bilhões de operações por segundo!"
            ],
            "internet": [
                "A internet conectou o mundo inteiro! É uma rede global de informações.",
                "A internet democratizou o acesso ao conhecimento!",
                "É incrível como podemos nos comunicar instantaneamente com qualquer lugar do mundo!"
            ]
        }

