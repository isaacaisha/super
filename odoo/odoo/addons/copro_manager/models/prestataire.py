# /home/siisi/super/odoo/odoo/addons/copro_manager/models/prestataire.py

from odoo import models, fields, api


class Prestataire(models.Model):
    _name = "copro.prestataire"
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Optional: For Odoo chatter
    _description = "Prestataire"

    name = fields.Char(string="Nom", required=True)
    email = fields.Char(string="Email", required=True, unique=True)
    phone = fields.Char(string="Téléphone")
    address = fields.Text(string="Adresse")
    service_type = fields.Selection([
        ('plumber', 'Plomberie'),
        ('electrician', 'Électricité'),
        ('cleaning', 'Nettoyage'),
        ('security', 'Sécurité'),
        ('other', 'Autre'),
    ], string="Type de Service", required=True)

    supersyndic_id = fields.Many2one('copro.supersyndic', string="Super Syndic Responsable")
    syndic_id = fields.Many2one("copro.syndic", string="Syndic Responsable")
    user_id = fields.Many2one('res.users', string="Utilisateur", readonly=True, ondelete='cascade')

    @api.model
    def create(self, vals):
        if vals.get('email'):

            user_vals = {
                'name': vals.get('name'),
                'login': vals.get('email'),
                'email': vals.get('email'),
                'password': 'siisi321',
                # Assign both the base internal user group and your custom group
                'groups_id': [(6, 0, [
                    self.env.ref('base.group_user').id,
                    self.env.ref('copro_manager.group_prestataire').id
                ])],
            }
            user = self.env['res.users'].sudo().create(user_vals)
            vals['user_id'] = user.id

        # Create prestataire entry in the database
        prestataire = super(Prestataire, self).create(vals)
        return prestataire

    @api.model
    def _get_user_prestataire_access(self):
        """Restrict prestataire access to only their supersyndic & syndic."""
        if self.env.user.has_group('copro_manager.group_prestataire'):
            return [('superyndic_id.user_id', '=', self.env.user.id)]
        elif self.env.user.has_group('copro_manager.group_prestataire'):
            return [('syndic_id.user_id', '=', self.env.user.id)]
        return []

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        args += self._get_user_prestataire_access()
        return super(Prestataire, self).search(args, offset, limit, order, count)
