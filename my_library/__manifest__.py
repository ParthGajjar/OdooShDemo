# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """Long description""",  # You can also rst format
    'author': "Your name",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '12.0.2',
    'depends': ['base', 'web', 'contacts'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/templates.xml'
    ],
}
