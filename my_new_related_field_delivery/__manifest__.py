# -*- coding: utf-8 -*-
{
    'name': 'Custom Fields in sale Order Lines',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for custom fields in sale order lines',
    'sequence': '102',
    'license': 'AGPL-3',
    'author': 'AB',
    'maintainer': 'AB',
    'website': 'ab.com',
    'depends': ['base', 'stock', 'my_custom_fields'],
    'demo': [],
    'data': [
        
        'views/view_related_serialnumber.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}