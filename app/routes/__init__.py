from .recipe_routes import recipe_bp
from .category_routes import category_bp
from .collection_routes import collection_bp

def register_routes(app):
    """註冊所有的 Blueprints 到 Flask app 中"""
    app.register_blueprint(recipe_bp)
    app.register_blueprint(category_bp, url_prefix='/categories')
    app.register_blueprint(collection_bp, url_prefix='/collections')
