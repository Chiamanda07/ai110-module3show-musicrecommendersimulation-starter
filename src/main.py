"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs.")

    # Starter example profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "tempo_bpm": 120,
        "valence": 0.75,
        "danceability": 0.8,
        "acousticness": 0.2,
    }

    # Edge case: conflicting energy and mood — high energy but sad mood.
    # Tests whether the scorer rewards energy proximity even when the mood is emotionally opposite.
    high_energy_sad = {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.9,
        "tempo_bpm": 130,
        "valence": 0.20,
        "danceability": 0.85,
        "acousticness": 0.10,
    }

    # Edge case: genre that doesn't exist in the catalog.
    # Genre score will always be 0.0 — tests whether the other features carry enough weight to still rank songs.
    unknown_genre = {
        "genre": "k-pop",
        "mood": "euphoric",
        "energy": 0.88,
        "tempo_bpm": 128,
        "valence": 0.90,
        "danceability": 0.92,
        "acousticness": 0.05,
    }

    # Edge case: contradictory acousticness and energy — wants fully acoustic AND maximum energy.
    # No song in the catalog scores high on both; tests which weight wins.
    acoustic_but_intense = {
        "genre": "folk",
        "mood": "intense",
        "energy": 1.0,
        "tempo_bpm": 160,
        "valence": 0.50,
        "danceability": 0.50,
        "acousticness": 1.0,
    }

    profiles = [
        ("Starter Profile",        user_prefs),
        ("High-Energy Sad",        high_energy_sad),
        ("Unknown Genre (k-pop)",  unknown_genre),
        ("Acoustic but Intense",   acoustic_but_intense),
    ]

    for profile_name, prefs in profiles:
        recommendations = recommend_songs(prefs, songs, k=5)

        print("\n" + "=" * 40)
        print(f"  Top 5 Recommendations — {profile_name}")
        print("=" * 40)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n#{i}: {song['title']} by {song['artist']}")
            print(f"    Score: {score:.2f}")
            print("    Reasons:")
            for reason in explanation.split(", "):
                print(f"      - {reason}")
        print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
