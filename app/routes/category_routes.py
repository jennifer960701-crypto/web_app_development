from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.category import Category
from app.models.tag import Tag

category_bp = Blueprint('categories', __name__)

@category_bp.route('/', methods=['GET'])
def index():
    """分類與標籤列表頁面"""
    categories = Category.get_all()
    tags = Tag.get_all()
    return render_template('categories/index.html', categories=categories, tags=tags)

@category_bp.route('/', methods=['POST'])
def create():
    """建立分類"""
    name = request.form.get('name')
    if not name:
        flash('分類名稱不可為空', 'error')
    else:
        if Category.create({'name': name}):
            flash('分類新增成功', 'success')
        else:
            flash('新增失敗', 'error')
    return redirect(url_for('categories.index'))

@category_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """刪除分類"""
    if Category.delete(id):
        flash('分類已刪除', 'success')
    else:
        flash('刪除分類失敗', 'error')
    return redirect(url_for('categories.index'))

@category_bp.route('/tags', methods=['POST'])
def create_tag():
    """建立標籤"""
    name = request.form.get('name')
    if not name:
        flash('標籤名稱不可為空', 'error')
    else:
        if Tag.create({'name': name}):
            flash('標籤新增成功', 'success')
        else:
            flash('新增失敗', 'error')
    return redirect(url_for('categories.index'))

@category_bp.route('/tags/<int:id>/delete', methods=['POST'])
def delete_tag(id):
    """刪除標籤"""
    if Tag.delete(id):
        flash('標籤已刪除', 'success')
    else:
        flash('刪除標籤失敗', 'error')
    return redirect(url_for('categories.index'))
