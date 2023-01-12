import pandas as pd

def merge_item(df_item: pd.DataFrame, df_shops: pd.DataFrame) -> pd.DataFrame:
    df_shops = df_shops.rename(columns={'id':'shop_id', 'name': 'shop_name'})
    df_merge = df_item.merge(df_shops, on='shop_id')
    return df_merge

def merge_order(df_order: pd.DataFrame, df_user: pd.DataFrame) -> pd.DataFrame:
    df_user = df_user.rename(columns={'id':'user_id', 'name': 'user_name'})
    df_merge = df_order.merge(df_user, on='user_id')
    return df_merge

def merge_all(df_item_shop: pd.DataFrame, df_order_user: pd.DataFrame) -> pd.DataFrame:
    """Merge item_shop and order_user for result table

    Args:
        df_item_shop (pd.DataFrame, required): dataframe of item and shop.
        df_order_user (pd.DataFrame, required): dataframe of order and user.
        
    Returns:
        pd.DataFrame: result of merge
    """

    df_item_shop = df_item_shop.rename(columns={'id':'item_id', 'name': 'item_name'})
    df_merge = df_order_user.merge(df_item_shop, on='item_id')
    return df_merge