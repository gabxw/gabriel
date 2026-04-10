# Research: Plataforma de Correcao ENEM com IA

## Decision 1: Server-side correction pipeline

- **Decision**: Normalize essay input in route handlers, send it through an AI adapter, validate
  the structured JSON output, and persist the result before responding.
- **Rationale**: Keeps secrets server-side, ensures deterministic rendering, and lets the dashboard
  replay the same result later.
- **Alternatives considered**: Client-side AI calls, free-form text output, and background-only
  processing.

## Decision 2: Auth and session model

- **Decision**: Use email/password authentication with server-issued secure sessions and hashed
  passwords.
- **Rationale**: Matches the product requirement, keeps the UX simple, and supports private
  history.
- **Alternatives considered**: OAuth/SSO, magic links, or local-storage JWTs.

## Decision 3: File ingestion

- **Decision**: Accept only `.txt`, `.pdf`, and `.docx` uploads, parse them on the server, normalize
  whitespace, and reject unsupported or unreadable files.
- **Rationale**: Guarantees the AI sees consistent text and lets the UI return precise validation
  errors.
- **Alternatives considered**: Browser-side extraction or storing binary uploads without
  normalization.

## Decision 4: Structured AI response

- **Decision**: Require the AI to return JSON that matches a strict schema with the final score,
  five competence scores, grammar errors, suggestions, feedback, and a rewritten essay.
- **Rationale**: The UI and database both need stable fields; malformed output must fail fast.
- **Alternatives considered**: Free-form completion text or post-processing natural language into
  data.

## Decision 5: Data persistence model

- **Decision**: Store users, sessions, essay submissions, and corrections in PostgreSQL through
  Prisma, with one essay mapped to one correction.
- **Rationale**: Simple relational storage fits access control, history queries, and deletion.
- **Alternatives considered**: Document store, blob storage, or denormalized history records.

## Decision 6: SaaS readiness

- **Decision**: Keep the code split into UI, services, ai, and db layers, with typed request and
  response boundaries.
- **Rationale**: The product can later add billing, tiers, and usage controls without rewriting the
  core correction flow.
- **Alternatives considered**: Page-level monoliths and direct provider calls from components.

## Open Questions

No open clarification items remain for the current plan.
