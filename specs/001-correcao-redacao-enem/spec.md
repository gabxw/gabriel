# Feature Specification: Plataforma de Correcao ENEM com IA

**Feature Branch**: `[001-correcao-redacao-enem]`  
**Created**: 2026-04-10  
**Status**: Draft  
**Input**: User description: "Criar plataforma web de correção automática de redações estilo ENEM usando IA. Usuário pode colar redação, fazer upload .txt .pdf .docx e clicar em Corrigir redação. Sistema deve enviar redação para modelo de IA, corrigir no padrão ENEM, gerar nota final 0-1000 e notas por competencia C1 a C5. Resposta deve conter nota final, notas por competencia, feedback detalhado, erros gramaticais, sugestões de melhoria e redação reescrita melhorada. UI com textarea grande, botao corrigir, loading e resultado abaixo. Stack desejada: Next.js, TypeScript, Tailwind, API IA, Prisma, PostgreSQL. Requisitos: resposta estruturada JSON, tempo resposta rapido, custo baixo por requisicao, arquitetura preparada para SaaS"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Corrigir redacao com IA (Priority: P1)

O usuario cola uma redacao ou faz upload de um arquivo suportado, clica em "Corrigir redacao" e recebe uma correcao completa no padrao ENEM.

**Why this priority**: This is the core value of the product and the main reason users visit the platform.

**Independent Test**: A tester can submit a sample redacao by text or supported file and confirm that the result appears without any account setup.

**Acceptance Scenarios**:

1. **Given** a valid essay pasted into the editor, **When** the user clicks "Corrigir redacao", **Then** the system returns a complete structured result with nota final, notas por competencia, feedback detalhado, erros gramaticais, sugestoes de melhoria, and a melhorada reescrita.
2. **Given** a supported file upload, **When** the user submits it, **Then** the same correction result is displayed below the editor after processing.

---

### User Story 2 - Criar conta e salvar historico (Priority: P2)

O usuario cria conta com email e senha para salvar correcoes, voltar depois e manter um historico pessoal.

**Why this priority**: The product needs private history and SaaS readiness, but it only becomes useful after the core correction flow exists.

**Independent Test**: A tester can register a new account, submit a correction, sign out, sign back in, and confirm that the correction is still available in the user's history.

**Acceptance Scenarios**:

1. **Given** a new visitor, **When** the visitor creates an account with email and password, **Then** the user can access the dashboard and saved corrections later.
2. **Given** a signed-in user, **When** the user completes a correction, **Then** the correction is saved to personal history.

---

### User Story 3 - Revisar e gerenciar correcoes antigas (Priority: P3)

O usuario autenticado abre correcoes antigas no dashboard e pode apagar redacoes que nao quer manter.

**Why this priority**: Reopening and deleting past corrections are important for ongoing usage, but they depend on the account and history foundation.

**Independent Test**: A tester can open a past correction from the dashboard and delete it, then verify that it no longer appears.

**Acceptance Scenarios**:

1. **Given** a dashboard with previous corrections, **When** the user opens one item, **Then** the full saved result is shown again.
2. **Given** a saved redacao in the dashboard, **When** the user deletes it, **Then** the item is removed from history and cannot be reopened.

---

### Edge Cases

- What happens when the essay text is empty or only contains the prompt?
- How does the system handle an unsupported file type or a file that cannot be read?
- What happens when the correction service returns incomplete or malformed structured data?
- How does the system behave if the correction takes too long or fails midway?
- What happens when a user tries to open or delete another user's correction?
- How does the system handle repeated submissions of the same essay?
- What happens when the user refreshes or leaves the page while a correction is still processing?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST allow users to submit a redacao by pasting text or uploading a `.txt`, `.pdf`, or `.docx` file.
- **FR-002**: The system MUST provide a single primary action to start the correction flow.
- **FR-003**: The system MUST return a structured correction result with final score, five competence scores, detailed feedback, grammar errors, improvement suggestions, and an improved rewrite.
- **FR-004**: The final score MUST range from 0 to 1000, and each competence score MUST be shown in the ENEM order C1 to C5.
- **FR-005**: The correction MUST follow the ENEM model for norma culta, compreensao do tema, argumentacao, coesao, and proposta de intervencao.
- **FR-006**: The interface MUST show a loading state while the correction is processing and prevent duplicate submissions during that time.
- **FR-007**: The system MUST show clear, user-friendly error messages for empty submissions, unsupported files, unreadable files, and correction failures.
- **FR-008**: The system MUST allow users to create an account and sign in with email and password.
- **FR-009**: The system MUST save each correction to the signed-in user's private history.
- **FR-010**: The system MUST let users view a dashboard with their past corrections.
- **FR-011**: The system MUST let users reopen any previously saved correction from the dashboard.
- **FR-012**: The system MUST let users delete a saved redacao from the dashboard and remove it from future history views.
- **FR-013**: The system MUST block access to any correction that does not belong to the signed-in user.
- **FR-014**: The system MUST keep the primary correction result structured enough for the UI to render each output field separately.

### Key Entities *(include if feature involves data)*

- **Usuario**: A person who creates an account, submits redacoes, and manages private history.
- **Redacao**: A submitted essay, whether entered as text or imported from a supported file.
- **Correcao**: The saved evaluation result for a redacao, including score, competence breakdown, feedback, errors, and rewritten text.
- **Historico de correcoes**: The user's list of previously saved redacoes and their correction results.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 90% of supported essays up to 600 words receive a complete correction result in under 30 seconds.
- **SC-002**: 100% of completed corrections include final score, five competence scores, detailed feedback, grammar errors, improvement suggestions, and an improved rewrite.
- **SC-003**: 95% of first-time users can complete their first correction without assistance.
- **SC-004**: 90% of signed-in users can reopen a previous correction from the dashboard in under 30 seconds.
- **SC-005**: 100% of delete actions remove the selected redacao from the user's history and prevent it from reopening.
- **SC-006**: 100% of unauthorized access attempts to another user's saved corrections are blocked.
