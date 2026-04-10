# Implementation Plan: Plataforma de Correcao ENEM com IA

**Branch**: `[001-correcao-redacao-enem]` | **Date**: `2026-04-10` | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-correcao-redacao-enem/spec.md`

## Summary

Build a SaaS-ready Next.js web app that accepts essay text or supported uploads, sends normalized
content to an AI correction pipeline, validates the structured JSON response, persists results in
PostgreSQL, and lets authenticated users review and delete prior corrections from a private
dashboard.

## Technical Context

**Language/Version**: TypeScript 5.x with the Next.js App Router  
**Primary Dependencies**: Next.js, React, Tailwind CSS, Prisma, PostgreSQL, Zod, password hashing
library, PDF/DOCX text extractors, AI provider SDK  
**Storage**: PostgreSQL  
**Testing**: Vitest, React Testing Library, Playwright  
**Target Platform**: Modern desktop and mobile web browsers  
**Project Type**: web  
**Performance Goals**: Most corrections should complete in under 30 seconds for essays up to about
600 words; dashboard pages should feel instant under normal load  
**Constraints**: Structured JSON responses, supported upload types only, authenticated history
access, server-side validation, low per-request cost, no direct UI-to-database access  
**Scale/Scope**: Single-product SaaS MVP with multi-user accounts, personal history, and room for
billing or tiers later

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ENEM scoring fidelity: pass
- Simple, fast UX: pass
- Clean, modular architecture: pass
- Data ownership and history: pass
- Authentication and safe inputs: pass
- Pragmatic quality and observability: pass

No constitution violations require justification for this plan.

## Project Structure

### Documentation (this feature)

```text
specs/001-correcao-redacao-enem/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
    └── openapi.yaml
```

### Source Code (repository root)

```text
app/
├── layout.tsx
├── page.tsx
├── dashboard/
│   └── page.tsx
├── auth/
│   ├── login/
│   │   └── page.tsx
│   └── register/
│       └── page.tsx
└── api/
    ├── auth/
    │   ├── login/
    │   │   └── route.ts
    │   ├── logout/
    │   │   └── route.ts
    │   └── register/
    │       └── route.ts
    └── corrections/
        ├── route.ts
        └── [id]/
            └── route.ts

src/
├── components/
│   ├── auth-form.tsx
│   ├── correction-result.tsx
│   ├── dashboard-list.tsx
│   ├── essay-editor.tsx
│   └── upload-input.tsx
├── lib/
│   ├── ai/
│   │   ├── correction-client.ts
│   │   ├── prompt-builder.ts
│   │   └── response-schema.ts
│   ├── auth/
│   ├── db/
│   ├── file/
│   └── validation/
└── server/
    ├── dto/
    ├── services/
    │   ├── auth-service.ts
    │   ├── correction-service.ts
    │   ├── history-service.ts
    │   └── upload-service.ts
    └── utils/
        └── essay-normalizer.ts

prisma/
├── schema.prisma
└── migrations/

tests/
├── unit/
├── integration/
└── e2e/
```

**Structure Decision**: Use a single Next.js web application with route handlers for API traffic, a
shared `src/` layer for UI and server utilities, and Prisma/PostgreSQL for persistence.

## Complexity Tracking

No constitution exceptions are needed. The simplest web-app architecture satisfies the feature and
keeps the plan aligned with the constitution.
