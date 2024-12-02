import pandas as pd

class InstrumentAnalyzer:
    def analyze_instrument(self, data: pd.DataFrame, instrument_type: str):
        """Analyze financial instrument data."""
        if instrument_type == 'stock':
            return self._analyze_stock(data)
        elif instrument_type == 'commodity':
            return self._analyze_commodity(data)
        else:
            raise ValueError("Unsupported instrument type")

    def _analyze_stock(self, data: pd.DataFrame):
        """Perform stock analysis."""
        return {
            'average_close': data['close'].mean(),
            'max_close': data['close'].max(),
            'min_close': data['close'].min()
        }

    def _analyze_commodity(self, data: pd.DataFrame):
        """Perform commodity analysis."""
        return {
            'average_close': data['close'].mean(),
            'max_close': data['close'].max(),
            'min_close': data['close'].min()
        }