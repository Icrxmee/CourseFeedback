# Guia de hospedagem

Duas formas de o CourseFeedback sair do seu PC. A primeira já funciona
hoje; a segunda exige sua conta no provedor (o código já está pronto).

---

## A) Link temporário (túnel) — já testado

O `cloudflared` cria uma saída pública que encaminha para o
`127.0.0.1:5000` local. **Sem conta**, dados continuam no seu PC.

```powershell
# 1. servidor local ligado
venv\Scripts\python app.py          # (ou o caminho da sua venv)

# 2. túnel (binário baixado do GitHub oficial da Cloudflare)
cloudflared.exe tunnel --url http://127.0.0.1:5000
# o console imprime: https://XXXX-XXXX.trycloudflare.com
```

- A URL morra quando você fecha o túnel ou o computador desliga.
- Bom para: testar com alunos, demonstração, piloto rápido.

---

## B) Hospedagem permanente — o que já está pronto no repositório

| Artefato | Função |
|---|---|
| `requirements.txt` | Flask + **gunicorn** (servidor WSGI de produção) |
| `app.py` | `FLASK_DEBUG`/`PORT`/`HOST` via **variáveis de ambiente**; debug **desligado por padrão** |
| `Dockerfile` | imagem universal (qualquer host com Docker) |
| `render.yaml` | blueprint automático do Render |
| `pesquisa_exemplo.json` + `persistencia.semear()` | primeira execução nunca começa com a tela vazia |

### Opções de provedor (confirme o free tier na hora — costuma mudar)

| Provedor | Como | Disco com `pesquisa.json` | Observação |
|---|---|---|---|
| **Render** | conecta o GitHub → lê o `render.yaml` → build → `gunicorn` | ❌ **efêmero** (redeploy/reinício zera; a semente recria o *exemplo*, respostas reais somem) | Mais fácil; instância dorme após inatividade (~50s no 1º acesso) |
| **PythonAnywhere** | conta grátis + config WSGI manual (guio abaixo) | ✅ **persistente** no plano grátis | URL `seuusuario.pythonanywhere.com` |
| **Hugging Face Spaces** (Docker) | conta GitHub → New Space → usa o `Dockerfile` | ❌ efêmero entre rebuilds | Rápido, público |

**Resumo:** quer *dados sobreviverem* de graça → **PythonAnywhere**;
quer *simplicidade total* e aceita perda por redeplooy → **Render**.

### Lacuna conhecida (próxima etapa do projeto)

O **cadastro de pesquisa ainda é só no terminal** — num servidor não há
terminal interativo. Por isso existe a **semente**. A solução definitiva
é a **Etapa 11: cadastro de pesquisa pela web** (formulário da
coordenação no navegador).

### Decisão de arquitetura pendente (roadmap)

Para escala real, migrar `pesquisa.json` para banco de dados
(SQLite em disco persistente, ou Postgres grátis — Neon/Supabase).
Isso vira uma etapa própria de aprendizado.

---

## Passo a passo — Render

1. Conta em <https://render.com> → *Sign up with GitHub* (seu login).
2. **New → Web Service** → conectar `Icrxmee/CourseFeedback`.
3. O Render detecta o `render.yaml` (*Blueprint*) → revisar → **Apply**.
4. Build automático (`pip install -r requirements.txt`) → deploy
   (`gunicorn app:app --bind 0.0.0.0:$PORT`).
5. URL final: `https://coursefeedback.onrender.com`.
6. Testar: home → `/responder` → `/relatorio`.

> ⚠️ Em disco efêmero, **cada reinício volta ao exemplo** (a semente
> só garante que o link nunca fique vazio). Para coleção real de
> respostas, use disco persistente/banco ou cadastro + exportação
> regulares.

## Passo a passo — PythonAnywhere

1. Conta em <https://www.pythonanywhere.com> (seu login).
2. *Files* → subir o repositório (ou *Open Bash* → `git clone`).
3. *Web → Add a new web app → Flask* → editar o `wsgi.py` apontando
   para `app.py` do projeto.
4. Em *Web → Virtualenv*, apontar para a venv do projeto (ou instalar
   `pip install -r requirements.txt` no console).
5. Reload → URL `https://seuusuario.pythonanywhere.com`.

## Checklist de segurança antes do link sair do PC

- [x] `FLASK_DEBUG=0` em produção (o console do Werkzeug é de
      **execução remota** — nunca pode ir público).
- [x] `.gitignore` protege o `pesquisa.json` (nomes não vão pro Git).
- [ ] **Anonimato/auth**: o relatório público mostra **nomes + respostas**
      — decidir antes de divulgar de verdade (roadmap).
- [ ] Migrar dados para banco quando sair de demonstração.
