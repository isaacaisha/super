# /home/siisi/super/odoo/odoo/addons/copro_manager/models/license.py

from odoo import models, fields, api

class Licence(models.Model):
    _name = "copro.license"
    _description = "License"

    name = fields.Char(string="Nom de Licence", required=True)
    start_at = fields.Date(string="Début le:", required=True)
    end_at = fields.Date(string="expire le:", required=True)

    def get_syndic(self):
        Syndic = self.env["copro.syndic"]  # ✅ Lazy import inside a method
        return Syndic.search([])

    @api.model
    def create(self, vals):
        # Ensure only superadmins can assign licenses
        if self.env.user not in self.env.ref('copro_manager.group_superadmin').users:
            raise AccessError("Only superadmins can assign a license.")
        
        return super(Licence, self).create(vals)
