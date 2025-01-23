from .insert_data import (
    insert_data_users_roles,
    insert_data_artists,
    insert_data_albums,
    insert_types_data,
    insert_songs_data,
    insert_data_users_sessions_data)
from ...core.database import get_db


def load_all_test_data(is_active: bool = False):
    if not is_active:
        return
    db = next(get_db()) 
    try:
        insert_data_users_roles(db)
        insert_data_artists(db)
        insert_data_albums(db)
        insert_types_data(db)
        insert_songs_data(db)
        insert_data_users_sessions_data(db)
    finally:
        db.close()

    print("Test data loaded successfully.")