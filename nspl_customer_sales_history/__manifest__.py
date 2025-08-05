{
    'name': 'Customer Sales History',
    'version': '17.0',
    'summary': """View customer sales history from Contacts or Sale Orders""",
    'description': """
    This module adds a smart button on Contacts and Sale Orders to quickly view the complete sales history of that customer.

    ✔ View customer's full sales history directly  
    ✔ Access from both Contact and Sales Order views  
    ✔ Enables better customer insights and decision making  
    ✔ Includes smart filter for commercial partners and child contacts  
    ✔ Respects user access rights for sales visibility  
    ✔ Lightweight, intuitive, and user-friendly design  

    Ideal for sales teams who need quick access to customer order history during negotiations or follow-ups.
        """,
    'category': 'Sales',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'contributors': ['Khanak Hathi'],
    'website': 'http://namahsoftech.com/',
    'license': 'OPL-1',
    'price': 19.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'depends': ['base', 'sale', 'sale_management', 'contacts'],
    'data': [
        'security/sales_history_security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
