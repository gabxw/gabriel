---
id: 001
title: Plataforma de correção ENEM
stage: constitution
date: 2026-04-10
surface: agent
model: gpt-5
feature: none
branch: master
user: LENOVO
command: /sp.constitution
labels: [constitution, enem, nextjs, prisma, tailwind]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\LENOVO\Documents\gabriel\.specify\memory\constitution.md
 - C:\Users\LENOVO\Documents\gabriel\history\prompts\constitution\001-plataforma-correcao-enem.constitution.prompt.md
tests:
 - Not run (documentation update only)
---

## Prompt

Run prompt: sp.constitution /sp.constitution

Projeto: Plataforma web de correção automática de redações estilo ENEM

Regras técnicas:
- Frontend em Next.js
- Backend em API routes do Next.js
- TypeScript obrigatório
- UI simples com Tailwind
- Banco PostgreSQL com Prisma
- Autenticação com email + senha
- Upload de redação por texto ou arquivo
- Avaliação com IA via API
- Arquitetura limpa e modular
- Código legível e bem comentado
- Separar camadas: UI, services, ai, db

Regras de produto:
- Corrigir redação no modelo ENEM
- Dar nota de 0 a 1000
- Avaliar 5 competências
- Mostrar erros gramaticais
- Sugerir melhorias
- Reescrever parágrafos
- Mostrar feedback detalhado
- Histórico de redações
- Tempo de resposta rápido
- Interface simples
- Priorizar performance
- Priorizar UX simples

## Response snapshot

Updated `.specify/memory/constitution.md` with a project-specific constitution for the ENEM essay-correction platform, including ENEM rubric fidelity, simple UX, modular Next.js architecture, secure data ownership, and governance/versioning rules.

## Outcome

- ✅ Impact: Established the governance baseline for the platform.
- 🧪 Tests: Not run (documentation-only change).
- 📁 Files: Updated the constitution and created the PHR record.
- 🔁 Next prompts: `/sp.specify`, then `/sp.plan`.
- 🧠 Reflection: The product and technical rules now align around the same stack, rubric, and UX goals.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): Run `/sp.specify` for the first feature slice, starting with text/file submission and correction output.
