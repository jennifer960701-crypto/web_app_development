import sqlite3
from app.models.db import get_db_connection

class Tag:
    @staticmethod
    def create(data):
        """
        新增一筆標籤記錄
        :param data: dict 包含 name
        :return: 新增的記錄 ID 或 None
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO tags (name) VALUES (?)', (data.get('name'),))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Tag.create 發生錯誤: {e}")
            return None

    @staticmethod
    def get_all():
        """
        取得所有標籤記錄
        :return: 標籤列表
        """
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM tags ORDER BY name').fetchall()
        except sqlite3.Error as e:
            print(f"Tag.get_all 發生錯誤: {e}")
            return []

    @staticmethod
    def get_by_id(tag_id):
        """
        取得單筆標籤記錄
        :param tag_id: 標籤 ID
        :return: 單筆標籤 或 None
        """
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM tags WHERE id = ?', (tag_id,)).fetchone()
        except sqlite3.Error as e:
            print(f"Tag.get_by_id 發生錯誤: {e}")
            return None

    @staticmethod
    def delete(tag_id):
        """
        刪除指定的標籤記錄
        :param tag_id: 標籤 ID
        :return: 成功回傳 True，失敗回傳 False
        """
        try:
            with get_db_connection() as conn:
                conn.execute('DELETE FROM tags WHERE id = ?', (tag_id,))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Tag.delete 發生錯誤: {e}")
            return False

class RecipeTag:
    @staticmethod
    def add_tag_to_recipe(recipe_id, tag_id):
        """加入標籤到食譜"""
        try:
            with get_db_connection() as conn:
                conn.execute('INSERT OR IGNORE INTO recipe_tags (recipe_id, tag_id) VALUES (?, ?)', (recipe_id, tag_id))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"RecipeTag.add_tag_to_recipe 發生錯誤: {e}")
            return False

    @staticmethod
    def remove_tag_from_recipe(recipe_id, tag_id):
        """從食譜移除標籤"""
        try:
            with get_db_connection() as conn:
                conn.execute('DELETE FROM recipe_tags WHERE recipe_id = ? AND tag_id = ?', (recipe_id, tag_id))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"RecipeTag.remove_tag_from_recipe 發生錯誤: {e}")
            return False

    @staticmethod
    def get_tags_for_recipe(recipe_id):
        """取得特定食譜的所有標籤"""
        try:
            with get_db_connection() as conn:
                return conn.execute('''
                    SELECT t.* FROM tags t
                    JOIN recipe_tags rt ON t.id = rt.tag_id
                    WHERE rt.recipe_id = ?
                ''', (recipe_id,)).fetchall()
        except sqlite3.Error as e:
            print(f"RecipeTag.get_tags_for_recipe 發生錯誤: {e}")
            return []
