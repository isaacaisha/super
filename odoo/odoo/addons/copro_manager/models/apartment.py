# /home/siisi/super/odoo/odoo/addons/copro_manager/models/apartment.py

from odoo import models, fields, api


class Apartment(models.Model):
    _name = 'copro.apartment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Apartment'

    name = fields.Char(string="Apartment Name", required=True)
    number = fields.Char(string="Apartment Number", required=True)
    floor = fields.Integer(string="Floor")
    residence_id = fields.Many2one('copro.residence', string="Residence", ondelete='cascade')

    # Relationships
    residence_ids = fields.Many2many(
        'copro.residence',
        relation='apartment_residence_rel',
        column1='supersyndic_id',
        column2='residence_id',
        string='Associated Residence'
    )
    superuser_ids = fields.Many2many(
        'res.users',
        string='Super Users',
        relation='apartment_superuser_rel',
        column1='residence_id',
        column2='user_id',
        tracking=True
    )
    supersyndic_ids = fields.Many2many(
        'copro.supersyndic', 
        string='Super Syndics',
        relation='apartment_supersyndic_rel',
        column1='residence_id',
        column2='supersyndic_id',
        tracking=True
    )
    syndic_ids = fields.Many2many(
        'copro.syndic', 
        string='Syndics',
        relation='apartment_syndic_rel',
        column1='residence_id',
        column2='syndic_id',
        tracking=True
    )
    coproprietaire_ids = fields.Many2many(
        'copro.coproprietaire', 
        string='Coproprietaires',
        relation='apartment_coproprietaire_rel',
        column1='residence_id',
        column2='coproprietaire_id',
        tracking=True
    )
    created_by = fields.Many2one(
        'res.users', 
        string='Created By', 
        default=lambda self: self.env.user,
        readonly=True,
        ondelete='set null'
    )
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    extra_data = fields.Json(string='Extra Data')
    