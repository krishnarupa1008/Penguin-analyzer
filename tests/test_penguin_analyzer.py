import pytest
import pandas as pd
from penguin_analyzer.data_loader import DataLoader
from penguin_analyzer.analyzer import PenguinAnalyzer

@pytest.fixture
def sample_data():
    # Small sample DataFrame mimicking penguins dataset
    data = {
        'species': ['Adelie', 'Gentoo', 'Adelie', 'Chinstrap'],
        'body_mass_g': [3700, 5000, 3800, 3700]
    }
    return pd.DataFrame(data)

def test_load_data():
    loader = DataLoader()
    df = loader.load_data()
    assert not df.empty
    assert 'species' in df.columns
    assert 'body_mass_g' in df.columns

def test_average_body_mass(sample_data):
    analyzer = PenguinAnalyzer(sample_data)
    avg = analyzer.average_body_mass()
    expected = sum(sample_data['body_mass_g']) / len(sample_data)
    assert avg == expected

def test_species_counts(sample_data):
    analyzer = PenguinAnalyzer(sample_data)
    counts = analyzer.species_counts()
    assert counts['Adelie'] == 2
    assert counts['Gentoo'] == 1
    assert counts['Chinstrap'] == 1

def test_filter_by_species(sample_data):
    analyzer = PenguinAnalyzer(sample_data)
    filtered = analyzer.filter_by_species('Adelie')
    assert len(filtered) == 2
    assert all(filtered['species'] == 'Adelie')
