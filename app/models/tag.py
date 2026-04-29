from app.models.db import get_db_connection

class Tag:
    @staticmethod
    def create(name):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tags (name) VALUES (?)', (name,))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM tags ORDER BY name').fetchall()

    @staticmethod
    def get_by_id(tag_id):
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM tags WHERE id = ?', (tag_id,)).fetchone()

    @staticmethod
    def delete(tag_id):
        with get_db_connection() as conn:
            conn.execute('DELETE FROM tags WHERE id = ?', (tag_id,))
            conn.commit()

class RecipeTag:
    @staticmethod
    def add_tag_to_recipe(recipe_id, tag_id):
        with get_db_connection() as conn:
            conn.execute('INSERT OR IGNORE INTO recipe_tags (recipe_id, tag_id) VALUES (?, ?)', (recipe_id, tag_id))
            conn.commit()

    @staticmethod
    def remove_tag_from_recipe(recipe_id, tag_id):
        with get_db_connection() as conn:
            conn.execute('DELETE FROM recipe_tags WHERE recipe_id = ? AND tag_id = ?', (recipe_id, tag_id))
            conn.commit()

    @staticmethod
    def get_tags_for_recipe(recipe_id):
        with get_db_connection() as conn:
            return conn.execute('''
                SELECT t.* FROM tags t
                JOIN recipe_tags rt ON t.id = rt.tag_id
                WHERE rt.recipe_id = ?
            ''', (recipe_id,)).fetchall()
