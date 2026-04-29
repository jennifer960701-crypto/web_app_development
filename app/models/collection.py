from app.models.db import get_db_connection

class Collection:
    @staticmethod
    def create(name, sort_order=0):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO collections (name, sort_order) VALUES (?, ?)', (name, sort_order))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM collections ORDER BY sort_order').fetchall()

    @staticmethod
    def get_by_id(collection_id):
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM collections WHERE id = ?', (collection_id,)).fetchone()

    @staticmethod
    def update(collection_id, name, sort_order):
        with get_db_connection() as conn:
            conn.execute('UPDATE collections SET name = ?, sort_order = ? WHERE id = ?', (name, sort_order, collection_id))
            conn.commit()

    @staticmethod
    def delete(collection_id):
        with get_db_connection() as conn:
            conn.execute('DELETE FROM collections WHERE id = ?', (collection_id,))
            conn.commit()

class CollectionRecipe:
    @staticmethod
    def add_recipe_to_collection(collection_id, recipe_id, sort_order=0):
        with get_db_connection() as conn:
            conn.execute('INSERT OR IGNORE INTO collection_recipes (collection_id, recipe_id, sort_order) VALUES (?, ?, ?)', 
                         (collection_id, recipe_id, sort_order))
            conn.commit()

    @staticmethod
    def remove_recipe_from_collection(collection_id, recipe_id):
        with get_db_connection() as conn:
            conn.execute('DELETE FROM collection_recipes WHERE collection_id = ? AND recipe_id = ?', (collection_id, recipe_id))
            conn.commit()

    @staticmethod
    def get_recipes_in_collection(collection_id):
        with get_db_connection() as conn:
            return conn.execute('''
                SELECT r.* FROM recipes r
                JOIN collection_recipes cr ON r.id = cr.recipe_id
                WHERE cr.collection_id = ?
                ORDER BY cr.sort_order
            ''', (collection_id,)).fetchall()
