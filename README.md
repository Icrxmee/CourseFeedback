# CourseFeedback

Sistema de avaliação de cursos com **terminal** e **interface web**, criado a partir de uma necessidade real de uma escola de artes e ofícios: após o fim de um curso, a coordenação pedagógica precisa coletar a opinião dos alunos sobre diferentes aspectos da experiência — satisfação geral, avaliação do professor, qualidade das aulas, carga horária e outros critérios definidos por ela mesma.

A ideia é simples: **quem responde monta o relatório sozinho.**

> Projeto com foco em **aprendizado de Python**. Cada etapa segue uma metodologia incremental: explicar o conceito → implementar uma parte pequena → testar → corrigir → commitar → só então avançar.

## Fluxo

```
Criar pesquisa (terminal)
      ↓
Definir curso e professor
      ↓
Criar perguntas e escolher o tipo de cada uma
      ↓
Alunos respondem — pelo terminal ou pelo navegador
      ↓
Sistema registra e processa as respostas (pesquisa.json)
      ↓
Relatório com contagens e porcentagens — terminal e web (barras)
      ↓
Futuramente: link público, gráficos e exportação
```

## Funcionalidades

- **Cadastro de curso e professor** com validação de entrada (texto não vazio, número maior que zero)
- **4 tipos de pergunta:**

  | Tipo | Exemplo |
  |---|---|
  | Sim/Não | "Você gostou do curso?" |
  | Nota 1–5 | "Nota para o professor" |
  | Múltipla escolha | opções definidas no cadastro — ex.: Professor, Conteúdo, Estrutura |
  | Aberta | "O que poderia ser melhorado?" (resposta em texto livre) |

- **Coleta por aluno**, com cada resposta ligada ao **ID** da pergunta (nunca à posição na lista)
- **Relatório no terminal**: contagem + porcentagem por opção; perguntas abertas são listadas com o nome de quem respondeu
- **Interface web (Flask)** com três páginas:
  - **Início** — dados da pesquisa e acesso rápido;
  - **Responder** — formulário do aluno (rádio, nota ou texto);
  - **Relatório** — mesmos números do terminal, apresentados com **barras de porcentagem**.
- **Persistência em JSON** (`pesquisa.json`): ao reabrir o terminal, um menu oferece *continuar a pesquisa salva* ou *criar uma nova*; o web carrega e acrescenta respostas ao mesmo arquivo
- **Proteções**: sem opção duplicada no cadastro de múltipla escolha, mínimo de 2 opções, cada pergunta guarda **cópia própria** do tipo (template do config nunca é alterado), **validação repetida no servidor** (o navegador nunca é a única barreira) e **trava** (`threading.Lock`) contra dois envios simultâneos se sobrescreverem

## Estrutura do projeto

```
CourseFeedback/
├── main.py                  # orquestra o fluxo no terminal
├── app.py                   # servidor web Flask — rotas e validação
├── requirements.txt         # dependências do web (Flask e bibliotecas)
├── pesquisa.json            # dados salvos (gerado na execução, não versionado)
├── templates/               # páginas HTML (Jinja2)
│   ├── base.html            # layout comum (topo, nav, rodapé)
│   ├── index.html           # página inicial
│   ├── responder.html       # formulário do aluno
│   ├── obrigado.html        # confirmação após enviar
│   └── relatorio.html       # relatório com barras
├── static/
│   └── style.css            # estilo da interface
└── funcoes/
    ├── __init__.py
    ├── configuracao.py      # tipos de pergunta (configuração do sistema)
    ├── entrada.py           # validações, cadastro de perguntas, coleta (terminal)
    ├── processamento.py     # filtrar/contar respostas, calcular porcentagens
    ├── relatorio.py         # montar_relatorio (modelo) + apresentação no terminal
    └── persistencia.py      # salvar e carregar a pesquisa (JSON)
```

Separando responsabilidades:

```
entrada.py ──────→ processamento.py ──────→ relatorio.py
(recebe)            (processa)          (monta o modelo)
        └──────────────┬──────────────────────┘
                configuracao.py       main.py  (terminal → print)
                (configurações)       app.py   (web → HTML)

As duas faces consomem o MESMO modelo de dados (montar_relatorio):
nada é recalculado em um lugar e no outro — só a apresentação muda.
```

## Como executar

**Pré-requisito:** [Python](https://www.python.org/) 3.10+ (desenvolvido e testado no 3.14)

```bash
git clone https://github.com/Icrxmee/CourseFeedback.git
cd CourseFeedback
python main.py
```

### Interface web

```bash
# 1. ambiente virtual + dependências (uma vez só)
python -m venv venv
venv\Scripts\pip install -r requirements.txt    # Linux/macOS: venv/bin/pip

# 2. subir o servidor (crie antes uma pesquisa: python main.py)
venv\Scripts\python app.py                      # Linux/macOS: venv/bin/python
# abra http://127.0.0.1:5000

# desenvolvimento com auto-reload (opcional; em produção fica desligado)
FLASK_DEBUG=1 venv\Scripts\python app.py
```

> **Quer colocar no ar?** Veja o passo a passo em
> [docs/hospedagem.md](docs/hospedagem.md) — túnel temporário
> (`cloudflared`) ou hospedagem permanente (Render, PythonAnywhere,
> Docker) já com tudo preparado no repositório.

> **Dica (OneDrive/nuvem):** se a pasta do projeto for sincronizada, crie a venv foradela — `python -m venv C:\caminho\fora_do_onedrive` — e use esse caminho no lugar de `venv\...`. Milhares de arquivos de terceiros não precisam subir para a nuvem; o `requirements.txt` recria tudo em segundos.

## Exemplo de saída

```
========================================
SISTEMA DE AVALIAÇÃO DE CURSO
========================================
...
pergunta: Você gostou do curso?
Sim: 8 (80.0%)
Não: 2 (20.0%)

pergunta: Nota para o professor?
Nota 1: 0 (0.0%)
Nota 2: 1 (10.0%)
...
Nota 5: 6 (60.0%)

pergunta: O que poderia ser melhorado?
- Ana: Mais projetos práticos
- Bruno: Aulas com mais tempo de execução
```

## Roadmap

- [x] Terminal com cadastro de perguntas e respostas
- [x] Perguntas com ID próprio
- [x] 4 tipos de pergunta (Sim/Não, Nota, Múltipla, Aberta)
- [x] Contagem e porcentagens
- [x] Persistência em JSON
- [x] Interface web local (Flask): home, formulário com validação e relatório com barras
- [ ] Interface web com link único público para os alunos
- [ ] Gráficos e dashboard
- [ ] Exportação de relatório (PDF, CSV, Excel)
- [ ] Autenticação: coordenação × alunos
- [ ] Decisão sobre anonimato das respostas

## Conceitos praticados

**Python** — variáveis, listas, dicionários, `for`/`while`, `if`/`elif`/`else`, `enumerate`, `range`, funções, validação de entrada, módulos e pacotes, estruturas aninhadas, `json`, context manager (`with`), `threading.Lock`.

**Web (Flask)** — HTTP (GET, POST, 302, 404), portas e rotas, decorators (`@app.route`), templates Jinja2 (herança, filtros, autoescape), formulários HTML, validação **no servidor**, padrão PRG (Post → Redirect → Get), arquivos `static/`.

**Arquitetura** — separação de responsabilidades, configuração dirigida por dados (novo tipo de pergunta = nova linha no config), identidade (`id`) × posição, referência × cópia (`dict()`/`list()`), funções auxiliares (extração/DRY), **modelo de dados × apresentação** (o mesmo `montar_relatorio` alimenta terminal e web).

**Ambiente** — `venv` (ambiente virtual), `requirements.txt`, `.gitignore`.

**Git/GitHub** — `clone`, `status`, `diff`, `add`, `commit`, `push`, `.gitignore`, `git rm --cached`, `git mv`, histórico limpo com mensagens convencionais (`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`).
