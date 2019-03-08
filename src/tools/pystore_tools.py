import pandas as pd
import pystore

def get_pystore(data_dir, store_label='iex_data_store'):
    """
    get pystore

    example:
        store = get_pystore(data_dir)

    :param data_dir:
    :param store_label:
    :return:
    """
    pystore.set_path(data_dir.as_posix())
    store = pystore.store(store_label)
    return store

def get_collection(data_dir, store_label='iex_data_store', key='IEX.INTRADAY'):
    """
    get collection from pystore

    example:
        collection = get_collection(data_dir, label)

    :param data_dir:
    :param key:
    :return:
    """
    store = get_pystore(data_dir, store_label)
    collection = store.collection(key)
    return collection

def get_item(symbol, data_dir, store_label='iex_data_store', key='IEX.INTRADAY'):
    """
    get item from store and collection

    example:
        item = get_item('ACWI', data_dir)
        df = item.to_pandas()
        cprint(df)

    :param symbol:
    :param data_dir:
    :param store_label:
    :param key:
    :return:
    """
    store = get_pystore(data_dir, store_label)
    collection = store.collection(key)
    item = collection.item(symbol)
    return item
