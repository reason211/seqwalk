# Contributing

SeqWalk values changes that make generated sequence diagrams more readable, portable, and easier for agents to validate.

Good contributions include:

- better browser validation snippets;
- accessibility improvements;
- template fixes that preserve endpoint alignment;
- adapters for additional AI coding tools;
- examples that cover real architecture flows;
- documentation that makes installation clearer.

Before opening a pull request:

```bash
python3 scripts/validate_skill.py skill/seqwalk
```

For template changes, render an example diagram and check:

- no console errors;
- sticky participant rail after scrolling;
- `maxActorToLifelineDelta <= 1`;
- `maxMessageEndpointDelta <= 1`;
- first-degree hover and click highlighting;
- store/cache highlight mode when stores exist.

Keep persistent docs current-state oriented. Describe how SeqWalk works now, not how a change evolved.
