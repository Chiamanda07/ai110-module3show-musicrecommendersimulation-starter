# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The system's biggest structural weakness is that the catalog skews high-energy — the average song energy is ~0.60 — which means low-energy listeners consistently receive poor matches even when the algorithm is working correctly. Because energy proximity is calculated as a simple linear gap (`1.0 - |song_energy - target_energy|`), a user who wants calm, soft music (energy ~0.1) finds that most songs in the catalog score near zero on that signal, leaving the recommender with little meaningful data to rank by. During experiments, this showed up clearly with the "Acoustic but Intense" profile: no song in the catalog has both high energy and high acousticness simultaneously, so the system was forced to sacrifice one preference entirely. Additionally, genre matching is binary — a jazz fan gets full credit on the one jazz song and nothing on any other, even styles they would likely enjoy — which creates a filter bubble where underrepresented genres lock users into a single track recommendation regardless of k. These issues are catalog problems as much as algorithm problems: no weight-tuning can recommend music that was never added to the dataset.

---

## 7. Evaluation  

Four user profiles were tested to check whether the scoring logic behaved as expected across normal and edge-case inputs.

**Starter Profile** (pop, happy, energy 0.8) was the baseline — a typical listener who likes upbeat, danceable pop. The system reliably surfaced "Sunrise City" and "Gym Hero" at the top, which felt right. What was surprising is that "Gym Hero" — a song tagged as *intense*, not *happy* — kept appearing in the top 2 even for the happy pop profile. The reason: its energy (0.93) is very close to the user's target (0.8), which earns it nearly as much weight as a perfect genre match. Mood being a smaller signal (or disabled during experiments) meant the emotional mismatch barely cost it anything.

**High-Energy Sad** (pop, sad, energy 0.9) tested whether the system could separate emotional tone from physical energy. It mostly could not — the top results were nearly identical to the Starter Profile because energy dominated. A truly "sad" song recommendation would require mood to carry more weight than the current scoring gives it.

**Unknown Genre — k-pop** (k-pop, euphoric, energy 0.88) tested what happens when a user's genre simply doesn't exist in the catalog. Every song scored 0 for genre, so rankings were decided entirely by energy and tempo proximity. All five results scored within 0.04 of each other — the system had almost no basis for differentiation and the playlist felt arbitrary.

**Acoustic but Intense** (folk, intense, energy 1.0, acousticness 1.0) was the most revealing edge case. No song in the 20-song catalog has both high energy and high acousticness at the same time — these two features naturally conflict in real music. The system was forced to pick one and ignore the other, and the results (max score ~0.53) exposed a catalog gap that weight adjustments alone cannot fix.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
