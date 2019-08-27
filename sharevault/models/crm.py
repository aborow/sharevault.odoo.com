# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
#from odoo.exceptions import ValidationError

#import logging
#_logger = logging.getLogger(__name__)

class Lead(models.Model):
    _inherit = 'crm.lead'

    sharevault_id = fields.Many2one('sharevault.sharevault','ShareVault')


    """
    lead_id

    crm.lead
    	> sharevault_id


    add smart button on ther contacts (same record and dependents)
    list
    """
