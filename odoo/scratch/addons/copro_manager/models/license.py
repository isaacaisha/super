# /home/siisi/super/odoo/scratch/addons/copro_manager/models/license.py

from odoo import models, fields, api
from odoo.exceptions import AccessError


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
        # Allow any Odoo superuser to create a license
        if not self.env.user._is_superuser():
            raise AccessError("Only an Odoo superuser can assign a license.")
        return super(Licence, self).create(vals)
