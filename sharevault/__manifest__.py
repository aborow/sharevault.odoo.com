# -*- coding: utf-8 -*-
{
    'name': 'Sharevault',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Wibtec',
    'website': 'www.wibtec.com',
    'summary': 'Setup for Sharevault',
    'description': """

- Sharevault data model

""",
    'depends': [
                'crm',
                ],
    'data': [
            'security/groups_data.xml',
            'security/ir.model.access.csv',
            'views/sharevault_view.xml',
            'views/res_partner_view.xml',
            ],
    'installable': True,
    'auto_install': False,
}
