import pandas as pd
from src.handle_missing_values import (
    DropMissingValuesStrategy,
    FillMissingValuesStrategy,
    MissingValueHandler,
)
from zenml import step

@step
def handle_missing_values_step(df: pd.DataFrame, strategy: str = 'mean') -> pd.DataFrame:
    if stratety == 'drop':
        handler = MissingValueHandler(DropMissingValuesStrategy(axis=0))
    elif strategy in ['mean', 'mode', 'median', 'constant']:
        handler = MissingValueHandler(FillMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f'Unsupported missing value handling strategy: {strategy}')

    cleaned_df = handler.handle_missing_values(df)

    return cleaned_df