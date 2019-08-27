# -*- coding: utf-8 -*-
{
    'name': 'SIC - Standard Industrial Classification',
	'version': '1.0',
	'category': 'Extra Tools',
    'summary': 'Standard Industrial Classification management',
	'description': """
This module creates a field to enter the 'Standard Industrial Classification'
code into the contac's record.

Data taken from https://www.naics.com

""",
    'author': 'Odooveloper',
    'website': 'http://www.odooveloper.com',
    'support': 'info@odooveloper.com',
    'depends': ['contacts'],
	'data': [
            'security/ir.model.access.csv',
            #'data/sic_code_data.xml',
            'views/partner_view.xml',
            'views/sic_code_view.xml',
            ],
    'installable': True,
    'active': False,
}
