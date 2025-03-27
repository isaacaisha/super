# /home/siisi/super/odoo/scratch/addons/copro_manager/__manifest__.py

{
    'name': 'OCA CRM Manager',
    'version': '1.0',
    #'version': '16.0.1.0.0',
    #'version': '18.0.1.0.0',
    'category': 'Property Management, Accounting',
    'description': """
        This module enhances Odoo's accounting features by providing additional tools 
        for financial analysis and reporting. It includes advanced features to help 
        manage license, residence, syndicate, owner, provider and analyze financial data effectively.
    """,
    'summary': 'Extra tools and functionalities for financial management in accounting, Syndicate, Co-owner, Co-provider, ... .',
    'author': 'Requin Tibùron',
    #'website': 'http://copromanage.pro/web/login',
    'website': 'http://siisi.online/web/login',
    'depends': ['base', 'mail'],
    'data': [
        #'security/groups.xml',
        #'security/ir_rules.xml',
        #'security/ir.model.access.csv',
        #'views/menus.xml',
        #'views/apps_menu.xml',
        #'views/contact_views.xml',
        #'views/supersyndic_views.xml',
        #'views/syndic_views.xml',
        #'views/coproprietaire_views.xml',
        #'views/prestataire_views.xml',
        #'views/license_views.xml',
        #'views/residence_views.xml',
        #'views/apartment_views.xml',
        #'data/supersyndic_data.xml',
        #'data/syndic_data.xml',
        #'data/coproprietaire_data.xml',
        #'data/prestataire_data.xml',
        #'data/residence_data.xml',
        #'data/apartment_data.xml',
    ],
    'images': ['static/description/shark.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
