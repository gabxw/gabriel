<!--
Sync Impact Report
Version change: unversioned template -> 1.0.0
Modified principles:
- Placeholder principles -> I. ENEM Scoring Fidelity
- Placeholder principles -> II. Simple, Fast UX
- Placeholder principles -> III. Clean, Modular Architecture
- Placeholder principles -> IV. Data Ownership and History
- Placeholder principles -> V. Authentication and Safe Inputs
- Placeholder principles -> VI. Pragmatic Quality and Observability
Added sections:
- Technical Standards
- Product Standards
Removed sections:
- none
Templates reviewed:
- ✅ .specify/templates/plan-template.md - constitution check remains compatible; no edits needed
- ✅ .specify/templates/spec-template.md - requirement structure already aligns; no edits needed
- ✅ .specify/templates/tasks-template.md - task structure already aligns; no edits needed
Deferred items:
- none
-->

# Plataforma de Correção ENEM Constitution

## Core Principles

### I. ENEM Scoring Fidelity
The product MUST correct redações strictly by the ENEM rubric. Every correction MUST return a
final score from 0 to 1000 and five competency scores in fixed order: competence 1 (norma culta),
competence 2 (compreensão do tema), competence 3 (argumentação), competence 4 (coesão), and
competence 5 (proposta de intervenção). The response MUST also include grammar errors,
improvement suggestions, detailed feedback, and an improved rewrite. Any scoring or feedback logic
that diverges from this rubric is out of bounds.

Rationale: the platform only has value if users can trust the evaluation model to match ENEM
expectations.

### II. Simple, Fast UX
The primary flow MUST be simple: paste text or upload a file, click one correction button, and
receive the result without extra setup. The interface MUST stay responsive on desktop and mobile,
avoid unnecessary steps, and prioritize fast perceived performance. New UI complexity MUST be
rejected unless it clearly improves correction quality, speed, or task completion.

Rationale: the product competes on speed and clarity, not on feature sprawl.

### III. Clean, Modular Architecture
The codebase MUST use Next.js with TypeScript and keep responsibilities separated into UI,
services, ai, and db layers. Server logic MUST live in Next.js API routes or route handlers inside
the same application; the UI MUST not talk directly to the database or AI provider. Modules MUST
stay small, typed, and easy to test. Additional abstractions are allowed only when they reduce
coupling or make the correction pipeline clearer.

Rationale: clean boundaries reduce regressions and keep the codebase maintainable as the product
grows.

### IV. Data Ownership and History
Each user MUST own their own redações, corrections, and history. The application MUST persist
essays, scores, feedback, and related metadata in PostgreSQL through Prisma so previous corrections
can be reopened exactly as saved. Deletion MUST remove the user's selected redação from history and
prevent future access through the dashboard. Data structures MUST be designed for reliable
retrieval, not just for a single one-off correction.

Rationale: users need a dependable history of their work, and the product depends on trustworthy
persistence.

### V. Authentication and Safe Inputs
The platform MUST require email-and-password authentication before users can store or revisit
corrections. File uploads MUST accept only `.txt`, `.pdf`, and `.docx`, and every upload MUST be
validated and normalized before it reaches the AI layer. Access control MUST ensure a user can only
view, open, or delete their own redações and results. Secrets and provider credentials MUST stay
out of source control.

Rationale: the product handles personal writing and must protect user data by default.

### VI. Pragmatic Quality and Observability
Core flows MUST be testable, and the implementation MUST include validation and clear error handling
for upload parsing, AI failures, and persistence errors. Code MUST remain legible with brief
comments only where the logic is not obvious. Logging and metrics MUST focus on the correction
pipeline, latency, and failure modes that affect user experience. The team MUST prefer the simplest
implementation that meets the requirement.

Rationale: reliability matters, but the project must avoid overengineering.

## Technical Standards

- The application MUST be built in Next.js with TypeScript.
- UI styling MUST use Tailwind.
- Backend behavior MUST be implemented inside Next.js API routes or route handlers.
- Persistence MUST use PostgreSQL with Prisma ORM.
- AI correction MUST run behind a dedicated `ai` service boundary.
- UI, services, ai, and db layers MUST remain separated and import in that direction only.
- Text input and file upload MUST feed the same correction pipeline after validation and
  normalization.
- The system MUST support authenticated login and registration with email and password.
- The dashboard MUST load correction history and allow open/delete actions for prior essays.

## Product Standards

- Users MUST be able to start a correction by pasting a redação or uploading a file.
- The correction result MUST include final score, scores per competence, grammar errors,
  suggestions, detailed feedback, and a rewritten version.
- The dashboard MUST show historical corrections and provide access to older items.
- The product MUST support deleting a redação from the history view.
- The default experience MUST stay simple and fast, with the correction action as the main call to
  action.
- The platform MUST avoid extra configuration steps that do not improve the user's result.

## Governance

- This constitution overrides lower-level implementation notes whenever they conflict.
- Changes MUST be proposed with a clear reason, a version bump, and the downstream files that need
  alignment.
- Versioning MUST follow semantic versioning:
  - MAJOR for rubric changes, auth model changes, data model changes, or other breaking governance
    changes.
  - MINOR for new capabilities or material expansions of existing rules.
  - PATCH for wording changes, clarifications, and non-semantic refinements.
- Compliance review MUST happen before spec, plan, and task work proceeds. Any spec, plan, or task
  set that conflicts with this constitution MUST be revised or explicitly justified through a
  constitution update first.
- Any change to the AI scoring rubric or the user data lifecycle MUST include a written rationale
  and a sync impact report in the updated constitution.
- The implementation MUST stay within the approved stack unless a constitution amendment explicitly
  changes it.

**Version**: 1.0.0 | **Ratified**: 2026-04-10 | **Last Amended**: 2026-04-10
