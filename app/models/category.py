import sqlite3
from app.models.db import get_db_connection

class Category:
    @staticmethod
    def create(data):
        """
        新增一筆分類記錄
        :param data: dict 包含 name
        :return: 新增的記錄 ID 或 None
        """
        try:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO categories (name) VALUES (?)', (data.get('name'),))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Category.create 發生錯誤: {e}")
            return None

    @staticmethod
    def get_all():
        """
        取得所有分類記錄
        :return: 分類列表
        """
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM categories ORDER BY name').fetchall()
        except sqlite3.Error as e:
            print(f"Category.get_all 發生錯誤: {e}")
            return []

    @staticmethod
    def get_by_id(category_id):
        """
        取得單筆分類記錄
        :param category_id: 分類 ID
        :return: 單筆分類 或 None
        """
        try:
            with get_db_connection() as conn:
                return conn.execute('SELECT * FROM categories WHERE id = ?', (category_id,)).fetchone()
        except sqlite3.Error as e:
            print(f"Category.get_by_id 發生錯誤: {e}")
            return None

    @staticmethod
    def update(category_id, data):
        """
        更新指定的分類記錄
        :param category_id: 分類 ID
        :param data: dict 包含 name
        :return: 成功回傳 True，失敗回傳 False
        """
        try:
            with get_db_connection() as conn:
                conn.execute('UPDATE categories SET name = ? WHERE id = ?', (data.get('name'), category_id))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Category.update 發生錯誤: {e}")
            return False

    @staticmethod
    def delete(category_id):
        """
        刪除指定的分類記錄
        :param category_id: 分類 ID
        :return: 成功回傳 True，失敗回傳 False
        """
        try:
            with get_db_connection() as conn:
                conn.execute('DELETE FROM categories WHERE id = ?', (category_id,))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Category.delete 發生錯誤: {e}")
            return False
