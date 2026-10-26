import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_ids = set(orders['customerId'])
    result = customers[~customers['id'].isin(ordered_ids)]
    import pandas as pd

    return result[['name']].rename(columns={'name': 'Customers'})