from flask import Blueprint, render_template, request, redirect, url_for, flash
# 之後實作會引入 model，例如：from app.models.recipe import Recipe

recipe_bp = Blueprint('recipes', __name__)

@recipe_bp.route('/')
@recipe_bp.route('/recipes')
def index():
    """
    首頁 / 食譜列表
    輸入：可選的查詢參數 ?q=關鍵字 或 ?category=1
    輸出：渲染 recipes/index.html
    """
    pass

@recipe_bp.route('/recipes/new', methods=['GET'])
def new():
    """
    新增食譜頁面
    輸出：渲染 recipes/form.html，供使用者填寫資料
    """
    pass

@recipe_bp.route('/recipes', methods=['POST'])
def create():
    """
    建立食譜
    處理邏輯：接收表單資料，儲存至 DB
    輸出：成功後 redirect 到 /recipes/<id>
    """
    pass

@recipe_bp.route('/recipes/<int:id>', methods=['GET'])
def detail(id):
    """
    食譜詳情頁面
    輸入：URL 參數 id
    輸出：渲染 recipes/detail.html
    """
    pass

@recipe_bp.route('/recipes/<int:id>/edit', methods=['GET'])
def edit(id):
    """
    編輯食譜頁面
    輸入：URL 參數 id
    輸出：取得該筆食譜資料，渲染 recipes/form.html 進行編輯
    """
    pass

@recipe_bp.route('/recipes/<int:id>/update', methods=['POST'])
def update(id):
    """
    更新食譜
    處理邏輯：接收表單資料，更新 DB
    輸出：成功後 redirect 到 /recipes/<id>
    """
    pass

@recipe_bp.route('/recipes/<int:id>/delete', methods=['POST'])
def delete(id):
    """
    刪除食譜
    處理邏輯：從 DB 刪除對應 id 的食譜
    輸出：成功後 redirect 到 /recipes
    """
    pass
