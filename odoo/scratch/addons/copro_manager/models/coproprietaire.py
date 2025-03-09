# /home/siisi/super/odoo/scratch/addons/copro_manager/models/coproprietaire.py

from odoo import models, fields, api


class Coproprietaire(models.Model):
    _name = 'copro.coproprietaire'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Optional: For Odoo chatter
    _description = 'Copropriétaire'

    name = fields.Char(string="Nom", required=True)
    email = fields.Char(string="Email", unique=True)
    phone = fields.Char(string="Téléphone")
    address = fields.Text(string="Adresse")

    syndic_id = fields.Many2one('copro.syndic', string="Syndic Associé", required=True)
    # Add this field to link to a user
    user_id = fields.Many2one('res.users', string="Utilisateur", readonly=True, ondelete='cascade')

    @api.model
    def create(self, vals):
        if vals.get('email'):
            user_vals = {
                'name': vals.get('name'),
                'login': vals.get('email'),
                'email': vals.get('email'),
                # Default password
                'password': 'siisi321',

                # Assign both the base internal user group and your custom group
                'groups_id': [(6, 0, [
                    self.env.ref('base.group_user').id,
                    self.env.ref('copro_manager.group_coproprietaire').id
                ])],
            }
            user = self.env['res.users'].sudo().create(user_vals)
            vals['user_id'] = user.id

        return super(Coproprietaire, self).create(vals)

    # Security rule to prevent modification
    @api.model
    def _get_user_coproprietaire_access(self):
        if self.env.user.has_group('copro_manager.group_coproprietaire'):
            return [('user_id', '=', self.env.user.id)]
        return []
