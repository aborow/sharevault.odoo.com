# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
#from odoo.exceptions import ValidationError

#import logging
#_logger = logging.getLogger(__name__)

class Sharevault(models.Model):
    _name = 'sharevault.sharevault'
    _description = 'ShareVaults'

    name = fields.Char('Name', required=True)
    key = fields.Integer('Key')
    company_id = fields.Many2one('res.company', 'Company')
    type = fields.Selection([('sv','SV'),('sve','SVe')], 'Type')
    partner_id = fields.Many2one('res.partner', 'Owner')
    partner_id_title = fields.Char('Title', related='partner_id.function')
    partner_id_email = fields.Char('Email', related='partner_id.email')
    partner_id_phone = fields.Char('Phone', related='partner_id.phone')
    date_creation = fields.Date('Creation')
    date_expiration = fields.Date('Expiration')
    date_last_upload = fields.Date('Last upload')
    date_last_download = fields.Date('Last download')
    date_last_login = fields.Date('Last login')
    quota_pages = fields.Integer('Quota: pages')
    quota_users = fields.Integer('Quota: users')
    quota_mb = fields.Integer('Quota: MB')
    util_pages = fields.Integer('Utilized: pages')
    util_users = fields.Integer('Utilized: users')
    util_mb = fields.Integer('Utilized: MB')
    total_logins = fields.Integer('Total: logins')
    total_tags = fields.Integer('Total: tags')
    total_tag_value = fields.Integer('Total: tag value')
    total_groups = fields.Integer('Total: groups')
    uncounted_filesize_mb = fields.Integer('Uncounted filesize (MB)')
    locked = fields.Boolean('Locked')
    published_last_30_days_mb = fields.Integer('Published in the last 30 days')
    lead_id = fields.Many2one('crm.lead', 'Opportunity')
