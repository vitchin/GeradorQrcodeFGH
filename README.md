# Gerador de QRCode

Este é um sistema simples para gerar QRCodes a partir de informações de manutenção predial.

## O que o sistema faz?

O sistema permite que o usuário preencha um formulário com detalhes de um serviço de manutenção e gere um QRCode contendo essas informações. O QRCode gerado pode ser impresso e anexado ao equipamento ou local correspondente.

## Tecnologias Utilizadas

- **Flask**: Um microframework web em Python para o backend.
- **HTML/CSS (Tailwind CSS)**: Para a estrutura e estilização das páginas.
- **JavaScript (jQuery)**: Para a lógica do frontend, como a captura de dados do formulário e a geração do QRCode.
- **qrcode.js**: Uma biblioteca JavaScript para gerar QRCodes.

## Páginas do Sistema

### Página Inicial

A página inicial contém um formulário para o usuário inserir as informações do serviço de manutenção.

<img src="./static/img/home.png" alt="pagina inicial">

### Página do QR Code

Esta página exibe o QR Code gerado a partir dos dados do formulário, juntamente com um resumo das informações. A página também oferece opções para voltar à página inicial ou imprimir o QR Code.

<img src="./static/img/qrcode.png" alt="pagina qrcode">
