import sqlite3
from app.models.db import get_db_connection

class Collection:
    @staticmethod
    def create(data):
        """
        新增一筆收藏夾記錄
        :param data: dict 包含 name, sort_order
        :return: 新增的記錄 ID 或 None
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO collections (name, sort_order) VALUES (?, ?)', 
                               (data.get('name'), data.get('sort_order', 0)))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Collection.create 發生錯誤: {e}")
            return None

    @staticmethod
    def get_all():
        """取得所有收藏夾記錄"""
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM collections ORDER BY sort_order').fetchall()
        except sqlite3.Error as e:
            print(f"Collection.get_all 發生錯誤: {e}")
            return []

    @staticmethod
    def get_by_id(collection_id):
        """取得單筆收藏夾記錄"""
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM collections WHERE id = ?', (collection_id,)).fetchone()
        except sqlite3.Error as e:
            print(f"Collection.get_by_id 發生錯誤: {e}")
            return None

    @staticmethod
    def update(collection_id, data):
        """更新收藏夾記錄"""
        try:
            with get_db_connection() as conn:
                conn.execute('UPDATE collections SET name = ?, sort_order = ? WHERE id = ?', 
                             (data.get('name'), data.get('sort_order', 0), collection_id))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Collection.update 發生錯誤: {e}")
            return False

    @staticmethod
    def delete(collection_id):
        """刪除收藏夾記錄"""
        try:
            with get_db_connection() as conn:
                conn.execute('DELETE FROM collections WHERE id = ?', (collection_id,))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Collection.delete 發生錯誤: {e}")
            return False

class CollectionRecipe:
    @staticmethod
    def add_recipe_to_collection(collection_id, recipe_id, sort_order=0):
        """加入食譜到收藏夾"""
        try:
            with get_db_connection() as conn:
                conn.execute('INSERT OR IGNORE INTO collection_recipes (collection_id, recipe_id, sort_order) VALUES (?, ?, ?)', 
                             (collection_id, recipe_id, sort_order))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"CollectionRecipe.add_recipe_to_collection 發生錯誤: {e}")
            return False

    @staticmethod
    def remove_recipe_from_collection(collection_id, recipe_id):
        """從收藏夾移除食譜"""
        try:
            with get_db_connection() as conn:
                conn.execute('DELETE FROM collection_recipes WHERE collection_id = ? AND recipe_id = ?', (collection_id, recipe_id))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"CollectionRecipe.remove_recipe_from_collection 發生錯誤: {e}")
            return False

    @staticmethod
    def get_recipes_in_collection(collection_id):
        """取得收藏夾裡的所有食譜"""
        try:
            with get_db_connection() as conn:
                return conn.execute('''
                    SELECT r.* FROM recipes r
                    JOIN collection_recipes cr ON r.id = cr.recipe_id
                    WHERE cr.collection_id = ?
                    ORDER BY cr.sort_order
                ''', (collection_id,)).fetchall()
        except sqlite3.Error as e:
            print(f"CollectionRecipe.get_recipes_in_collection 發生錯誤: {e}")
            return []
