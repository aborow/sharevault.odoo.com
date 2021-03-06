# -*- coding: utf-8 -*-
{
    'name': 'ShareVault',
    'version': '1.1',
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
                'account',
                #'sic_code'
                ],
    'data': [
            'security/groups_data.xml',
            'security/ir.model.access.csv',
            'data/auditlog_data.xml',
            #'data/generic_data.xml',
            'views/sharevault_view.xml',

            'views/partner_view.xml',
            'views/crm_view.xml',

            'views/templates.xml',
            ],
    'installable': True,
    'auto_install': False,
}
