# Example Prompts

## Architecture Flow

```text
Use ExactSeq to create a self-contained interactive HTML sequence diagram.

System:
- Browser
- API Gateway
- Auth Service
- Redis cache
- Postgres
- Audit log

Show:
- login request
- token validation
- cache hit path
- cache miss path with Postgres fallback
- audit log write
- response to browser

Requirements:
- sticky participant rail
- pixel-aligned lifelines
- measured message endpoints
- first-degree hover and click highlighting
- store/cache highlighting for Redis, Postgres, and Audit log
- validate at 1440x900 and 1280x800
- report maxActorToLifelineDelta and maxMessageEndpointDelta
```

## Existing Diagram Update

```text
Use ExactSeq to update ./docs/payment-flow.html.

Read the existing actor list and steps first.
Add the refund path from API to Payment Processor to Ledger.
Keep the current visual style.
Do not invent services that are not in the source docs.
Validate the updated HTML and report alignment deltas.
```
