# Laboratórios e exercícios

Exercícios organizados por assunto. Cada pasta contém seu README e instruções. O nome do repositório agrupa estudos; consulte cada projeto para seu escopo e limitações.

| Área | Projeto | Objetivo |
|---|---|---|
| Segurança | [Verificador e gerador de senhas](seguranca-informacao/verificador-senhas) | Explorar geração aleatória, regras e limites das estimativas de força |
| Redes | [Simulador de rede](redes-computadores/simulador-rede) | Estudar conceitos de comunicação |
| IA | [Chatbot simples](inteligencia-artificial/chatbot-simples) | Explorar processamento de texto e base de conhecimento |
| Web | [Calculadora](programacao/calculadora-web) | Praticar HTML, CSS e JavaScript |
| Python | [Exercícios](programacao/python-simples) | Praticar fundamentos de programação |

## Segurança do gerador

A geração usa `secrets` e `SystemRandom`, incluindo embaralhamento e seleção de palavras. A lista de palavras do exemplo é pequena e didática: não é adequada para gerar passphrases de alto valor. A fórmula baseada no tamanho do alfabeto é uma estimativa idealizada, não uma medida da força de uma senha humana.

```bash
python -m unittest discover -s tests -v
```

Para um projeto defensivo com correlação de eventos e relatórios, veja [Auth Log Guardian](https://github.com/ThaisESGomes/auth-log-guardian).
