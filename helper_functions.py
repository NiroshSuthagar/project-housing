import pandas as pd

def concat_list_of_df(list_item):
    try:
        if len(list_item) == 1:
            return list_item[0].copy()
        
        combined = pd.concat(list_item, ignore_index=True, axis=0)
        return combined
    
    except Exception as e:
        print(f'Combining dataframes errored with: {e}')
        
