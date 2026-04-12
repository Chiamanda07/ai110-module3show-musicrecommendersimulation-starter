# Reflection: Comparing User Profile Outputs

---

## Starter Profile vs. High-Energy Sad

These two profiles look very different on paper — one wants happy pop, the other wants sad pop with a high-energy feel. But their top 5 results were nearly identical: "Gym Hero" and "Sunrise City" topped both lists.

Why? Because both profiles share almost the same energy target (0.8 vs. 0.9), and energy is the heaviest signal in the scorer. Mood only gets a fraction of the weight. So the system essentially sees two "high-energy pop" users and ignores the emotional difference between them. In plain language: the recommender doesn't really understand *feelings* — it understands *speed and intensity*. A sad workout playlist and a happy dance playlist end up looking the same to it.

---

## High-Energy Sad vs. Unknown Genre (k-pop)

The High-Energy Sad profile at least got genre credit when a pop song appeared. The k-pop profile never got genre credit at all — zero points on every single song — because k-pop isn't in the catalog.

This meant the k-pop user's top 5 was decided almost entirely by who had the closest energy and tempo. All five songs scored between 0.55 and 0.59 — a razor-thin spread. For the High-Energy Sad profile the spread was wider (0.53–0.73) because genre matches created clear winners. The takeaway: without genre as a signal, the recommender gets flat and indecisive. It's like asking someone to pick your favorite restaurant but not telling them what cuisine you eat — they just default to "popular places near you."

---

## Unknown Genre (k-pop) vs. Acoustic but Intense

Both profiles were edge cases where the system struggled, but for different reasons.

The k-pop user got poor results because the *catalog* didn't have their genre — the algorithm was fine, the data just wasn't there. The Acoustic-but-Intense user got poor results because their two strongest preferences *contradict each other in real music* — almost no song is both fully acoustic and maximum energy. The system had to pick a side, and energy (the heavier weight) usually won, surfacing metal and rock songs with near-zero acousticness.

In plain language: the k-pop user was failed by a missing data problem. The acoustic-intense user was failed by a real-world physics problem — that combination of music mostly doesn't exist. No change to the algorithm would fix either issue without either expanding the catalog or redesigning what "acoustic" means in the scoring.

---

## Why Does "Gym Hero" Keep Showing Up for Happy Pop Users?

"Gym Hero" is tagged as *intense*, not *happy* — so intuitively it shouldn't top a happy pop list. But here's what the scorer actually sees:

- The user wants energy ~0.8. Gym Hero's energy is 0.93 — very close. That earns it a high energy score.
- The user wants pop genre. Gym Hero is pop. That earns it the full genre bonus.
- The user wants happy mood. Gym Hero is *intense*. That costs it mood points — but mood is a smaller weight than genre + energy combined.

So Gym Hero wins on the two biggest signals and only loses a small amount on mood. It's the recommender equivalent of a store recommending running shoes to someone who asked for casual sneakers — same brand, right color, close enough on the features that get measured, but emotionally not quite what you meant. The system doesn't know what "happy" *feels* like; it only knows that "happy" is a label that either matches or doesn't.
