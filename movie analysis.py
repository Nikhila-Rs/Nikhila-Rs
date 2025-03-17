import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Load sample movie ratings data."""
    data = {
        "Movie": [
            "Inception", "The Dark Knight", "Interstellar", "Titanic", "Avatar",
            "Toy Story", "Finding Nemo", "Frozen", "The Lion King", "Shrek"
        ],
        "Rating": [8.8, 9.0, 8.6, 7.8, 7.9, 8.3, 8.1, 7.5, 8.5, 7.9]
    }
    df = pd.DataFrame(data)
    return df

def analyze_ratings(df):
    """Analyze movie ratings and print insights."""
    if df is None:
        return
    
    print("\nMovie Ratings Analysis:")
    print(f"Total movies: {df.shape[0]}")
    print(f"Average rating: {df['Rating'].mean():.2f}")
    print(f"Highest-rated movie: {df.loc[df['Rating'].idxmax(), 'Movie']} ({df['Rating'].max()})")
    print(f"Lowest-rated movie: {df.loc[df['Rating'].idxmin(), 'Movie']} ({df['Rating'].min()})")
  
    plt.figure(figsize=(10, 5))
    plt.barh(df['Movie'], df['Rating'], color='skyblue')
    plt.xlabel("Rating")
    plt.ylabel("Movie")
    plt.title("Movie Ratings Visualization")
    plt.gca().invert_yaxis()
    plt.show()

def main():
    df = load_data()
    analyze_ratings(df)

if __name__ == "__main__":
    main()
