import fitz  # PyMuPDF

def extract_text(contents: bytes) -> dict:
    """
    Extrai o texto da primeira página do PDF e retorna as informações estruturadas.
    """
    pdf_document = fitz.open(stream=contents, filetype="pdf")
    
    # Extrai texto apenas da primeira página
    first_page = pdf_document[0]
    text = first_page.get_text()
    
    # Limpa o texto e extrai as informações
    cleaned_text = clean_text(text)
    infos = extract_info_from_text(cleaned_text)
    
    return infos


def clean_text(text: str) -> str:
    """
    Remove múltiplas quebras de linha e espaços extras.
    """
    cleaned_text = []
    for line in text.split("\n"):
        line = line.strip()  # Remove espaços no início e no final da linha
        if line:  # Ignora linhas vazias
            cleaned_text.append(line)
            
    return "\n".join(cleaned_text)


def extract_info_from_text(text: str) -> dict:
    """
    Extrai as informações da capa do PDF com base na estrutura esperada.
    """
    infos = text.split("\n")
    
    # Universidade (primeira linha)
    universidade = infos[0]
    
    # Curso (segunda linha)
    curso = infos[1]
    
    # Nomes dos alunos (da linha 3 até um máximo de 6 linhas)
    alunos = []
    for i in range(2,4):  # Verifica as linhas 3 a 8 (índices 2 a 7)
        alunos.append(infos[i])
    
    # Título e Subtítulo (primeira linha após os alunos)
    titulo_index = 2 + len(alunos)  # Índice da linha após os alunos
    
    titulo = infos[titulo_index]
    subtitulo = ""
    if ":" in titulo:
        titulo, subtitulo = map(str.strip, titulo.split(":", 1))  # Divide o título e subtítulo
    
    cidade = infos[-2]
    mes_ano = infos[-1]
    
    # Retorna as informações em um dicionário
    return {
        "universidade": universidade,
        "curso": curso,
        "alunos": alunos,
        "titulo": titulo,
        "subtitulo": subtitulo,
        "cidade": cidade,
        "mes_ano": mes_ano,
    }