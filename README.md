# Gerador de ficha catalografica 2.0

Este projeto foi desenvolvido para resolver a necessidade de uma biblioteca de universidade para gerar fichas catalograficas de forma uniforme.
Teoricamente é a segunda versão do projeto, na primeira versão o gerador apenas funcionava com a introdução manual das informações,
porem agora introduzi a funcionalidade de realizar a extração automatica.

## Oque é uma ficha catalografica?

A ficha catalográfica é um elemento obrigatório em trabalhos acadêmicos, como monografias, dissertações e teses, conforme as normas da ABNT (Associação Brasileira de Normas Técnicas). Ela contém informações essenciais para a identificação da obra, facilitando sua organização e recuperação em bibliotecas. Os dados incluem título, autor, orientador, instituição, ano de publicação, palavras-chave, entre outros. Sua formatação segue padrões específicos que garantem a uniformidade e a clareza das informações.

## Descrição do Projeto

O Gerador de Ficha Catalográfica é uma aplicação web composta por duas camadas principais:

### Frontend
Desenvolvido em React, o frontend é responsável por:
- Interface de usuário intuitiva para inserção manual de dados.
- Upload de documentos para extração automática de informações.
- Envio de dados para o backend para processamento.
- Exibição do resultado final com opção de download do PDF gerado.

### Backend
Implementado em Python utilizando o framework FastAPI, o backend é responsável por:
- Processamento dos dados recebidos do frontend.
- Extração automática de informações relevantes dos documentos enviados.
- Aplicação de regras de formatação conforme padrões bibliográficos.
- Geração do arquivo PDF final.
- Tecnologias Utilizadas
- Frontend: React
- Backend: Python com FastAPI
- Outras tecnologias: Bibliotecas para manipulação de PDF e extração de texto

## Benefícios Esperados

- Eficiência: Redução do tempo gasto na criação de fichas catalográficas.
- Precisão: Menor propensão a erros de digitação e formatação.
- Acessibilidade: Interface amigável e de fácil utilização para bibliotecários de diferentes níveis de experiência.

### Link para primeira versão

[gerador v1.0](https://unisantabiblioteca.github.io/Gerador-Ficha-Catalografica/)

* Primeiro
* Segundo
    * Segundo.1
    * Segundo.2
* Terceiro
