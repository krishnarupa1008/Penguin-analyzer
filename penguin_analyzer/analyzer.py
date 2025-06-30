import pandas as pd

class PenguinAnalyzer:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def average_body_mass(self):
        return self.df['body_mass_g'].mean()

    def species_counts(self):
        return self.df['species'].value_counts()

    def filter_by_species(self, species_name: str):
        return self.df[self.df['species'] == species_name]
