from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initializes the Recommender with a catalog of songs."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k song recommendations for the given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable explanation of why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    print(f"Loading songs from {csv_path}...")
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(dict(row))
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """
    Scores a single song against user preferences using the weighted algorithm.
    Returns (final_score, explanation).
    """
    reasons = []

    # Genre: 1.0 if exact match, 0.0 otherwise (weight: 0.15)
    genre_score = 1.0 if song["genre"] == user_prefs["genre"] else 0.0
    weighted_genre = 0.15 * genre_score
    reasons.append(f"genre match (+{weighted_genre:.2f})")

    # EXPERIMENT: mood check disabled
    # # Mood: 1.0 if exact match, 0.0 otherwise (weight: 0.225)
    # mood_score = 1.0 if song["mood"] == user_prefs["mood"] else 0.0
    # weighted_mood = 0.225 * mood_score
    # reasons.append(f"mood match (+{weighted_mood:.2f})")

    # Energy: proximity to target, 0.0–1.0 range (weight: 0.40)
    energy_score = max(0.0, 1.0 - abs(song["energy"] - user_prefs["energy"]))
    weighted_energy = 0.40 * energy_score
    reasons.append(f"energy fit (+{weighted_energy:.2f})")

    # Tempo: normalize difference over 60 BPM max gap (weight: 0.09)
    tempo_score = max(0.0, 1.0 - abs(song["tempo_bpm"] - user_prefs["tempo_bpm"]) / 60.0)
    weighted_tempo = 0.09 * tempo_score
    reasons.append(f"tempo fit (+{weighted_tempo:.2f})")

    # Valence: proximity to target (weight: 0.045)
    valence_score = max(0.0, 1.0 - abs(song["valence"] - user_prefs["valence"]))
    weighted_valence = 0.045 * valence_score
    reasons.append(f"valence fit (+{weighted_valence:.2f})")

    # Danceability: proximity to target (weight: 0.045)
    dance_score = max(0.0, 1.0 - abs(song["danceability"] - user_prefs["danceability"]))
    weighted_dance = 0.045 * dance_score
    reasons.append(f"danceability fit (+{weighted_dance:.2f})")

    # Acousticness: proximity to target (weight: 0.045)
    acoustic_score = max(0.0, 1.0 - abs(song["acousticness"] - user_prefs["acousticness"]))
    weighted_acoustic = 0.045 * acoustic_score
    reasons.append(f"acousticness fit (+{weighted_acoustic:.2f})")

    # NOTE: max score is ~0.775 while mood is disabled
    final_score = (
        weighted_genre
        + weighted_energy
        + weighted_tempo
        + weighted_valence
        + weighted_dance
        + weighted_acoustic
    )

    return final_score, ", ".join(reasons)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
