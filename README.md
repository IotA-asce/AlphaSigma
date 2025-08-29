# AlphaSigma
Video generation maybe

## Configuration

1. Copy `.env.sample` to `.env` and fill in the required values.
2. Add your OpenAI and Google Cloud API keys.
3. Specify the model IDs and timezone.

`.env` is ignored by git, so your secrets stay local.

## Docker

Build and start the API with a Selenium Chrome container:

```bash
docker compose up -d --build
```

The API will be available on http://localhost:8000.
