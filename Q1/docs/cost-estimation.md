# RAG Pipeline Cost Estimation

## Infrastructure

| Component | Choice | Cost |
|-----------|--------|------|
| Embedding model | sentence-transformers all-MiniLM-L6-v2 (local CPU) | $0 |
| LLM | OpenRouter `openrouter/free` (auto-router) | $0 |
| Vector database | ChromaDB (local, embedded) | $0 |
| **Total** | | **$0/month** |

## Usage Assumptions

- 15 engineers on the team
- Each engineer makes ~10 queries per working day
- ~22 working days per month
- Total: ~3,300 queries/month
- Average query: 2 chunks retrieved (~1500 tokens context)
- Average response: ~300 tokens

## Cost Breakdown

### Embeddings (sentence-transformers, local)
- Model: all-MiniLM-L6-v2 (~90MB, downloaded once)
- Runs on CPU, no API calls
- **Cost: $0**

### LLM Inference (OpenRouter free tier)
- Free tier auto-routes across available free models
- Current free models include: DeepSeek V4 Flash, NVIDIA Nemotron 3 Super, OpenAI gpt-oss-120b, GLM 4.5 Air
- Rate limit: ~200 requests/minute
- At 3,300 queries/month, peak rate is well under 1 request/minute
- **Cost: $0**

### Vector Database (ChromaDB)
- Embedded mode, runs locally
- No server, no cloud costs
- **Cost: $0**

## Scaling Path

If the team outgrows free tier limits (unlikely below ~50 engineers):

| Upgrade | Cost |
|---------|------|
| OpenRouter paid models | $0.10-0.50 per 1M tokens |
| Self-hosted Ollama (llama3.2:3b) | One-time GPU cost, $0/month inference |
| Even at 50 engineers, 20 queries/day each | Likely under $5/month |

## Notes

- The OpenRouter free tier is the most likely bottleneck. If rate limits are hit, queries will queue or fail gracefully.
- For a production deployment, a paid OpenRouter plan or self-hosted Ollama would provide more predictable performance.
- The all-MiniLM-L6-v2 embedding model provides adequate retrieval quality for a 20-note vault. For larger vaults (100+ notes), consider upgrading to a larger model or using OpenAI text-embedding-3-small ($0.02/1M tokens).
