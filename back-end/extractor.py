import fitz  # PyMuPDF
import re    # Para limpeza de quebras de linha com regex

TIPOS_DE_DOCUMENTO = {
    "TCC": "Trabalho de Conclusão de Curso",
    "Dissertação": "Dissertação",
    "Dissertação (Mestrado)": "Dissertação de Mestrado",
    "Tese (Doutorado)": "Tese de Doutorado"
}

def extract_text(contents: bytes) -> dict:
    """
    Extrai o texto da primeira página do PDF e retorna o texto limpo.
    """
    pdf_document = fitz.open(stream=contents, filetype="pdf")

    # Extrai texto apenas da primeira página
    first_page = pdf_document[0]
    text_first_page = first_page.get_text()
    cleaned_text_first_page = clean_text(text_first_page)
    infos_first_page = extract_blocks(cleaned_text_first_page)

    # Extrai o texto da segunda página
    second_page = pdf_document[1]
    text_second_page = second_page.get_text()
    cleaned_text_second_page = clean_text(text_second_page)

    # Extrai texto a partir da terceira página até a décima
    other_pages = pdf_document[2:5]
    text_other_pages = "".join([page.get_text() for page in other_pages])
    # cleaned_text_other_pages = clean_text(text_other_pages)

    # Adicionar o tipo de trabalho ao dicionário de informações
    tipo_trabalho = extract_tipo_trabalho(cleaned_text_second_page)

    # Extrair orientador(a) e co-orientador(a)
    orientadores = extract_orientadores(text_other_pages)

    # Extrair palavras-chave
    palavras_chave = extract_palavras_chave(text_other_pages)
    
    # Oganiza melhor a data e local
    local_data = infos_first_page.get('local_data', [])
    ano = local_data[-1].split("/")[-1]
    cidade = local_data[0].split(" ")[0]
    estado = local_data[0].split(" ")[-1]

    # Consolidar informações
    infos_first_page.update({
        "tipo_trabalho": tipo_trabalho,
        "orientadores": orientadores,
        "palavras_chave": palavras_chave,
        "ano": ano,
        "cidade": cidade,
        "estado": estado,
        "total_paginas": pdf_document.page_count
    })

    infos = infos_first_page

    return infos

def clean_text(text: str) -> str:
    """
    Remove qualquer sequência maior que dois '\n' consecutivos, mantendo apenas dois.
    Também remove espaços em branco invisíveis e caracteres de controle.
    """
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'[ \t\u00A0]+', ' ', text)
    text = re.sub(r'(\n\s*){3,}', '\n\n', text)
    text = re.sub(r' +\n', '\n', text)
    text = re.sub(r'\n +', '\n', text)
    return text

def extract_blocks(text: str) -> dict:
    """
    Extrai blocos de texto separados por duas quebras de linha (\n\n).
    Retorna um dicionário com os blocos identificados.
    """
    blocks = text.strip().split("\n\n")
    return {
        "universidade_curso": blocks[0].strip().split("\n"),
        "alunos": blocks[1].strip().split("\n"),
        "titulo_subtitulo": blocks[2].strip().replace("\n", " ").split(":"),
        "local_data": blocks[3].strip().split("\n")
    }

def extract_tipo_trabalho(text: str) -> str:
    """
    Verifica se o texto contém algum dos tipos de trabalho definidos em TIPOS_DE_DOCUMENTO.
    Retorna o tipo de trabalho encontrado ou 'Desconhecido' se não encontrar nenhum.
    """
    for key, value in TIPOS_DE_DOCUMENTO.items():
        if re.search(rf'\b{re.escape(key)}\b', text, re.IGNORECASE) or \
           re.search(rf'\b{re.escape(value)}\b', text, re.IGNORECASE):
            return key
    return "Desconhecido"

def extract_orientadores(text: str) -> dict:
    # Regex atualizado para capturar nomes antes de ² (subscrito), 2 normal, ³ (subscrito) e 3 normal
    orientador_match = re.search(r'([A-Za-zÀ-ÿ\s]+?)[\s.]*[\u00B2|2]', text)  # Captura ² e 2 normal
    co_orientador_match = re.search(r'([A-Za-zÀ-ÿ\s]+?)[\s.]*[\u00B3|3]', text)  # Captura ³ e 3 normal
    
    orientador = orientador_match.group(1).strip() if orientador_match else "Não encontrado"
    co_orientador = co_orientador_match.group(1).strip() if co_orientador_match else "Não encontrado"

    return {
        "orientador": orientador,
        "co_orientador": co_orientador
    }

def extract_palavras_chave(text: str) -> list:
    # Regex para capturar as palavras-chave até o ponto final, incluindo separadores por vírgula ou ponto e vírgula
    match = re.search(r'palavras[- ]chave[s]?:?\s*(.*?)(?=\s*\.)', text, re.IGNORECASE | re.DOTALL)
    if match:
        # Captura as palavras-chave entre "Palavras-chave" e o ponto final
        palavras_chave_texto = match.group(1)
        
        # Remove quebras de linha e caracteres especiais, substituindo-os por espaços
        palavras_chave_texto = re.sub(r'[\n\r\t\u00A0]', ' ', palavras_chave_texto)
        
        # Divide as palavras-chave por ';' ou ','
        palavras_chave = re.split(r'[;,]', palavras_chave_texto)
        
        # Remove espaços extras e o ponto final no final das palavras-chave
        palavras_chave = [palavra.replace("  "," ").strip().rstrip('.') for palavra in palavras_chave if palavra.strip()]
        
        return palavras_chave
    
    # Caso não encontre as palavras-chave, retorna uma lista vazia
    return []
