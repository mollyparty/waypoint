# Waypoint memory workflow

Version-Timestamp: 2026-09-05 18:00:00 UTC-4

## Ownership and context

Astra is the coordinating agent. Keep the active objective, phase, evidence, blockers and exact next action in `vault/01-Project/CURRENT-WORK.json`. Read it after START-HERE at session start. Other IDEs and models use the same files. The vault is durable memory; the graph is a derived retrieval aid.

## Checkpoint after meaningful work

1. Update CURRENT-WORK, the session note, and START-HERE. Change PROGRESS only if phase status changed. Record accepted decisions in the decision log; proposals remain pending until the authorized decision maker accepts them.
2. Run `python catalog/build.py` if catalog data changed. Run `python tools/memory.py check` and address errors.
3. Review graph facts against changed sources. Update only supported facts and retain superseded history explicitly. Run `python tools/memory.py baseline` after the review to record source hashes. This records a drift baseline, not semantic certification.
4. Stage only the intended files. Run `python tools/memory.py publish --tool "Codex desktop" --tool-version "unknown" --message "type(scope): summary"`, substituting the actual calling tool/version. It checks staged scope, requires memory evidence, commits with attribution, pushes the current branch to origin, and verifies the live remote hash. Failures exit nonzero; a failed push leaves the local commit available for retry with `git push origin HEAD`.
5. Run `python tools/memory.py report --remote` to refresh the local HTML status page. Open `memory/index.html`. Its timestamp is a snapshot, not a live background service. Generated status files are ignored because Git state becomes stale immediately after commits.

## Portable setup

Run `python tools/memory.py install` on each clone. It points Git at the tracked `.githooks` directory. Old local hooks remain recoverable in `.git/hooks`; the new hooks do not rebuild or erase graph data. To undo, restore the previous `core.hooksPath` value, or unset it if absent before installation. The installer prints the previous value.

Git hooks are local checks and can be bypassed by Git options. They do not replace human review. Obsidian Sync, if configured separately, is independent from GitHub. No service pushes every keystroke. The publish command is the checked agent checkpoint operation.

## Delegation contract

Give a specialist one bounded objective, applicable decision IDs, relevant source paths, allowed files, and acceptance criteria. Require its result to include changed files, sources, checks with outcomes, proposed decisions, unresolved questions, and next action. Astra reviews results before integrating them into shared memory. Use one writer for CURRENT-WORK and decision numbering. Preserve founder approval gates across retries, model changes, and context compaction.

## Verification and limits

The health check validates checkpoint fields, evidence paths, graph identifiers/endpoints/source paths, source hash drift, and generated catalog output. It cannot determine whether every natural-language claim is true or whether an unrecorded conversation contained a decision. Record decisions and checkpoints during work, not only at the end. Read sources when graph freshness is uncertain. Existing legacy graph claims require targeted review; a clean hash comparison alone is not proof of correctness.
