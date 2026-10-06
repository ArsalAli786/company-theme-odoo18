from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    company_primary_color = fields.Char(
        string='Company Theme Color',
    )