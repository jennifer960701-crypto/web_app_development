from flask import Blueprint, render_template, request, redirect, url_for, flash
# from app.models.collection import Collection

collection_bp = Blueprint('collections', __name__)

@collection_bp.route('/', methods=['GET'])
def index():
    """
    收藏夾列表頁面
    輸出：渲染 collections/index.html，顯示使用者的所有清單
    """
    pass

@collection_bp.route('/', methods=['POST'])
def create():
    """
    建立收藏夾
    處理邏輯：接收表單資料，建立新清單
    輸出：redirect 到 /collections
    """
    pass

@collection_bp.route('/<int:id>', methods=['GET'])
def detail(id):
    """
    收藏夾詳情頁面
    輸入：URL 參數 id
    輸出：渲染 collections/detail.html，顯示該清單內的食譜
    """
    pass

@collection_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """
    刪除收藏夾
    處理邏輯：從 DB 刪除該清單
    輸出：redirect 到 /collections
    """
    pass
