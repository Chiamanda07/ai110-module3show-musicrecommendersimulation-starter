# Model Card: Music Recommender Simulation

## 1. Model Name

**MoodMatch**

---

## 2. Intended Use

MoodMatch is designed to suggest songs from a small catalog based on what a user tells us they like. It assumes the user can describe their preferences with simple labels like genre, mood, and an energy level from 0 to 1. It should not be used to make decisions about real users without significant improvements to the dataset and algorithm.

---

## 3. How the Model Works

The recommender scores every song in the catalog against what the user says they want. It checks seven things: genre, mood, energy level, tempo, emotional positivity (valence), danceability, and how acoustic the song sounds. Each factor gets a score between 0 and 1. Then each score is multiplied by a weight. Genre and mood matter most, energy matters a lot, and the rest matter a little. All the weighted scores are added up to get a final number. The song with the highest number is recommended first.


---

## 4. Data

The catalog has 20 songs. Each song has a title, artist, genre, mood, and five numerical features: energy, tempo (BPM), valence, danceability, and acousticness. The genres include pop, lofi, rock, jazz, hip-hop, electronic, ambient, indie pop, r&b, classical, country, metal, folk, and reggae(  but most appear only once). However, the data doesn't have all the different type of genres like k-pop and Latin music, It also has very few calm or low-energy songs, and no song that is both high energy and highly acoustic at the same time.

---

## 5. Strengths

The system works best when the user's preferences are well-represented in the catalog. The scoring also handles songs that are "close enough"; it does not have to be a perfect match on every feature to rank highly, just strong on the features that carry the most weight.

---

## 6. Limitations and Bias

The catalog skews high-energy (the average song energy is around 0.60) so low-energy listeners get poor matches even when the algorithm is working correctly. A user who wants calm, soft music will find that almost every song scores near zero on energy, leaving the system with nothing useful to rank by. Genre matching is also all-or-nothing: a jazz fan gets full credit for the one jazz song and zero credit for everything else, even songs they might enjoy. This creates a filter bubble where underrepresented genres produce nearly useless results. Finally, the system currently has mood disabled from experiments, which means two users with opposite emotional preferences but similar energy levels get identical playlists.

---

## 7. Evaluation

Four profiles were tested:

- **Starter Profile** (pop, happy, energy 0.8): The baseline. Results felt reasonable, but "Gym Hero" — tagged as *intense*, not *happy* — kept showing up because its energy was close enough to earn more points than a mood mismatch would cost it.
- **High-Energy Sad** (pop, sad, energy 0.9): Results were nearly identical to the Starter Profile. The system could not meaningfully separate "sad" from "happy" when energy was similar.
- **Unknown Genre — k-pop** (k-pop, euphoric, energy 0.88): Every song scored zero for genre. The top 5 results were almost tied, with scores within 0.04 of each other. The playlist felt random.
- **Acoustic but Intense** (folk, intense, energy 1.0, acousticness 1.0): No catalog song satisfies both signals. Scores maxed out around 0.53. This exposed a catalog gap that no weight change can fix.

Two experiments were also run: doubling the energy weight showed that energy alone can dominate rankings, and disabling mood confirmed that emotional context matters more than the default weights suggest.

---

## 8. Future Work

- **Add artist diversity rules.** Right now the same artist can appear multiple times in the top 5. A simple rule like "no more than one song per artist" would make playlists feel more varied.
- **Replace binary genre matching with genre families.** Jazz and blues are similar; pop and indie pop are similar. A partial-match system would help users whose exact genre is rare in the catalog.
- **Expand the catalog.** Twenty songs is too small to serve users with niche tastes. Adding more low-energy, acoustic, and non-Western genres would directly fix the biggest bias found in testing.

---

## 9. Personal Reflection

**Biggest learning moment**

The data matters more than the algorithm. No matter how I adjusted the weights, the catalog's gaps (too few calm songs, abscence of some genres) created bad results for certain users that math alone couldn't fix.

**How AI tools helped — and when I needed to double-check**

AI tools were fast at applying weight changes and verifying the math summed to 1.0. But I still read the file after every edit to make sure the logic was actually correct, not just syntactically clean.

**What surprised me about how a simple algorithm can "feel" like a recommendation**

Even with just addition and seven features, the output felt surprisingly real. I think the labels do a lot of the work. "Genre match" and "energy fit" makes the system feel smart even when it is just arithmetic.

**What I would try next**

I would add a rule to prevent the same artist from appearing twice in one playlist. After that, I would replace the binary genre check with a similarity map so that pop and indie pop count as "close" instead of "totally different."
