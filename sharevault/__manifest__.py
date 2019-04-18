# -*- coding: utf-8 -*-
{
    'name': 'ShareVault',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Wibtec',
    'website': 'www.wibtec.com',
    'summary': 'Setup for ShareVault',
    'description': """

- ShareVault data model

""",
    'depends': [
                'crm',
                'auditlog',
                'helpdesk',
                'sale_management',
                'account'
                ],
    'data': [
            'security/groups_data.xml',
            'security/ir.model.access.csv',
            'data/auditlog_data.xml',
            'views/sharevault_view.xml',
            'views/res_partner_view.xml',
            ],
    'installable': True,
    'auto_install': False,
}
