# 學生成績系統 - Django

這是一個以Django實作的學生成績系統專案。透過此專案，練習到Django的專案架構，以及各種相關功能的實作。

## 專案需求

- Django 4.2版本
- JavaScript ES6語法
- 使用Django內建的ORM來處理資料庫的操作與下SQL指令
- 模板化（template tags、template 繼承等）
- 實作Models
- 練習 JavaScript （DOM API 及 JQuery 兩個版本）
- AJAX
- 自建學生系統

## 學生系統功能

- R(read): 檢視學生成績 (All Students)、檢視科目 (Subjects)、排序 (Rank)、搜尋 (Search)
- login/register: 帳號管理功能，使用 Django 內建的 ​@login_required
- 分頁功能
- 使用 jQuery 的 Scroll 功能搭配 AJAX 實作向下拉自動載入
- 使用 command line 指令來自動新增學生資料
- C (create Student): 實作新增學生功能，用 Django 的 Form 實作
- 防呆功能（使用 Form 的 ValidationError）
- 將防呆做在 models 內: model 的 Validator 使用 Regular Expression（電話）
- 防呆錯誤訊息使用 ​Django message
- admin管理
- 使用 JavaScript / jQuery 的防呆功能
- AJAX排序
- 使用 htmx 功能
- 使用autocomplete 配合 AJAX 完成搜尋功能

## 參考資源

- [Django教學文件](https://docs.djangoproject.com/en/4.0/)
- [Mozilla Django教學](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)