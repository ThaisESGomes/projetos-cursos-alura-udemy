# Verificador de Senhas

Uma ferramenta de segurança desenvolvida em Python para avaliar a força de senhas e gerar senhas seguras, demonstrando conceitos importantes de segurança da informação.

## Funcionalidades

- Análise de força de senhas
- Verificação de critérios de segurança
- Geração de senhas seguras
- Detecção de senhas comuns/vazadas
- Relatório detalhado de segurança
- Interface de linha de comando

## Critérios de avaliação

- Comprimento mínimo (8 caracteres)
- Presença de letras maiúsculas
- Presença de letras minúsculas
- Presença de números
- Presença de caracteres especiais
- Verificação contra lista de senhas comuns

## Como usar

1. Execute o verificador:
```bash
python verificador_senhas.py
```

2. Escolha uma opção do menu:
   - Verificar força de senha
   - Gerar senha segura
   - Analisar múltiplas senhas
   - Sair

## Exemplo de uso

```
=== Verificador de Senhas ===
1. Verificar força de senha
2. Gerar senha segura
3. Analisar múltiplas senhas
4. Sair

Escolha uma opção: 1
Digite a senha para verificar: MinhaSenh@123

=== Análise de Segurança ===
Senha: MinhaSenh@123
Força: FORTE 💪

✅ Comprimento adequado (12 caracteres)
✅ Contém letras maiúsculas
✅ Contém letras minúsculas
✅ Contém números
✅ Contém caracteres especiais
✅ Não está na lista de senhas comuns

Pontuação: 95/100
Recomendação: Senha segura! Continue usando boas práticas.
```

## Estrutura do projeto

```
verificador-senhas/
├── verificador_senhas.py
├── gerador_senhas.py
├── senhas_comuns.py
└── README.md
```

