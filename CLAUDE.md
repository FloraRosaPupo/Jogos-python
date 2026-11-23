# Jogos de terminal em Python

Adivinhação, forca e jogo da velha, com menu para alternar. Só Python padrão.

## Estrutura
```
jogos.py        menu principal → chama cada jogo
adivinhacao.py  número secreto com tentativas
forca.py        palavra secreta, letras, desenho da forca (cerca de 160 linhas)
velha.py        tabuleiro 3x3, vitória e empate
tests/test_jogos.py  regras e navegação sem input real
```

## Comandos (PowerShell)
```powershell
python -m unittest discover -s tests -v
python jogos.py
```

## CI e deploy
- `ci.yml` roda unittest.
- Não há deploy.

## Regras
- Sem dependências externas.
- Regras testáveis sem `input()`: separe a lógica da entrada e saída, ou injete funções de entrada.
- Não versione `__pycache__/` (adicione ao `.gitignore` se faltar).
