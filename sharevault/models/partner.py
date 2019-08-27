# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _


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
