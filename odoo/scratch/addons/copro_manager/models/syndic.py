# /home/siisi/super/odoo/scratch/addons/copro_manager/models/syndic.py

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Syndic(models.Model):
    _name = 'copro.syndic'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Syndic'

    # Existing fields
    name = fields.Char(string="Nom du Syndic", required=True)
    email = fields.Char(string="Email", unique=True)
    phone = fields.Char(string="Téléphone")
    address = fields.Text(string="Adresse")
    user_id = fields.Many2one('res.users', string="User Account", ondelete='set null')
    residence_ids = fields.Many2many(
        'copro.residence',
        relation='residence_syndic_rel',
        column1='syndic_id',
        column2='residence_id',
        string='Managed Residences'
    )

    # Fields for license creation
    license_type = fields.Selection([
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('pro', 'Pro'),
    ], string="License Type")
    license_start = fields.Date(string="License Start Date")
    license_end = fields.Date(string="License End Date")
    license_id = fields.Many2one('copro.license', string="License")

    @api.model
    def create(self, vals):
        # Extract license details from the vals dictionary
        license_type = vals.pop('license_type', None)
        license_start = vals.pop('license_start', None)
        license_end = vals.pop('license_end', None)
        existing_license_id = vals.get('license_id')

        # Validate license inputs: Check if both an existing license and new license details are provided
        new_license_details = any([license_type, license_start, license_end])
        if existing_license_id and new_license_details:
            raise ValidationError("Cannot set both an existing license and new license details.")
        if new_license_details and not all([license_type, license_start, license_end]):
            raise ValidationError("All license details (Type, Start, End) are required.")

        # Create user for syndic if email is provided
        if vals.get('email'):
            user_vals = {
                'name': vals.get('name'),
                'login': vals.get('email'),
                'email': vals.get('email'),
                'password': 'siisi321',  # Ensure to handle passwords securely
                'groups_id': [(6, 0, [
                    self.env.ref('base.group_user').id,
                    self.env.ref('copro_manager.group_syndic').id
                ])],
            }
            user = self.env['res.users'].sudo().create(user_vals)
            vals['user_id'] = user.id

        # Create syndic entry in the database
        syndic = super(Syndic, self).create(vals)

        # Create a new license if new license details were provided
        if new_license_details:
            license_vals = {
                'name': f"License for {syndic.name}",
                'license_type': license_type,
                'start_at': license_start,
                'end_at': license_end,
            }
            # Create a new license and associate it with the syndic
            license = self.env['copro.license'].create(license_vals)
            syndic.license_id = license.id

        return syndic
