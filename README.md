# Divisor de arquivos MP3

Script em Python para dividir um arquivo `.mp3` em trechos de 15 minutos, salvando cada parte também em `.mp3`.

## Funcionalidades

- Divide arquivos `.mp3` em partes de 15 minutos
- Mantém o último trecho com a duração restante, caso seja menor que 15 minutos
- Exibe no terminal:
  - a duração total do arquivo original
  - o nome de cada arquivo gerado
  - a duração de cada trecho gerado
- Solicita, em tempo de execução, os caminhos dos executáveis `ffmpeg` e `ffprobe`
- Não exige que o `ffmpeg` esteja configurado no `PATH` do sistema

## Requisitos

- Python 3.10 ou superior
- `ffmpeg.exe`
- `ffprobe.exe` (recomendado)

## Instalação

Clone o repositório e instale a dependência:

```bash
pip install -r requirements.txt
```

## Como usar

Execute o script:

```bash
python dividir_mp3.py
```

O programa solicitará:

1. Caminho completo do executável `ffmpeg`
2. Caminho completo do executável `ffprobe` (opcional, mas recomendado)
3. Caminho completo do arquivo `.mp3`

### Exemplo de caminhos no Windows

```text
C:\ffmpeg\bin\ffmpeg.exe
C:\ffmpeg\bin\ffprobe.exe
C:\audios\aula.mp3
```

## Exemplo de saída

```text
=== Divisor de arquivos MP3 ===

Informe o caminho completo do executável ffmpeg: C:\ffmpeg\bin\ffmpeg.exe
Informe o caminho completo do executável ffprobe (ou pressione Enter para pular): C:\ffmpeg\bin\ffprobe.exe

Informe o caminho completo do arquivo .mp3: C:\audios\aula.mp3

============================================================
Arquivo original: aula.mp3
Duração total:    00:48:00
Tamanho do trecho: 15 minutos
Total de partes:   4
============================================================
aula_part1.mp3  |  duração: 00:15:00
aula_part2.mp3  |  duração: 00:15:00
aula_part3.mp3  |  duração: 00:15:00
aula_part4.mp3  |  duração: 00:03:00
============================================================
Processo concluído.
```

## Estrutura sugerida

```text
mp3-splitter/
├── dividir_mp3.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Observações

- Os arquivos gerados serão salvos na mesma pasta do arquivo original.
- O nome das partes seguirá o padrão:
  - `nomeoriginal_part1.mp3`
  - `nomeoriginal_part2.mp3`
  - `nomeoriginal_part3.mp3`
- O `ffprobe` não é obrigatório, mas melhora a leitura de metadados do áudio.
