import pandas as pd

class InstrumentAnalyzer:
    def analyze_instrument(self, data: pd.DataFrame, instrument_type: str):
        """
        Analyze the financial instrument data.
        """
        if instrument_type == 'stock':
            return self._analyze_stock(data)
        elif instrument_type == 'commodity':
            return self._analyze_commodity(data)
        else:
            raise ValueError("Unsupported instrument type")

    def _analyze_stock(self, data: pd.DataFrame):
        """
        Perform stock-specific analysis.
        """
        return {'average_close': data['close'].mean()}

    def _analyze_commodity(self, data: pd.DataFrame):
        """
        Perform commodity-specific analysis.
        """
        return {'average_close': data['close'].mean()}