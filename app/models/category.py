from app.models.db import get_db_connection

class Category:
    @staticmethod
    def create(name):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (name,))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM categories ORDER BY name').fetchall()

    @staticmethod
    def get_by_id(category_id):
        with get_db_connection() as conn:
            return conn.execute('SELECT * FROM categories WHERE id = ?', (category_id,)).fetchone()

    @staticmethod
    def update(category_id, name):
        with get_db_connection() as conn:
            conn.execute('UPDATE categories SET name = ? WHERE id = ?', (name, category_id))
            conn.commit()

    @staticmethod
    def delete(category_id):
        with get_db_connection() as conn:
            conn.execute('DELETE FROM categories WHERE id = ?', (category_id,))
            conn.commit()
