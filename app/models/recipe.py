from app.models.db import get_db_connection

class Recipe:
    @staticmethod
    def create(title, ingredients=None, instructions=None, notes=None, source_url=None, cooking_time=None, category_id=None):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO recipes (title, ingredients, instructions, notes, source_url, cooking_time, category_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (title, ingredients, instructions, notes, source_url, cooking_time, category_id))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM recipes ORDER BY created_at DESC').fetchall()

    @staticmethod
    def get_by_id(recipe_id):
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()

    @staticmethod
    def update(recipe_id, title, ingredients=None, instructions=None, notes=None, source_url=None, cooking_time=None, category_id=None):
        with get_db_connection() as conn:
            conn.execute('''
                UPDATE recipes
                SET title = ?, ingredients = ?, instructions = ?, notes = ?, source_url = ?, cooking_time = ?, category_id = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (title, ingredients, instructions, notes, source_url, cooking_time, category_id, recipe_id))
            conn.commit()

    @staticmethod
    def delete(recipe_id):
        with get_db_connection() as conn:
            conn.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
            conn.commit()
