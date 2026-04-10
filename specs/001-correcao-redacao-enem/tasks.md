# Tasks: Plataforma de Correcao ENEM com IA

**Input**: Design documents from `/specs/001-correcao-redacao-enem/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests were not explicitly requested in the feature spec, so this task list focuses on
implementation tasks and manual verification points.

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize the Next.js app scaffold and toolchain files in `package.json`, `tsconfig.json`, `next.config.ts`, `eslint.config.mjs`, `postcss.config.mjs`, and `tailwind.config.ts`
- [ ] T002 Create the base app shell, global styles, and landing route in `app/layout.tsx`, `app/page.tsx`, and `app/globals.css`
- [ ] T003 Add environment contract and database client bootstrap in `.env.example`, `src/lib/env.ts`, and `src/lib/db/prisma.ts`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Define the Prisma data model for users, sessions, essay submissions, and corrections in `prisma/schema.prisma` and create the initial migration in `prisma/migrations/0001_init/migration.sql`
- [ ] T005 [P] Implement shared password hashing and session token utilities in `src/lib/auth/password.ts` and `src/lib/auth/session.ts`
- [ ] T006 [P] Implement essay normalization and file extraction helpers in `src/server/services/upload-service.ts`, `src/server/utils/essay-normalizer.ts`, and `src/lib/file/text-extractor.ts`
- [ ] T007 [P] Define the AI correction prompt, response schema, and provider client in `src/lib/ai/prompt-builder.ts`, `src/lib/ai/response-schema.ts`, and `src/lib/ai/correction-client.ts`
- [ ] T008 [P] Add shared validation and ownership guard utilities in `src/lib/validation/auth.ts`, `src/lib/validation/correction.ts`, and `src/server/utils/require-user.ts`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Corrigir redacao com IA (Priority: P1) (MVP)

**Goal**: The user pastes an essay or uploads a supported file, clicks "Corrigir redacao", and receives a complete ENEM-style correction.

**Independent Test**: Submit a sample essay by text or supported file and confirm the structured correction result appears without account setup.

### Implementation for User Story 1

- [ ] T009 [P] [US1] Build the essay editor and file upload controls in `src/components/essay-editor.tsx` and `src/components/upload-input.tsx`
- [ ] T010 [P] [US1] Build the correction result view in `src/components/correction-result.tsx`
- [ ] T011 [US1] Compose the correction form with loading, submit, and response-state handling in `src/components/correction-form.tsx`
- [ ] T012 [US1] Wire the main landing page to the correction form and result state in `app/page.tsx`
- [ ] T013 [US1] Implement the correction submission API for pasted text and file uploads in `app/api/corrections/route.ts`
- [ ] T014 [US1] Implement the correction orchestration pipeline with AI validation and persistence in `src/server/services/correction-service.ts`
- [ ] T015 [US1] Render the structured correction payload, including final score, five competencies, grammar errors, suggestions, feedback, and rewritten essay in `src/components/correction-result.tsx`

**Checkpoint**: User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Criar conta e salvar historico (Priority: P2)

**Goal**: The user creates an email/password account, signs in, and can access a private dashboard with saved corrections.

**Independent Test**: Register a new account, complete a correction, sign out, sign back in, and confirm the correction is preserved in the dashboard history.

### Implementation for User Story 2

- [ ] T016 [P] [US2] Build the registration and login screens in `app/auth/register/page.tsx`, `app/auth/login/page.tsx`, and `src/components/auth-form.tsx`
- [ ] T017 [P] [US2] Implement the auth API routes for register, login, and logout in `app/api/auth/register/route.ts`, `app/api/auth/login/route.ts`, and `app/api/auth/logout/route.ts`
- [ ] T018 [US2] Implement server-side auth and session lifecycle logic in `src/server/services/auth-service.ts`, `src/lib/auth/session.ts`, and `src/lib/auth/password.ts`
- [ ] T019 [US2] Build the authenticated dashboard shell and history list in `app/dashboard/page.tsx` and `src/components/dashboard-list.tsx`
- [ ] T020 [US2] Implement the history listing and access-filtering service in `src/server/services/history-service.ts` and the GET branch of `app/api/corrections/route.ts`

**Checkpoint**: At this point, user account creation and private history access should work independently of the delete/open flow

---

## Phase 5: User Story 3 - Revisar e gerenciar correcoes antigas (Priority: P3)

**Goal**: The signed-in user can open a saved correction from the dashboard and delete old essays they no longer want to keep.

**Independent Test**: Open a saved correction from the dashboard, delete it, and confirm it no longer appears or opens again.

### Implementation for User Story 3

- [ ] T021 [P] [US3] Implement the saved-correction read and delete endpoints with ownership checks in `app/api/corrections/[id]/route.ts`
- [ ] T022 [P] [US3] Build the saved-correction detail page in `app/dashboard/[id]/page.tsx` and reuse `src/components/correction-result.tsx`
- [ ] T023 [US3] Wire open and delete actions from the dashboard list in `src/components/dashboard-list.tsx`
- [ ] T024 [US3] Implement deletion cascade and unauthorized-access handling in `src/server/services/history-service.ts` and `src/server/utils/require-user.ts`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T025 [P] Harden empty, loading, error, and unauthorized states across `src/components/correction-form.tsx`, `src/components/auth-form.tsx`, and `src/components/dashboard-list.tsx`
- [ ] T026 [P] Refine responsive layout, visual hierarchy, and accessibility tokens in `app/globals.css`, `app/layout.tsx`, and `tailwind.config.ts`
- [ ] T027 Add logging and latency/failure hooks for the correction pipeline in `src/server/utils/logger.ts` and `src/server/services/correction-service.ts`
- [ ] T028 Update quickstart implementation notes in `specs/001-correcao-redacao-enem/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in priority order (P1 -> P2 -> P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Uses the correction history created by User Story 1 for end-to-end verification
- **User Story 3 (P3)**: Can start after User Story 2 - May integrate with User Story 1 and 2 components but should remain independently testable

### Within Each User Story

- Core data and service boundaries before UI wiring
- UI components before route integration
- API routes before dashboard or page actions
- Independent story complete before moving to the next priority

### Parallel Opportunities

- T005-T008 can be worked in parallel once the Prisma schema shape is agreed
- T009 and T010 can be built in parallel for User Story 1
- T016 and T017 can be built in parallel for User Story 2
- T021 and T022 can be built in parallel for User Story 3
- T025 and T026 can be polished in parallel

---

## Parallel Example: User Story 1

```bash
# Build the editor and result view together:
Task: "Build the essay editor and file upload controls in src/components/essay-editor.tsx and src/components/upload-input.tsx"
Task: "Build the correction result view in src/components/correction-result.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Demo the correction flow before adding authentication or history

### Incremental Delivery

1. Deliver the correction flow first so the product has immediate value
2. Add account creation and private history second
3. Add opening and deletion of prior corrections third
4. Finish with polish, accessibility, and observability improvements
