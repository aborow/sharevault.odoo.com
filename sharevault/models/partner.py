# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
#from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'

    sharevault_ids = fields.One2many('sharevault.sharevault', 'partner_id', 'ShareVaults')
    sharevault_ids_count = fields.Integer('ShareVault count', compute='get_sharevault_count')

    @api.multi
    def get_sharevault_count(self):
        self.ensure_one()
        self.sharevault_ids_count = len(self.sharevault_ids)


    auditlog_ids_count = fields.Integer('Auditlog count', compute='get_auditlog_count')

    @api.multi
    def get_auditlog_count(self):
        self.ensure_one()
        AuditLog = self.env['auditlog.log']
        model_id = self.env['ir.model'].search([('model','=',self._name)])
        self.auditlog_ids_count = AuditLog.search_count([
                                                        ('model_id','=',model_id.id),
                                                        ('res_id','=',self.id)
                                                        ])

    @api.multi
    def call_auditlog(self):
        self.ensure_one()
        action = self.env.ref('auditlog.action_auditlog_log_tree').read()[0]
        model_id = self.env['ir.model'].search([('model','=',self._name)])
        action.update({
                        'target': 'current',
                        'context': {
                                    'search_default_res_id': self.id,
                                    'search_default_model_id': model_id.id
                                    }
                        })
        return action
