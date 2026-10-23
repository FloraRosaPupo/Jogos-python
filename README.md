# Jogos de Terminal em Python

## Descrição

Coleção de jogos de terminal em Python: adivinhação, forca e jogo da velha. Um menu permite alternar entre partidas; as regras e a navegação têm testes automatizados sem dependências externas.

## Stack e bibliotecas

Python padrão e unittest.

## Funcionalidades

- Adivinhação.
- Forca.
- Jogo da velha e menu.

## Licença

Não há uma licença de distribuição definida para este repositório. Nenhuma licença MIT, Apache ou equivalente é concedida por este README. As atribuições e os direitos dos materiais de terceiros permanecem preservados.

## Validação e limites

Vencedor, empate, limites do tabuleiro e navegação. Execução interativa complementar pelo terminal.

## Execução e testes

Jogos de terminal: forca, adivinhação e jogo da velha. Requer Python 3.11+; não há dependências externas.

```sh
python jogos.py
python -m unittest discover -s tests -v
```
`palavras.txt` contém o vocabulário da forca. O menu permite várias partidas sem recursão; o jogo da velha valida coordenadas e encerra empates. A CI executa os testes de regras e menu.

## Organização e manutenção

Cada jogo já é um módulo coeso. Menu iterativo e regras de tabuleiro independentes da entrada permitem testes sem interação; não há motivo para introduzir framework de estado ou camadas de UI.

Veja [a revisão de desenvolvimento](docs/REVISAO.md) para decisões, testes e limites, e [o guia de contribuição](CONTRIBUTING.md) para o fluxo de manutenção.
