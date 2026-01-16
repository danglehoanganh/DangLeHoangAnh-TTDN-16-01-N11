{
    'name': 'Quản lý Tài chính / Kế toán',
    'version': '1.0',
    'summary': 'Quản lý thu chi, sổ quỹ, nghiệp vụ kế toán cơ bản',
    'category': 'Accounting',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/finance_entry_view.xml',
    ],
    'application': True,
    'installable': True,
}
