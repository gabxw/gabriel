---
id: 001
title: Plataforma de correcao ENEM
stage: spec
date: 2026-04-10
surface: agent
model: gpt-5
feature: 001-correcao-redacao-enem
branch: 001-correcao-redacao-enem
user: LENOVO
command: /sp.specify
labels: [spec, enem, ia, saas]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\LENOVO\Documents\gabriel\specs\001-correcao-redacao-enem\spec.md
 - C:\Users\LENOVO\Documents\gabriel\specs\001-correcao-redacao-enem\checklists\requirements.md
 - C:\Users\LENOVO\Documents\gabriel\history\prompts\001-correcao-redacao-enem\001-plataforma-correcao-enem.spec.prompt.md
tests:
 - Manual validation against the spec quality checklist
---

## Prompt

Criar plataforma web de correção automática de redações estilo ENEM usando IA.

Usuário pode:
- colar redação
- upload .txt .pdf .docx
- clicar em "Corrigir redação"

Sistema deve:
- enviar redação para modelo de IA
- corrigir no padrão ENEM
- gerar nota final 0-1000
- gerar notas por competência:
  C1 norma culta
  C2 compreensão do tema
  C3 argumentação
  C4 coesão
  C5 proposta de intervenção

Resposta deve conter:
- nota final
- notas por competência
- feedback detalhado
- erros gramaticais
- sugestões de melhoria
- redação reescrita melhorada

UI:
- textarea grande
- botão corrigir
- loading
- resultado abaixo

Stack:
- Next.js
- TypeScript
- Tailwind
- API IA
- Prisma
- PostgreSQL

Requisitos:
- resposta estruturada JSON
- tempo resposta rápido
- custo baixo por requisição
- arquitetura preparada para SaaS

## Response snapshot

Created a complete feature spec for the ENEM essay correction platform, including three prioritized user stories, edge cases, functional requirements, key entities, and measurable success criteria. Also added the spec quality checklist and validated it as ready for planning.

## Outcome

- ✅ Impact: The feature is now scoped and ready for `/sp.plan`.
- 🧪 Tests: Manual validation against the spec checklist completed.
- 📁 Files: Updated `spec.md`, created `checklists/requirements.md`, and recorded this PHR.
- 🔁 Next prompts: `/sp.plan`.
- 🧠 Reflection: The spec keeps the first release centered on correction, then account/history, then dashboard management.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): Run `/sp.plan` to turn the spec into a concrete implementation plan.
