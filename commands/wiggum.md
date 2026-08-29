---
description: Explicitly turn on bounded autonomous mode with frozen scope and one root orchestrator
disable-model-invocation: true
---

Enter bounded autonomous mode as sole root. Freeze scope, risk, expected surface, and budgets. Stop on expansion, two repair rounds, three identical failures, ownership conflict, or destructive action. Do not run this command from another skill.

Always read the environment you need from the current working tree's direnv. Never use `nix develop` to run commands, and never install dependencies on the fly. If you are blocked on a dependency requirement, stop working and ask for the dependency you need. If it can be added to the Nix environment, then do so, regenerate the environment using `de`, and then re-read the direnv environment and try again.

Follow `wiggum` and `change-control`: smallest correct diff, risk-proportionate checks, leaf delegation, one stable-candidate review, one final gate, durable counters, and escalation before expansion.

When available, use Anvil via your `anvil` skill as the default for every operation it supports. Check unsaved Emacs buffers before each edit batch; prefer Anvil for file exploration and git queries. Fall back to shell or apply_patch only when required, and briefly state why. Recheck Anvil state before committing.

$ARGUMENTS
