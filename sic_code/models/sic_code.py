# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SIC_Division(models.Model):
    _name = 'sic_code.division'
    _description = 'Standard Industrial Classification (division)'
    _order = 'name ASC'

    name = fields.Char('Name')
    description = fields.Char('Industry Title')
    active = fields.Boolean('Active', default=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Division already exists !"),
    ]


class SIC_Group(models.Model):
    _name = 'sic_code.group'
    _description = 'Standard Industrial Classification (group)'
    _order = 'name ASC'

    name = fields.Char('Name')
    description = fields.Char('Industry Title')
    division_id = fields.Many2one('sic_code.division', 'Division', required=True)
    active = fields.Boolean('Active', default=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name, division_id)', "Group already exists !"),
    ]


class SIC_Code(models.Model):
    _name = 'sic_code.code'
    _description = 'Standard Industrial Classification (code)'
    _order = 'name ASC'

    name = fields.Char('Code', size=4, required=True, help='Four digit code')
    group_id = fields.Many2one('sic_code.group', 'Group')
    division_id = fields.Many2one('sic_code.division', 'Division',
                        related='group_id.division_id', store=True)
    description = fields.Char('Industry', size=100, required=True)
    active = fields.Boolean('Active', default=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name, group_id)', "Code already exists !"),
    ]


    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = [
                        '|', ('description', '=ilike', '%' + name + '%'),
                        ('name', operator, name)
                    ]
        codes = self.search(domain + args, limit=limit)
        return codes.name_get()

    @api.multi
    def name_get(self):
        result = []
        for s in self:
            result.append((s.id, "[%s] %s" % (s.name, s.description)))
        return result

    @api.multi
    @api.onchange('name')
    @api.constrains('name')
    def _check_code(self):
        self.ensure_one()
        msg_error=[]
        if self.name:
            try:
                test = int(self.name)
            except:
                msg_error.append(_('The code should be a number.'))

            if len(self.name)!=4:
                msg_error.append(_('The code should have four digits.'))

        if msg_error:
            raise ValidationError('\n'.join(msg_error))
