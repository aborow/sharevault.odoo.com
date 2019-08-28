# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Partner(models.Model):
    _inherit = 'res.partner'

    sic_code = fields.Char('SIC Code')
