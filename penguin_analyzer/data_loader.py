import seaborn as sns
import pandas as pd

class DataLoader:
    def __init__(self):
        self.df = None

    def load_data(self):
        self.df = sns.load_dataset('penguins')
        return self.df