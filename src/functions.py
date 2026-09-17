import itertools

# Função para inverter a ordem dos pesos de acordo com os índices passados
def inverter_pesos(grafo, troca_indices):
    grafo_invertido = []
    
    for origem, destino, peso1, peso2, peso3 in grafo:
        pesos = [peso1, peso2, peso3]  # Lista com os pesos
        # Trocar os pesos conforme os índices passados
        pesos[troca_indices[0]], pesos[troca_indices[1]] = pesos[troca_indices[1]], pesos[troca_indices[0]]
        grafo_invertido.append((origem, destino, pesos[0], pesos[1], pesos[2]))
    
    return grafo_invertido

#função max_vertex
def max_vertex(grafo, inicio, fim, t_max, c_max, s_max):
    # Armazenar o melhor caminho e o número máximo de arestas
    melhor_caminho = []
    max_arestas = 0
    tempo_final = 0
    custo_final = 0
    satisfacao_final = 0
    
    # Função auxiliar para explorar o caminho
    def dfs(vertice_atual, caminho, arestas_percorridas, tempo_acumulado, custo_acumulado, satisfacao_acumulada):
        nonlocal melhor_caminho, max_arestas, tempo_final, custo_final, satisfacao_final
        
        # Se atingirmos o destino e o tempo, custo e satisfação não ultrapassaram os limites, verificamos se é o melhor caminho
        if vertice_atual == fim:
            media_satisfacao = satisfacao_acumulada / arestas_percorridas if arestas_percorridas > 0 else 0
            if arestas_percorridas > max_arestas and tempo_acumulado <= t_max and custo_acumulado <= c_max and media_satisfacao <= s_max:
                melhor_caminho = caminho[:]
                max_arestas = arestas_percorridas
                tempo_final = tempo_acumulado
                custo_final = custo_acumulado
                satisfacao_final = media_satisfacao
            return
        
        # Explora os vizinhos
        for (u, v, tempo, custo, score) in grafo:
            if u == vertice_atual and v not in caminho:  # Garantir que não repita vértices
                # Verifica se o tempo, custo e satisfação acumulados não ultrapassam os limites
                media_satisfacao = (satisfacao_acumulada + score) / (arestas_percorridas + 1) if arestas_percorridas + 1 > 0 else 0
                if tempo_acumulado + tempo <= t_max and custo_acumulado + custo <= c_max and media_satisfacao <= s_max:
                    dfs(v, caminho + [v], arestas_percorridas + 1, tempo_acumulado + tempo, custo_acumulado + custo, satisfacao_acumulada + score)
    
    # Inicia a DFS a partir do vértice inicial
    dfs(inicio, [inicio], 0, 0, 0, 0)
    
    return melhor_caminho, max_arestas, tempo_final, custo_final, satisfacao_final

#caminho minimo
def min_path(grafo, inicio, fim, peso, peso_mapping):
    # Identificando o índice do peso a ser minimizado
    if peso not in peso_mapping:
        raise ValueError(f"Peso inválido. Escolha entre {list(peso_mapping.keys())}")
    peso_index = peso_mapping[peso]

    # Criar lista de vértices únicos no grafo
    vertices = set()
    for origem, destino, *_ in grafo:
        vertices.add(origem)
        vertices.add(destino)
    
    # Remover vértices inicial e final para gerar as permutações
    vertices.remove(inicio)
    vertices.remove(fim)

    # Gerar todas as permutações possíveis de vértices intermediários
    permutacoes = itertools.permutations(vertices)

    # Inicializar valores do menor caminho
    melhor_custo = float('inf')
    melhor_tempo = float('inf')
    melhor_caminho = []

    # Iterar por todas as permutações para encontrar o menor caminho
    for perm in permutacoes:
        caminho_completo = [inicio] + list(perm) + [fim]
        custo_total = 0
        tempo_total = 0
        
        # Calcular os custos para o caminho atual
        valido = True
        for i in range(len(caminho_completo) - 1):
            origem = caminho_completo[i]
            destino = caminho_completo[i + 1]
            
            # Encontrar a aresta correspondente no grafo
            for u, v, tempo, custo, score in grafo:
                if u == origem and v == destino:
                    custo_total += custo  # Sempre soma o custo em R$
                    tempo_total += tempo  # Sempre soma o tempo em minutos
                    if peso_index == 2:  # Score é acumulado como tempo alternativo
                        tempo_total += score
                    break
            else:
                # Se não encontrou uma aresta válida, o caminho não é possível
                valido = False
                break
        
        # Atualizar o melhor caminho se válido e com menor custo
        if valido and custo_total < melhor_custo:
            melhor_custo = custo_total
            melhor_tempo = tempo_total
            melhor_caminho = caminho_completo

    # Formatar o caminho para exibição
    caminho_formatado = " -> ".join(melhor_caminho)
    
    return melhor_custo, melhor_tempo, caminho_formatado

#next...