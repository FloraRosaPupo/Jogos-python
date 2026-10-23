# Jogos em Python
Jogos de terminal: forca, adivinhação e jogo da velha. Requer Python 3.11+; não há dependências externas.

```sh
python jogos.py
python -m unittest discover -s tests -v
```
`palavras.txt` contém o vocabulário da forca. O menu permite várias partidas sem recursão; o jogo da velha valida coordenadas e encerra empates. A CI executa os testes de regras e menu.

## Licença
Não há licença de distribuição definida neste repositório.


## Stack e bibliotecas

Python padrão e unittest.


## Funcionalidades

- Adivinhação.
- forca.
- jogo da velha e menu.


## Organização e manutenção

Cada jogo já é um módulo coeso. Menu iterativo e regras de tabuleiro independentes da entrada permitem testes sem interação; não há motivo para introduzir framework de estado ou camadas de UI.

Veja [a revisão de desenvolvimento](docs/REVISAO.md) para decisões, testes e limites, e [o guia de contribuição](CONTRIBUTING.md) para o fluxo de manutenção.
