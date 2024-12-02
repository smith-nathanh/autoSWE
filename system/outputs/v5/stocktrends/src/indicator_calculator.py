import pandas as pd
import numpy as np

class IndicatorCalculator:
    def calculate_renko(self, data: pd.DataFrame, brick_size: float) -> pd.DataFrame:
        """Calculate Renko chart data."""
        renko_data = []
        last_close = data['close'].iloc[0]
        for i in range(1, len(data)):
            price_change = data['close'].iloc[i] - last_close
            while abs(price_change) >= brick_size:
                renko_data.append(last_close + np.sign(price_change) * brick_size)
                last_close += np.sign(price_change) * brick_size
                price_change = data['close'].iloc[i] - last_close
        return pd.DataFrame(renko_data, columns=['renko_close'])

    def calculate_line_break(self, data: pd.DataFrame, line_count: int) -> pd.DataFrame:
        """Calculate Line Break chart data."""
        line_break_data = []
        last_close = data['close'].iloc[0]
        for i in range(1, len(data)):
            if len(line_break_data) < line_count or data['close'].iloc[i] > max(line_break_data[-line_count:]):
                line_break_data.append(data['close'].iloc[i])
            elif data['close'].iloc[i] < min(line_break_data[-line_count:]):
                line_break_data.append(data['close'].iloc[i])
        return pd.DataFrame(line_break_data, columns=['line_break_close'])

    def calculate_pnf(self, data: pd.DataFrame) -> pd.DataFrame:
        """Calculate Point and Figure chart data."""
        pnf_data = []
        last_close = data['close'].iloc[0]
        for i in range(1, len(data)):
            if data['close'].iloc[i] > last_close:
                pnf_data.append('X')
            elif data['close'].iloc[i] < last_close:
                pnf_data.append('O')
            last_close = data['close'].iloc[i]
        return pd.DataFrame(pnf_data, columns=['pnf'])