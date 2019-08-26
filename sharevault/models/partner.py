# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

import logging
_logger = logging.getLogger(__name__)


class AccountStatus(models.Model):
    _name = 'res.partner.account_status'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class DataSource(models.Model):
    _name = 'res.partner.data_source'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class UpdateRequest(models.Model):
    _name = 'res.partner.data_update_request'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class LeadType(models.Model):
    _name = 'res.partner.lead_type'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class LifecycleStage(models.Model):
    _name = 'res.partner.lifecycle_stage'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class OrganizationType(models.Model):
    _name = 'res.partner.organization_type'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class Persona(models.Model):
    _name = 'res.partner.persona'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class Status(models.Model):
    _name = 'res.partner.status'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class Subindustry(models.Model):
    _name = 'res.partner.subindustry'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class ContactType(models.Model):
    _name = 'res.partner.contact_type'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class Matter(models.Model):
    _name = 'res.partner.matter'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class Tecnology(models.Model):
    _name = 'res.partner.tecnology'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class Confidential(models.Model):
    _name = 'res.partner.confidential'
    name = fields.Char('Name')
    active = fields.Boolean('Active')

class JobFunction(models.Model):
    _name = 'res.partner.job_function'
    name = fields.Char('Name')
    active = fields.Boolean('Active')



class Partner(models.Model):
    _inherit = 'res.partner'

    sharevault_ids = fields.One2many('sharevault.sharevault', 'partner_id', 'ShareVaults')
    sharevault_ids_count = fields.Integer('ShareVault count', compute='get_sharevault_count')
    auditlog_ids_count = fields.Integer('Auditlog count', compute='get_auditlog_count')


    ae_targeted = fields.Boolean('AE Targeted')
    annual_revenue = fields.Integer('Annual Revenue')
    european_union = fields.Boolean('Are you a citizen or resident of the European Union (EU)?')
    data_source_details = fields.Char('Data Source Details')
    domain = fields.Char('Domain')
    first_name = fields.Char('First Name', computed='get_first_last_name', store=True)
    last_name = fields.Char('Last Name', computed='get_first_last_name', store=True)
    imported_phone = fields.Char('Imported Phone')
    marketing_flag = fields.Boolean('Marketing Flag')
    marketing_note = fields.Char('Marketing note')
    salesforce_contact_id = fields.Char('Salesforce Contact ID')
    salesforce_lead_id = fields.Char('Salesforce Lead ID')
    shareVault_last_login_date = fields.Date('ShareVault Last Login Date')
    shareVault_subscription = fields.Boolean('ShareVault Subscription')
    shareVault_user = fields.Integer('ShareVault User ID')
    agree_data_collection = fields.Boolean('Agree with data collection')
    number_employees = fields.Integer('Number of Employees')

    account_status_id = fields.Many2one('res.partner.account_status', 'Account Status')
    data_source_id = fields.Many2one('res.partner.data_source', 'Data Source') #SKYPE
    data_update_request_id = fields.Many2one('res.partner.data_update_request', 'Data Update Request') #SKYPE
    lead_type_id = fields.Many2one('res.partner.lead_type', 'Lead Type') #SKYPE
    lifecycle_stage_id = fields.Many2one('res.partner.lifecycle_stage', 'Lifecycle stage') #SKYPE
    organization_type_id = fields.Many2one('res.partner.organization_type', 'Organization Type')
    persona_id = fields.Many2one('res.partner.persona', 'Persona', required=True)
    status_id = fields.Many2one('res.partner.status', 'Status') #SKYPE
    subindustry_id = fields.Many2one('res.partner.subindustry', 'Sub Industry') #SKYPE
    contact_type_id = fields.Many2one('res.partner.contact_type', 'Contact Type') #SKYPE
    matter_id = fields.Many2one('res.partner.matter', 'Subject matter most interested in?') #SKYPE
    tecnology_id = fields.Many2one('res.partner.tecnology', 'Technology solution used to share documents with 3rd parties?') #SKYPE
    confidential_id = fields.Many2one('res.partner.confidential', 'When will be sharing confidential information with a third party?') #SKYPE
    job_function = fields.Many2one('res.partner.job_function', 'Job Function') #SKYPE


    # new fields from XLS (select)
    job_level = fields.Selection([
                                ('CLEVEL','CLEVEL'),
                                ('Dir+','Dir+'),
                                ('IndContributor','IndContributor'),
                                ('Mgr+','Mgr+'),
                                ('Other','Other'),
                                ('VP+','VP+')
                                ], 'Job Level')

    sharevault_activated_user = fields.Selection([('null','null')], 'ShareVault Activated User')
    sharevault_admin = fields.Selection([('null','null')], 'ShareVault Admin')
    sharevault_domain = fields.Selection([('null','null')], 'ShareVault Domain')
    sharevault_email_subscription = fields.Selection([('null','null')], 'ShareVault Email Subscription')
    shareVault_publisher = fields.Selection([('null','null')], 'ShareVault Publisher')


    fax = fields.Char('Fax')
    fax_opt_out = fields.Boolean('Fax Opt Out')


    @api.onchange('name')
    @api.depends('name')
    @api.multi
    def get_first_last_name(self):
        first_name = ''
        last_name = ''
        if self.company_type == 'person':
            if self.name:
                aux = self.name.split(' ')
                _logger.info(aux)
                first_name = aux[0]
                _logger.info(first_name)
                if len(aux)>1:
                    last_name = aux[-1]
        self.first_name = first_name
        self.last_name = last_name

    @api.multi
    def get_sharevault_count(self):
        self.ensure_one()
        self.sharevault_ids_count = len(self.sharevault_ids)

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


    def _get_name(self):
        """ Utility method to allow name_get to be overrided without re-browse the partner """
        partner = self
        name = partner.name or ''

        if partner.first_name and partner.last_name:
            name = partner.first_name + ' ' + partner.last_name

        if partner.company_name or partner.parent_id:
            if not name and partner.type in ['invoice', 'delivery', 'other']:
                name = dict(self.fields_get(['type'])['type']['selection'])[partner.type]
            if not partner.is_company:
                name = "%s, %s" % (partner.commercial_company_name or partner.parent_id.name, name)
        if self._context.get('show_address_only'):
            name = partner._display_address(without_company=True)
        if self._context.get('show_address'):
            name = name + "\n" + partner._display_address(without_company=True)
        name = name.replace('\n\n', '\n')
        name = name.replace('\n\n', '\n')
        if self._context.get('address_inline'):
            name = name.replace('\n', ', ')
        if self._context.get('show_email') and partner.email:
            name = "%s <%s>" % (name, partner.email)
        if self._context.get('html_format'):
            name = name.replace('\n', '<br/>')
        if self._context.get('show_vat') and partner.vat:
            name = "%s ‒ %s" % (name, partner.vat)
        return name
