# Quickstart

## Prerequisites

- Node.js 20+
- npm
- PostgreSQL database
- AI API key

## Environment Variables

Create a `.env.local` file with values like:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/enem
AUTH_SECRET=replace-with-a-long-random-secret
AI_API_KEY=replace-with-your-api-key
AI_MODEL=replace-with-the-chosen-model
AI_BASE_URL=https://api.example.com
UPLOAD_MAX_MB=10
```

## Setup

1. Install dependencies: `npm install`
2. Create the database and set the environment variables
3. Run migrations: `npx prisma migrate dev`
4. Start the app: `npm run dev`

## Verification

1. Register a new account
2. Paste an essay and run a correction
3. Upload a `.txt`, `.pdf`, or `.docx` file and confirm the same result flow
4. Open the dashboard and verify history persistence
5. Delete a correction and confirm it disappears from the list

## Test Commands

- `npm run lint`
- `npm run test`
- `npm run test:e2e`

## Notes

- If the scripts above do not exist yet, create them during implementation.
- Keep the correction output JSON stable so the UI can render every field directly.
