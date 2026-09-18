# Binary editing safety

The editor follows conservative rules:

1. Detect the container/version before editing.
2. Keep unknown fields opaque.
3. Stage changes before writing.
4. Produce a preview of intended mutations.
5. Rebuild checksums/framing only through format-aware writers.
6. Verify round-trip parsing after rebuild.
7. Preserve the original and write a new copy.
8. Fail closed if a required structure/template is missing.

For game-save tooling, refusing an edit is often better engineering than producing a corrupted file that looked valid in memory.
