import fitz  # PyMuPDF
import re    # Para limpeza de quebras de linha com regex

def extract_text(contents: bytes) -> dict:
    """
    Extrai o texto da primeira página do PDF e retorna o texto limpo.
    """
    pdf_document = fitz.open(stream=contents, filetype="pdf")
    
    # Extrai texto apenas da primeira página
    first_page = pdf_document[0]
    text = first_page.get_text()
    
    # Limpa o texto e extrai as informações
    cleaned_text = clean_text(text)
    infos = extract_blocks(cleaned_text)
    return infos


def clean_text(text: str) -> str:
    """
    Remove qualquer sequência maior que dois '\n' consecutivos, mantendo apenas dois.
    Também remove espaços em branco invisíveis e caracteres de controle.
    """
    # 1️⃣ Uniformizar quebras de linha (\r\n, \r → \n)
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # 2️⃣ Remover espaços invisíveis (como \u00A0, tabs, etc.)
    text = re.sub(r'[ \t\u00A0]+', ' ', text)  # Substitui espaços múltiplos por um único espaço

    # 3️⃣ Substituir múltiplas quebras de linha seguidas por no máximo duas
    text = re.sub(r'(\n\s*){3,}', '\n\n', text)  # Garante no máximo duas quebras de linha consecutivas

    # 4️⃣ Remover espaços extras antes ou depois das quebras de linha
    text = re.sub(r' +\n', '\n', text)  # Remove espaços antes de \n
    text = re.sub(r'\n +', '\n', text)  # Remove espaços após \n

    return text



def extract_blocks(text: str) -> dict:
    """
    Extrai blocos de texto separados por duas quebras de linha (\n\n).
    Retorna um dicionário com os blocos identificados.
    """
    # Dividir o texto em blocos usando duas quebras de linha consecutivas
    blocks = text.strip().split("\n\n")

    # Garantir que existam exatamente 4 blocos (preenche com vazio se faltar)
    while len(blocks) < 4:
        blocks.append("")

    # Criar o dicionário com os blocos nomeados
    result = {
        "universidade_faculdade": blocks[0].strip(),
        "alunos": blocks[1].strip(),
        "titulo_trabalho": blocks[2].strip(),
        "local_data": blocks[3].strip()
    }

    return result