# 路由設計文件 - 食譜收藏夾系統

基於先前的架構與資料庫設計，本文件規劃了系統的所有網址路由、對應的處理邏輯與渲染的頁面模板。

## 1. 路由總覽表格

### 食譜相關 (Recipe Routes)

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 / 食譜列表 | GET | `/` 或 `/recipes` | `templates/recipes/index.html` | 顯示所有食譜，支援搜尋與篩選 |
| 新增食譜頁面 | GET | `/recipes/new` | `templates/recipes/form.html` | 顯示新增食譜表單 |
| 建立食譜 | POST | `/recipes` | — | 接收表單，存入 DB，重導向至列表或詳細頁 |
| 食譜詳情 | GET | `/recipes/<int:id>` | `templates/recipes/detail.html` | 顯示單筆食譜完整內容 |
| 編輯食譜頁面 | GET | `/recipes/<int:id>/edit` | `templates/recipes/form.html` | 顯示編輯表單（帶入原有資料） |
| 更新食譜 | POST | `/recipes/<int:id>/update` | — | 接收表單更新資料，重導向至詳細頁 |
| 刪除食譜 | POST | `/recipes/<int:id>/delete` | — | 刪除指定食譜，重導向至列表頁 |

### 分類與標籤 (Category & Tag Routes)

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 分類與標籤列表 | GET | `/categories` | `templates/categories/index.html` | 顯示所有分類與標籤 |
| 新增分類 | POST | `/categories` | — | 建立新分類，重導向至列表頁 |
| 刪除分類 | POST | `/categories/<int:id>/delete`| — | 刪除分類，重導向至列表頁 |
| 新增標籤 | POST | `/tags` | — | 建立新標籤，重導向至列表頁 |
| 刪除標籤 | POST | `/tags/<int:id>/delete` | — | 刪除標籤，重導向至列表頁 |

### 收藏夾管理 (Collection Routes)

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 收藏夾列表 | GET | `/collections` | `templates/collections/index.html`| 顯示使用者的收藏夾清單 |
| 新增收藏夾 | POST | `/collections` | — | 建立新收藏夾，重導向至列表頁 |
| 收藏夾詳情 | GET | `/collections/<int:id>` | `templates/collections/detail.html`| 顯示收藏夾內的食譜清單 |
| 刪除收藏夾 | POST | `/collections/<int:id>/delete`| — | 刪除收藏夾，重導向至列表頁 |

---

## 2. 每個路由的詳細說明

### 2.1 首頁 / 食譜列表 (`GET /`)
*   **輸入**：可選的查詢參數 `?q=關鍵字` 或 `?category=1`。
*   **處理邏輯**：從 Model 取得食譜資料；若有查詢參數則進行過濾。
*   **輸出**：渲染 `recipes/index.html`，傳遞食譜列表資料。
*   **錯誤處理**：無。

### 2.2 新增食譜 (`POST /recipes`)
*   **輸入**：表單欄位 (`title`, `ingredients`, `instructions`, `notes`, `source_url`, `cooking_time`, `category_id`, `tags_id`)。
*   **處理邏輯**：呼叫 `Recipe.create()` 寫入食譜，並呼叫 `RecipeTag.add_tag_to_recipe()` 寫入關聯標籤。
*   **輸出**：成功後 `redirect(url_for('recipes.detail', id=new_id))`。
*   **錯誤處理**：若 `title` 為空，回傳錯誤訊息並重新渲染 `recipes/form.html`。

### 2.3 刪除食譜 (`POST /recipes/<id>/delete`)
*   **輸入**：URL 參數 `id`。
*   **處理邏輯**：呼叫 `Recipe.delete(id)`，依賴資料庫的 Cascade Delete 移除關聯。
*   **輸出**：`redirect(url_for('recipes.index'))`。
*   **錯誤處理**：若查無該 ID，回傳 404 Not Found。

---

## 3. Jinja2 模板清單

所有的網頁將繼承共用的基礎版型 `base.html`：

1.  `templates/base.html`：**基礎版型**（包含 Navbar, Footer, 引入 CSS/JS）。
2.  `templates/recipes/index.html`：**首頁/列表頁**（繼承 base，顯示卡片列表與搜尋列）。
3.  `templates/recipes/detail.html`：**食譜詳細頁**（繼承 base，顯示內容與個人筆記）。
4.  `templates/recipes/form.html`：**新增/編輯共用表單**（繼承 base，依傳入資料決定是新增還是編輯模式）。
5.  `templates/categories/index.html`：**分類管理頁面**（繼承 base，顯示分類與標籤的清單及新增表單）。
6.  `templates/collections/index.html`：**收藏夾管理首頁**（繼承 base，顯示所有收藏夾）。
7.  `templates/collections/detail.html`：**單一收藏夾內容頁**（繼承 base，顯示該清單內的食譜）。

---

## 4. 路由骨架程式碼

路由骨架將分為三個 Blueprint，並建立於 `app/routes/` 目錄：
*   `recipe_routes.py`
*   `category_routes.py`
*   `collection_routes.py`
程式碼檔案已在專案中產出，僅包含路由定義與 Docstring。
