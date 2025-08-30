# AlphaSigma

AlphaSigma is a minimal service that plans stories with OpenAI, renders
videos via Google's Veo API, rotates visual styles, and publishes results.
It exposes a FastAPI backend used by the CLI and scheduler.

## Environment Setup

1. Copy `.env.sample` to `.env`.
2. Set the required variables:
   - `OPENAI_API_KEY`
   - `OPENAI_MODEL_ID`
   - `GCP_API_KEY`
   - `GCP_MODEL_ID`
   - `TIMEZONE`
3. `.env` is ignored by git so your secrets stay local.

## Docker

Build and start the API with a Selenium Chrome container:

```bash
docker compose up -d --build
```

The API will be available on `http://localhost:8000`. Stop the stack with:

```bash
docker compose down
```

### noVNC Access

The Selenium container exposes a noVNC interface on port `7900`. Visit
`http://localhost:7900` in your browser and log in with the default password
`secret` to observe the Chrome session.

## Endpoints

- `POST /plan` – create a story plan from a topic.
- `POST /render` – render a video from a plan and optional style.
- `POST /run-daily` – run the scheduler to plan, render, and publish.

### `curl` Examples

Create a plan:

```bash
curl -X POST http://localhost:8000/plan \
  -H 'Content-Type: application/json' \
  -d '{"topic":"space travel"}'
```

Render a video from a plan:

```bash
curl -X POST http://localhost:8000/render \
  -H 'Content-Type: application/json' \
  -d '{"plan":{"title":"Space","scenes":["Launch","Orbit"]},"style":"cinematic"}'
```

## Scheduler

The scheduler coordinates planning, rendering and publishing. Trigger it via:

```bash
curl -X POST http://localhost:8000/run-daily \
  -H 'Content-Type: application/json' \
  -d '{"topic":"space travel"}'
```

In production, call this endpoint from a cron job or other scheduler to run
the workflow daily.

## Publishing and Extensions

`Publisher` currently logs the URI of each rendered video. Extend this class to
support additional destinations:

- Social platforms such as YouTube, TikTok or Instagram.
- Storage services like Amazon S3 or Google Cloud Storage.

Custom implementations can authenticate with external services, upload the
rendered asset and return a link or identifier.

## Maintainers

See [PROMPT.md](PROMPT.md) for guidance on style headers, lens constraints, and dialogue conventions.

