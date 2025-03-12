# /home/siisi/super/odoo/scratch/addons/copro_manager/models/syndic.py

from odoo import models, fields, api


class Syndic(models.Model):
    _name = 'copro.syndic'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Optional: For Odoo chatter
    _description = 'Syndic'

    name = fields.Char(string="Nom du Syndic", required=True)
    email = fields.Char(string="Email", unique=True)
    phone = fields.Char(string="Téléphone")
    address = fields.Text(string="Adresse")

    license_id = fields.Many2one('copro.license', string="License", ondelete='set null')
    user_id = fields.Many2one('res.users', string="User Account", ondelete='set null')

    residence_ids = fields.Many2many(
        'copro.residence',
        relation='residence_syndic_rel',
        column1='syndic_id',
        column2='residence_id',
        string='Managed Residences'
    )

    @api.model
    def create(self, vals):
        if vals.get('email'):
            user_vals = {
                'name': vals.get('name'),
                'login': vals.get('email'),
                'email': vals.get('email'),
                'password': 'siisi321',
                # Assign both the base internal user group and the syndic group
                'groups_id': [(6, 0, [
                    self.env.ref('base.group_user').id,
                    self.env.ref('copro_manager.group_syndic').id
                ])],
            }
            user = self.env['res.users'].sudo().create(user_vals)
            vals['user_id'] = user.id
            
        return super(Syndic, self).create(vals)

    # Security rules to ensure syndics can only interact with their own data
    @api.model
    def _get_user_syndic_access(self):
        if self.env.user.has_group('copro_manager.group_syndic'):
            return [('syndic_id', '=', self.env.user.syndic_id.id)]
        return []
