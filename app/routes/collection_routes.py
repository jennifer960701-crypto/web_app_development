from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.collection import Collection, CollectionRecipe

collection_bp = Blueprint('collections', __name__)

@collection_bp.route('/', methods=['GET'])
def index():
    """收藏夾列表頁面"""
    collections = Collection.get_all()
    return render_template('collections/index.html', collections=collections)

@collection_bp.route('/', methods=['POST'])
def create():
    """建立收藏夾"""
    name = request.form.get('name')
    if not name:
        flash('收藏夾名稱不可為空', 'error')
    else:
        if Collection.create({'name': name, 'sort_order': 0}):
            flash('收藏夾新增成功', 'success')
        else:
            flash('新增失敗', 'error')
    return redirect(url_for('collections.index'))

@collection_bp.route('/<int:id>', methods=['GET'])
def detail(id):
    """收藏夾詳情頁面"""
    collection = Collection.get_by_id(id)
    if not collection:
        flash('找不到該收藏夾', 'error')
        return redirect(url_for('collections.index'))
    
    recipes = CollectionRecipe.get_recipes_in_collection(id)
    return render_template('collections/detail.html', collection=collection, recipes=recipes)

@collection_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """刪除收藏夾"""
    if Collection.delete(id):
        flash('收藏夾已刪除', 'success')
    else:
        flash('刪除失敗', 'error')
    return redirect(url_for('collections.index'))
