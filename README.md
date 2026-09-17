# Otimização de Trajetos Turísticos no Rio de Janeiro

Este projeto aplica modelagem matemática e otimização em grafos para resolver o problema de planejamento de roteiros turísticos diários. O objetivo é maximizar a quantidade de Pontos de Interesse (POIs) visitados, respeitando restrições rígidas de tempo máximo, orçamento limite e satisfação mínima esperada pelo usuário.

O embasamento teórico, a modelagem de Programação Inteira e os detalhes da heurística adotada estão documentados no relatório técnico disponível na pasta `docs/`.

## 📁 Estrutura do Projeto

A estrutura de arquivos e pastas do projeto está dividida da seguinte forma:

```text
├── data/
│   ├── POIs_tables_references.xlsx  # Referências de custos e tempos manuais
│   ├── rawDataGmaps.csv             # Dados brutos extraídos da API
│   ├── data.csv                     # Dados processados (features calculadas)
│   └── dados.csv                    # Base final filtrada para o grafo
├── docs/
│   └── projetoPI_ElisAlvesBraga.pdf # Relatório técnico e modelagem matemática
├── notebooks/
│   ├── 01_getData.ipynb             # Coleta de dados (Google Maps API)
│   ├── 02_orgData.ipynb             # Limpeza e feature engineering (Pandas)
│   └── 03_otimizationProject.ipynb  # Algoritmo de otimização e resultados
├── src/
│   └── functions.py                 # Funções auxiliares (Heurística de Dijkstra adaptada)
├── .env.example                     # Template para configuração de chaves de API
├── .gitignore                       # Proteção de credenciais e arquivos temporários
├── requirements.txt                 # Dependências do projeto
└── README.md
```

## 🛠️ Tecnologias e Bibliotecas

* **Python 3**
* `pandas` e `numpy` (Manipulação e estruturação de dados)
* `networkx` (Criação e manipulação de grafos direcionados)
* `googlemaps` (Coleta de rotas, tempos e valores de deslocamento)
* `os` (Gestão segura de variáveis de ambiente)

## 🚀 Como Executar

O projeto foi construído para ser reprodutível. Siga os passos abaixo:

1. **Clone o repositório e crie um ambiente virtual:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuração da API (Opcional para visualização):**
   A extração original já foi realizada e os dados estão contidos na pasta `data/`. Caso deseje rodar o notebook `01_getData.ipynb` para coletar novas rotas, é necessário configurar uma chave da Google Maps API.
   * Renomeie o arquivo `.env.example` para `.env`
   * Insira a sua chave: `GOOGLE_API_KEY=sua_chave_aqui`

4. **Rodando a Otimização:**
   Você pode ir direto para o notebook `03_otimizationProject.ipynb` para visualizar a construção do grafo via `networkx` e a aplicação do algoritmo de Dijkstra adaptado para maximização de vértices sob restrições múltiplas.

## 🧠 Destaques Técnicos

* **Segurança:** Uso de variáveis de ambiente (`.env`) para ocultar credenciais em código público.
* **Modularização:** Lógicas complexas de busca em grafos isoladas no pacote `src/functions.py` para manter os notebooks limpos e focados em análise.
* **Modelagem:** Adaptação de um problema de natureza NP-Difícil utilizando métodos heurísticos para encontrar rotas sub-ótimas altamente eficientes em tempo viável de processamento.

## 📄 Licença

Este projeto é de uso restrito e não está disponível para redistribuição.