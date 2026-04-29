import sqlite3
from app.models.db import get_db_connection

class Recipe:
    @staticmethod
    def create(data):
        """
        新增一筆食譜記錄
        :param data: dict 包含 title, ingredients, instructions, notes, source_url, cooking_time, category_id
        :return: 新增的記錄 ID 或 None (發生錯誤)
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO recipes (title, ingredients, instructions, notes, source_url, cooking_time, category_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('title'), data.get('ingredients'), data.get('instructions'), 
                    data.get('notes'), data.get('source_url'), data.get('cooking_time'), 
                    data.get('category_id')
                ))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Recipe.create 發生錯誤: {e}")
            return None

    @staticmethod
    def get_all():
        """
        取得所有食譜記錄
        :return: 食譜列表 (sqlite3.Row 物件)
        """
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM recipes ORDER BY created_at DESC').fetchall()
        except sqlite3.Error as e:
            print(f"Recipe.get_all 發生錯誤: {e}")
            return []

    @staticmethod
    def get_by_id(recipe_id):
        """
        取得單筆食譜記錄
        :param recipe_id: 食譜 ID
        :return: 單筆食譜 (sqlite3.Row 物件) 或 None
        """
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
        except sqlite3.Error as e:
            print(f"Recipe.get_by_id 發生錯誤: {e}")
            return None

    @staticmethod
    def update(recipe_id, data):
        """
        更新指定的食譜記錄
        :param recipe_id: 食譜 ID
        :param data: dict 包含要更新的欄位
        :return: 成功回傳 True，失敗回傳 False
        """
        try:
            with get_db_connection() as conn:
                conn.execute('''
                    UPDATE recipes
                    SET title = ?, ingredients = ?, instructions = ?, notes = ?, 
                        source_url = ?, cooking_time = ?, category_id = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (
                    data.get('title'), data.get('ingredients'), data.get('instructions'), 
                    data.get('notes'), data.get('source_url'), data.get('cooking_time'), 
                    data.get('category_id'), recipe_id
                ))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Recipe.update 發生錯誤: {e}")
            return False

    @staticmethod
    def delete(recipe_id):
        """
        刪除指定的食譜記錄
        :param recipe_id: 食譜 ID
        :return: 成功回傳 True，失敗回傳 False
        """
        try:
            with get_db_connection() as conn:
                conn.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Recipe.delete 發生錯誤: {e}")
            return False
