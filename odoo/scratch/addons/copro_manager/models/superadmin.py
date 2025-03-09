# /home/siisi/super/odoo/scratch/addons/copro_manager/models/superadmin.py

import secrets
import string
from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    image = fields.Binary(string="Image", attachment=True)

    # To track created residences
    created_residences = fields.One2many(
        'copro.residence',
        'created_by',
        string='Created Residences'
    )


class SuperAdmin(models.Model):
    _name = 'copro.superadmin'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Optional: For Odoo chatter
    _description = 'Super Administrator'

    image = fields.Binary(string="Image", attachment=True)
    name = fields.Char(string="Nom", required=True)
    email = fields.Char(string="Email", required=True, unique=True)
    phone = fields.Char(string="Téléphone")
    password = fields.Char(string="Password")
    login = fields.Char(string="Login", compute="_compute_login", store=True)
    groups_id = fields.Many2many('res.groups', string="Groups")

    syndic_ids = fields.One2many('copro.syndic', 'superadmin_id', string="Syndics Gérés")
    user_id = fields.Many2one('res.users', string="Utilisateur", ondelete='set null')

    residence_ids = fields.Many2many(
        'copro.residence',
        relation='residence_superadmin_rel',
        column1='superadmin_id',
        column2='residence_id',
        string='Supervised Residences'
    )

    @api.depends('user_id')
    def _compute_login(self):
        for record in self:
            record.login = record.user_id.login if record.user_id else ''

    @api.model
    def create(self, vals):
        # Ensure no conflicting user types before assigning the group
        #superadmin_group = self.env.ref('copro_manager.group_superadmin')
        
        if superadmin_group:
            user_vals = {
                'name': vals.get('name'),
                'login': vals.get('email'),
                'email': vals.get('email'),
                'password': 'siisi321',
                'groups_id': [(6, 0, [
                    self.env.ref('base.group_user').id,
                    self.env.ref('copro_manager.group_superadmin').id,
                ])],
            }
            
            user = self.env['res.users'].sudo().create(user_vals)
            vals['user_id'] = user.id
        
        return super(SuperAdmin, self).create(vals)
