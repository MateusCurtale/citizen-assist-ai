# Citizen Assist AI — Central do Cidadão de Aurora

**Integrantes do Grupo:**
* Mateus Felipe Curtale Serafim - 571129
* Vinicius Sanches Chiarle -
* Gabrieli de Lima Pettena -

## Estrutura do Projeto

```text
citizen-assist-ai/
├── fichas/
│   ├── FC-01_rg_segunda_via.md
│   ├── FC-02_cpf.md
│   ├── FC-03_titulo_de_eleitor.md
│   ├── FC-04_carteira_de_trabalho.md
│   ├── FC-05_certidoes.md
│   ├── FC-06_cnh_renovacao.md
│   └── FC-07_regras_gerais.md
├── .env
├── requirements.txt
├── agente.py               # Pipeline em LangGraph (Guardrails, Busca e Agente)
├── app.py                  # Interface web acessível em Streamlit
└── citizen_assist.ipynb    # Benchmark Golden Dataset + LLM as a Judge (V1 vs V2)
```

## Como Executar

1. Crie e ative o ambiente virtual e instale as dependências:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

2. Configure sua chave da API Groq no arquivo `.env`:
```env
GROQ_API_KEY=gsk_sua_chave_aqui
```

3. Para abrir a interface acessível (testes com usuários):
```bash
streamlit run app.py
```

4. Para rodar a avaliação completa do *Golden Dataset* (26 perguntas) e o *LLM as a Judge*:
Abra o arquivo `citizen_assist.ipynb` no VS Code ou Jupyter e execute todas as células.
