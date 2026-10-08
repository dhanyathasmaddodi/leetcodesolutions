import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df_bigCountries=world[
        (world['area']>=3000000) | (world['population']>= 25000000)  
    ]
    result_df=df_bigCountries[
        ['name','population','area']
    ]
    return result_df
    