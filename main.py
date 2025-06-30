from penguin_analyzer.data_loader import DataLoader
from penguin_analyzer.analyzer import PenguinAnalyzer

def main():
    # Load data
    loader = DataLoader()
    df = loader.load_data()

    # Analyze data
    analyzer = PenguinAnalyzer(df)
    print("Average Body Mass (g):", analyzer.average_body_mass())
    print("\nSpecies Counts:\n", analyzer.species_counts())

    # Filter by species
    print("\nFiltered Penguins (Adelie):\n", analyzer.filter_by_species("Adelie"))

if __name__ == "__main__":
    main()
