from app.models.menu_item import MenuItem

def create_menu_item(db_session, menu_item_data):
    new_item = MenuItem(**menu_item_data.dict())
    db_session.add(new_item)
    db_session.commit()
    db_session.refresh(new_item)
    return new_item