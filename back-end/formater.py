def formater(data):
    data = handle_names(data)
    data = capitalize_data(data)
    return data

def handle_names(data):
    # Inverter nomes dos alunos
    nomes_alunos = data.get('alunos', [])
    nomes_alunos_invertidos = [inverter_nome(nome) for nome in nomes_alunos]

    # Inverter nomes dos orientadores e coorientadores, se existirem
    orientadores = data.get('orientadores', {})
    orientador = orientadores.get('orientador')
    co_orientador = orientadores.get('co_orientador')

    orientador_invertido = inverter_nome(orientador) if orientador and orientador != "Não encontrado" else orientador
    co_orientador_invertido = inverter_nome(co_orientador) if co_orientador and co_orientador != "Não encontrado" else co_orientador

    # Atualiza o dicionário com as listas de nomes invertidos
    data.update({
        "alunos_invertidos": nomes_alunos_invertidos,
        "orientadores_invertidos": {
            "orientador": orientador_invertido,
            "co_orientador": co_orientador_invertido
        }
    })

    return data

def inverter_nome(nome):
    if nome:
        partes = nome.strip().split()
        partes = [parte.capitalize() for parte in partes]
        
        if len(partes) > 1:
            ultimo_nome = partes[-1]
            restante = ' '.join(partes[:-1])
            return f"{ultimo_nome}, {restante}"
        return partes[0]
    return nome

def capitalize_data(data):
    # Função que aplica capitalize() em todos os campos relevantes
    fields_to_capitalize = [
        'alunos', 'alunos_invertidos', 'local_data', 'palavras_chave',
        'titulo_subtitulo', 'universidade_curso'
    ]
    
    for field in fields_to_capitalize:
        if field in data:
            # Se for uma lista de strings, aplica capitalize() em cada item da lista
            if isinstance(data[field], list):
                data[field] = [item.title() for item in data[field]]
            else:
                # Se for uma string única, aplica capitalize diretamente
                data[field] = data[field].title()
    
    # Especialmente para os orientadores, se existirem
    if 'orientadores_invertidos' in data:
        orientadores = data['orientadores_invertidos']
        for key in orientadores:
            if orientadores[key] and orientadores[key] != "Não encontrado":
                orientadores[key] = orientadores[key].title()

    return data
