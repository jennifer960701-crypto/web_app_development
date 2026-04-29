from flask import Blueprint, render_template, request, redirect, url_for, flash
# from app.models.category import Category
# from app.models.tag import Tag

category_bp = Blueprint('categories', __name__)

@category_bp.route('/', methods=['GET'])
def index():
    """
    分類與標籤列表頁面
    輸出：渲染 categories/index.html，顯示現有分類與標籤，並提供新增表單
    """
    pass

@category_bp.route('/', methods=['POST'])
def create():
    """
    建立分類
    處理邏輯：接收表單資料，建立新分類
    輸出：redirect 到 /categories
    """
    pass

@category_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """
    刪除分類
    處理邏輯：從 DB 刪除該分類
    輸出：redirect 到 /categories
    """
    pass

# Tag 相關路由目前也放這裡管理比較方便
@category_bp.route('/tags', methods=['POST'])
def create_tag():
    """
    建立標籤
    處理邏輯：接收表單資料，建立新標籤
    輸出：redirect 到 /categories
    """
    pass

@category_bp.route('/tags/<int:id>/delete', methods=['POST'])
def delete_tag(id):
    """
    刪除標籤
    處理邏輯：從 DB 刪除該標籤
    輸出：redirect 到 /categories
    """
    pass
