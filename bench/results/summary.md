# Handover fidelity benchmark: results

Score = share of points (1 / 0.5 / 0 per question). Overall is the mean ± SD over runs (sessions × repeats). `pre-compaction` = questions whose facts were stated before a mid-session /compact.

| Condition | runs | Overall | ml-divergence | survival-revision | pre-compaction | evidence | gotcha | jargon | mental-map | next-action | no-go | pressure | running | superseded | taste | Handover chars | Handover time (s, median) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 6 | 0.34 ± 0.07 | 0.29 | 0.39 | 0.40 | 0.33 | 0.50 | 0.78 | 0.17 | 0.00 | 0.22 | 0.25 | 0.00 | 0.50 | 0.41 | 0 | 0 |
| compact | 6 | 0.89 ± 0.08 | 0.82 | 0.97 | 0.95 | 1.00 | 1.00 | 1.00 | 0.50 | 1.00 | 0.89 | 1.00 | 0.75 | 0.83 | 0.94 | 12020 | 101 |
| pocock-handoff | 6 | 0.88 ± 0.04 | 0.88 | 0.89 | 0.90 | 0.90 | 1.00 | 1.00 | 0.58 | 1.00 | 0.89 | 1.00 | 0.75 | 0.89 | 0.85 | 4594 | 87 |
| ykdojo-handoff | 6 | 0.88 ± 0.06 | 0.86 | 0.89 | 0.89 | 0.90 | 1.00 | 1.00 | 0.58 | 1.00 | 0.83 | 1.00 | 0.75 | 0.83 | 0.87 | 4739 | 65 |
| humanlayer-handoff | 6 | 0.84 ± 0.09 | 0.79 | 0.89 | 0.89 | 0.83 | 1.00 | 1.00 | 0.50 | 0.92 | 0.83 | 1.00 | 0.75 | 0.89 | 0.81 | 5603 | 96 |
| softaworks-handoff | 6 | 0.86 ± 0.07 | 0.81 | 0.91 | 0.90 | 0.97 | 1.00 | 1.00 | 0.50 | 1.00 | 0.78 | 1.00 | 0.67 | 0.83 | 0.85 | 7757 | 288 |
| willseltzer-handoff | 6 | 0.86 ± 0.04 | 0.82 | 0.89 | 0.92 | 0.93 | 1.00 | 1.00 | 0.50 | 0.83 | 0.83 | 1.00 | 0.75 | 0.83 | 0.85 | 7451 | 106 |
| remvisual-handoff | 6 | 0.90 ± 0.06 | 0.88 | 0.93 | 0.94 | 0.97 | 1.00 | 1.00 | 0.58 | 1.00 | 0.94 | 1.00 | 0.83 | 0.83 | 0.89 | 14052 | 206 |
| shift-change-quick | 6 | 0.94 ± 0.06 | 0.90 | 0.97 | 0.97 | 1.00 | 1.00 | 1.00 | 0.67 | 0.92 | 0.94 | 1.00 | 0.83 | 0.83 | 1.00 | 6822 | 133 |
| shift-change | 6 | 0.94 ± 0.05 | 0.90 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 0.58 | 0.92 | 1.00 | 1.00 | 0.75 | 0.94 | 1.00 | 7441 | 184 |

Excluded as infrastructure failures and re-run (7): compact-r3-1789750377.json, compact-r3.json, humanlayer-handoff-r2.json, shift-change-quick-r3-1789750388.json, shift-change-r2.json, shift-change-r3-1789750385.json, ykdojo-handoff-r2.json. Their files are kept in `results/<session>/failed/`.
