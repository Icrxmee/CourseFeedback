# CourseFeedback

Sistema de avaliação de cursos em terminal, criado a partir de uma necessidade real de uma escola de artes e ofícios: após o fim de um curso, a coordenação pedagógica precisa coletar a opinião dos alunos sobre diferentes aspectos da experiência — satisfação geral, avaliação do professor, qualidade das aulas, carga horária e outros critérios definidos por ela mesma.

A ideia é simples: **quem responde monta o relatório sozinho.**

> Projeto com foco em **aprendizado de Python**. Cada etapa segue uma metodologia incremental: explicar o conceito → implementar uma parte pequena → testar → corrigir → commitar → só então avançar.

## Fluxo

```
Criar pesquisa
      ↓
Definir curso e professor
      ↓
Criar perguntas e escolher o tipo de cada uma
      ↓
Alunos respondem
      ↓
Sistema registra e processa as respostas
      ↓
Relatório com contagens e porcentagens
      ↓
Futuramente: interface web, links, gráficos e exportação
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
- **Persistência em JSON** (`pesquisa.json`): ao reabrir o programa, um menu oferece *continuar a pesquisa salva* ou *criar uma nova*
- **Proteções**: sem opção duplicada no cadastro de múltipla escolha, mínimo de 2 opções, cada pergunta guarda **cópia própria** do tipo (template do config nunca é alterado)

## Estrutura do projeto

```
CourseFeedback/
├── main.py                  # orquestra o fluxo da aplicação
├── pesquisa.json            # dados salvos (gerado na execução, não versionado)
└── funcoes/
    ├── __init__.py
    ├── configuracao.py      # tipos de pergunta (configuração do sistema)
    ├── entrada.py           # validações, cadastro de perguntas, coleta de respostas
    ├── processamento.py     # filtrar/contar respostas, calcular porcentagens
    ├── relatorio.py         # tela inicial e relatório final
    └── persistencia.py      # salvar e carregar a pesquisa (JSON)
```

Separando responsabilidades:

```
entrada.py ──────→ processamento.py ──────→ relatorio.py
(recebe)            (processa)               (apresenta)
        └──────────────┬──────────────────────┘
                configuracao.py               main.py
                (configurações)               (orquestra)
```

## Como executar

**Pré-requisito:** [Python](https://www.python.org/) 3.10+ (desenvolvido e testado no 3.14)

```bash
git clone https://github.com/Icrxmee/CourseFeedback.git
cd CourseFeedback
python main.py
```

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
- [ ] Interface web com link único para os alunos
- [ ] Gráficos e dashboard
- [ ] Exportação de relatório (PDF, CSV, Excel)
- [ ] Autenticação: coordenação × alunos
- [ ] Decisão sobre anonimato das respostas

## Conceitos praticados

**Python** — variáveis, listas, dicionários, `for`/`while`, `if`/`elif`/`else`, `enumerate`, `range`, funções, validação de entrada, módulos e pacotes, estruturas aninhadas, `json`, context manager (`with`).

**Arquitetura** — separação de responsabilidades, configuração dirigida por dados (novo tipo de pergunta = nova linha no config), identidade (`id`) × posição, referência × cópia (`dict()`/`list()`), funções auxiliares (extração/DRY).

**Git/GitHub** — `clone`, `status`, `diff`, `add`, `commit`, `push`, `.gitignore`, `git rm --cached`, `git mv`, histórico limpo com mensagens convencionais (`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`).
