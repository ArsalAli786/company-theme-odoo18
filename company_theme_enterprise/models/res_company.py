from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    apps_menu_background = fields.Image(
        string="Apps Menu Background",
        max_width=2560,
        max_height=1440,
        attachment=True,
    )
