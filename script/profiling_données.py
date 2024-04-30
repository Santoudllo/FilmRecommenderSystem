import warnings
from ydata_profiling import ProfileReport
import pandas as pd

# Ignorer les avertissements de dépréciation de pandas_profiling

warnings.filterwarnings("ignore", category=DeprecationWarning)

train = pd.read_csv('../data/movies_data.csv')
# le rapport de profilage

prof = ProfileReport(train)
prof.to_file(output_file='rapport.html')
