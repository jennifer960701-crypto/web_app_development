from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.recipe import Recipe
from app.models.category import Category

recipe_bp = Blueprint('recipes', __name__)

@recipe_bp.route('/')
@recipe_bp.route('/recipes')
def index():
    """首頁 / 食譜列表"""
    recipes = Recipe.get_all()
    categories = Category.get_all()
    
    # 處理搜尋與篩選
    q = request.args.get('q', '').lower()
    cat_id = request.args.get('category')
    
    filtered_recipes = []
    for r in recipes:
        match = True
        if q:
            title = r['title'].lower() if r['title'] else ''
            ingredients = r['ingredients'].lower() if r['ingredients'] else ''
            if q not in title and q not in ingredients:
                match = False
        if cat_id and str(r['category_id']) != str(cat_id):
            match = False
            
        if match:
            filtered_recipes.append(r)
            
    return render_template('recipes/index.html', recipes=filtered_recipes, categories=categories)

@recipe_bp.route('/recipes/new', methods=['GET'])
def new():
    """新增食譜頁面"""
    categories = Category.get_all()
    return render_template('recipes/form.html', categories=categories, recipe=None)

@recipe_bp.route('/recipes', methods=['POST'])
def create():
    """建立食譜邏輯"""
    data = {
        'title': request.form.get('title'),
        'ingredients': request.form.get('ingredients'),
        'instructions': request.form.get('instructions'),
        'notes': request.form.get('notes'),
        'source_url': request.form.get('source_url'),
        'cooking_time': request.form.get('cooking_time') or None,
        'category_id': request.form.get('category_id') or None
    }
    
    if not data['title']:
        flash('標題為必填欄位', 'error')
        return redirect(url_for('recipes.new'))
        
    recipe_id = Recipe.create(data)
    if recipe_id:
        flash('食譜新增成功！', 'success')
        return redirect(url_for('recipes.detail', id=recipe_id))
    else:
        flash('新增失敗，請稍後再試。', 'error')
        return redirect(url_for('recipes.new'))

@recipe_bp.route('/recipes/<int:id>', methods=['GET'])
def detail(id):
    """食譜詳情頁面"""
    recipe = Recipe.get_by_id(id)
    if not recipe:
        flash('找不到該食譜', 'error')
        return redirect(url_for('recipes.index'))
        
    # 如果有對應分類，也可以一起撈出來，或是在 template 裡面處理
    # 這裡為了簡化，MVP 直接用 id
    return render_template('recipes/detail.html', recipe=recipe)

@recipe_bp.route('/recipes/<int:id>/edit', methods=['GET'])
def edit(id):
    """編輯食譜頁面"""
    recipe = Recipe.get_by_id(id)
    if not recipe:
        flash('找不到該食譜', 'error')
        return redirect(url_for('recipes.index'))
        
    categories = Category.get_all()
    return render_template('recipes/form.html', categories=categories, recipe=recipe)

@recipe_bp.route('/recipes/<int:id>/update', methods=['POST'])
def update(id):
    """更新食譜邏輯"""
    data = {
        'title': request.form.get('title'),
        'ingredients': request.form.get('ingredients'),
        'instructions': request.form.get('instructions'),
        'notes': request.form.get('notes'),
        'source_url': request.form.get('source_url'),
        'cooking_time': request.form.get('cooking_time') or None,
        'category_id': request.form.get('category_id') or None
    }
    
    if not data['title']:
        flash('標題為必填欄位', 'error')
        return redirect(url_for('recipes.edit', id=id))
        
    if Recipe.update(id, data):
        flash('食譜更新成功！', 'success')
    else:
        flash('更新失敗，請稍後再試。', 'error')
        
    return redirect(url_for('recipes.detail', id=id))

@recipe_bp.route('/recipes/<int:id>/delete', methods=['POST'])
def delete(id):
    """刪除食譜邏輯"""
    if Recipe.delete(id):
        flash('食譜已刪除', 'success')
    else:
        flash('刪除失敗', 'error')
    return redirect(url_for('recipes.index'))
