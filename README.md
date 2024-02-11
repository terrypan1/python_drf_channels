# django
### init
- python -m venv venv
- venv\Scripts\activate 進入虛擬環境
- python -m pip install --upgrade pip
- pip freeze > requirements.txt
- pip install -r requirements.txt
- pip install django
- pip install python-dotenv 創建.env檔案
- pip install djangorestframework 
- https://www.django-rest-framework.org/#installation
- tree /f
### 1.django-admin startproject [項目名稱]
### 2.python manage.py startapp app01 (必須要在裡面創建)
- python ../../manage.py startapp users  在apps路徑下創建users
- python manage.py runserver 啟動server
### 3.python -m pip install django-redis

### 4.pip install djangorestframework 
- 註冊
    INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'rest_framework'
]
- drf配置 REST_FRAMEWORK = {"UNAUTHENTICATED_USER": None} 不然會抱錯
### 5.pip install django-cors-headers
### 6.urls.py 配置路由
### 7.app01/views.py 配置
- class drf用法
class InfoView(APIView):
    def get(self,request):
        return Response({'status':True,'message':'success'})
### 8.pip install ipython
- pip install django-extensions
INSTALLED_APPS = [
    'django_extensions',
]
- python manage.py shell_plus or python manage.py shell 都可以使用
### 9.pip install coreapi
- REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
- urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^docs/', include_docs_urls(title='My API title')),
]
### 10 pip install djangorestframework-simplejwt
- Access Token：
用途：用于访问受保护的 API 资源。
有效期：通常较短，例如您提到的 2 小时。
使用：在每次 API 请求的 HTTP 头部中附带这个 token，
通常是在 Authorization 头部，格式为 Bearer [access_token]。
- Refresh Token：
用途：用于在 access token 过期后获取一个新的 access token。
有效期：通常比 access token 长得多。
使用：当 access token 过期时，将 refresh token 发送到专门的 endpoint（例如 /api/token/refresh/），以获取一个新的 access token。

### 11.pip install celery 
- celery -A celery_tasks.main worker -l info (啟動) 
- celery -A celery_tasks.main worker -l info --pool=solo
- celery -A celery_tasks.main beat -l info

### 12.pip install drf-spectacular (pip install drf-yasg)
- https://drf-spectacular.readthedocs.io/en/latest/index.html
- python manage.py spectacular --file schema.yml
### 13.pip install black pip install flake8
- editor.defaultFormatter: null: 此設定表示將不會設置任何預設格式化程式。當進行程式碼格式化時，使用者需要手動選擇或設置所需的格式化程式。
- editor.formatOnSave: true: 啟用此設定將使 VS Code 在儲存文件時自動進行程式碼格式化。這可以確保程式碼的一致性和清晰度。
- python.formatting.provider: "black": 指定 Python 文件的格式化程式為 Black。Black 是一個用於 Python 的自動程式碼格式化工具，它可以根據其設定的標準自動調整程式碼的格式。
- python.formatting.blackArgs: ["--line-length", "119"]: 設定 Black 格式化程式的參數。在這個例子中，指定了一個參數 --line-length，並設置其值為 119，這表示 Black 將會將程式碼行的最大長度設置為 119 個字元。
- [python]: 此設定是針對 Python 文件的特定設定區段。
- editor.codeActionsOnSave: {"source.organizeImports": true}: 啟用此設定將使 VS Code 在儲存 Python 文件時自動組織導入語句。這將自動對文件中的導入進行排序和清理，以確保其一致性和可讀性。
### icons
- https://fonts.google.com/icons
### request對象(基於drf二次封裝)
- oop知識
- drf請求流程
### app(介紹)
- settings.py 項目配置        常常操作
- urls.py URL和函數的對應關係  常常操作
- asgi.py 接收網路請求 異步
- wsgi.py 接收網路請求 同步
- manage.py 項目的管理 啟動項目 創建app 數據管理
### 數據庫
- pip install mysqlclient
- pip install redis
- 創建帳號
create database meiduo_mall default charset=utf8;
create user meiduo identified by 'meiduo'; 
grant all on meiduo_mall.* to 'meiduo'@'%'; 
flush privileges;
--------------------------
- python manage.py makemigrations
- python manage.py migrate
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "app01"
] 要註冊app01
- 定義類型 https://docs.djangoproject.com/zh-hans/5.0/ref/models/fields/
### redis
- pip install django-redis

### 使用python manage.py shell
- from app01.models import TodoInfo
- TodoInfo.objects.create(name='Jack',done=True) 直接添加數據

### docker
- source venv/bin/activate

### 遇到導包失敗
- deactivate
- Remove-Item -Recurse -Force C:\Users\User\Desktop\flask\flask_model\venv
- python -m venv venv 
- 重來

### sudo apt update
### sudo apt install docker-compose
### docker-compose build 
### docker-compose up -d

### ngrok
### http://localhost:4040/ 裡面訪問 

### git 設定隱私 token 圖片教學

### 佈署上gcp後 ngrok 要打開防火牆 4040