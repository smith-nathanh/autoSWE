import pandas as pd

class TestValidator:
    def validate_renko(self, data: pd.DataFrame, expected: pd.DataFrame) -> bool:
        """
        Validate Renko chart data against expected results.
        """
        return data.equals(expected)

    def validate_line_break(self, data: pd.DataFrame, expected: pd.DataFrame) -> bool:
        """
        Validate Line Break chart data against expected results.
        """
        return data.equals(expected)