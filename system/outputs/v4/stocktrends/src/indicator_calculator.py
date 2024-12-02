import pandas as pd
import numpy as np

class IndicatorCalculator:
    def calculate_renko(self, data: pd.DataFrame, brick_size: float) -> pd.DataFrame:
        """
        Calculate Renko chart data.
        """
        renko_data = []
        last_close = data['close'].iloc[0]
        for i in range(1, len(data)):
            price_change = data['close'].iloc[i] - last_close
            if abs(price_change) >= brick_size:
                bricks = int(price_change / brick_size)
                for _ in range(abs(bricks)):
                    renko_data.append(last_close + np.sign(price_change) * brick_size)
                    last_close += np.sign(price_change) * brick_size
        return pd.DataFrame(renko_data, columns=['close'])

    def calculate_line_break(self, data: pd.DataFrame, line_count: int) -> pd.DataFrame:
        """
        Calculate Line Break chart data.
        """
        line_break_data = []
        for i in range(line_count, len(data)):
            if data['close'].iloc[i] > max(data['close'].iloc[i-line_count:i]) or \
               data['close'].iloc[i] < min(data['close'].iloc[i-line_count:i]):
                line_break_data.append(data['close'].iloc[i])
        return pd.DataFrame(line_break_data, columns=['close'])

    def calculate_pnf(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate Point and Figure chart data.
        """
        pnf_data = []
        last_price = data['close'].iloc[0]
        for i in range(1, len(data)):
            if data['close'].iloc[i] != last_price:
                pnf_data.append(data['close'].iloc[i])
                last_price = data['close'].iloc[i]
        return pd.DataFrame(pnf_data, columns=['close'])