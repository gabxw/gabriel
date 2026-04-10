# Data Model

## Entity: User

- **id**: UUID primary key
- **email**: Unique lowercase string
- **passwordHash**: Hashed password string
- **createdAt**: Creation timestamp
- **updatedAt**: Last update timestamp

**Relationships**

- One user owns many session records.
- One user owns many essay submissions.

**Validation**

- Email must be unique and required.
- Password is never stored in plain text.

## Entity: Session

- **id**: UUID primary key
- **userId**: Foreign key to User
- **tokenHash**: Hashed session token
- **expiresAt**: Expiration timestamp
- **revokedAt**: Optional revocation timestamp
- **createdAt**: Creation timestamp

**Relationships**

- Each session belongs to one user.

**Validation**

- Session tokens must expire and can be revoked.

## Entity: EssaySubmission

- **id**: UUID primary key
- **userId**: Foreign key to User
- **sourceType**: Enum `text` or `file`
- **originalText**: Raw user input or extracted text
- **normalizedText**: Cleaned text sent to the AI pipeline
- **originalFileName**: Optional uploaded file name
- **originalFileMimeType**: Optional uploaded file MIME type
- **originalFileSize**: Optional uploaded file size in bytes
- **status**: Enum `pending`, `processing`, `completed`, `failed`
- **errorMessage**: Optional human-readable failure message
- **createdAt**: Creation timestamp
- **updatedAt**: Last update timestamp

**Relationships**

- Each essay submission belongs to one user.
- Each essay submission has one correction record when completed.

**Validation**

- Exactly one input source is required: text or file.
- Normalized text must not be empty.
- Uploads must be limited to `.txt`, `.pdf`, and `.docx`.

## Entity: Correction

- **id**: UUID primary key
- **essaySubmissionId**: Unique foreign key to EssaySubmission
- **finalScore**: Integer from 0 to 1000
- **c1Score**: Integer from 0 to 200
- **c2Score**: Integer from 0 to 200
- **c3Score**: Integer from 0 to 200
- **c4Score**: Integer from 0 to 200
- **c5Score**: Integer from 0 to 200
- **grammarErrors**: JSON array of structured error objects
- **improvementSuggestions**: JSON array of strings
- **detailedFeedback**: Long-form feedback text
- **rewrittenEssay**: Improved essay version
- **aiModel**: Model identifier used for the correction
- **promptVersion**: Prompt version used for the run
- **processingMs**: Processing time in milliseconds
- **createdAt**: Creation timestamp

**Relationships**

- Each correction belongs to one essay submission.

**Validation**

- The five competence scores must stay within range.
- The final score must stay within 0 to 1000.
- The sum of the five competence scores should equal the final score.

## Relationship Notes

- Deleting a user should cascade to their sessions and essay history.
- Deleting an essay submission should remove its correction record.
- History queries should sort by `createdAt` descending.
- Dashboard list views should use essay submission metadata plus correction summary fields.
