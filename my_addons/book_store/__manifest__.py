{
    'name': "Book Store",
    'summary': "Book Store App",
    'author': 'Htet Myat',
    'category': 'bookstore',
    'data': [
        'security/ir.model.access.csv',
        'views/book_store_views.xml',
        'views/book_store_tree_view.xml',
        'views/book_store_search_view.xml',
        'reports/book_list_report.xml',
        # 'views/book_catalog_views.xml',
    ],
    'depends': [
        'reports',
    ]
}