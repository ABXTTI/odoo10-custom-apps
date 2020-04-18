# -*- coding: utf-8 -*-
from odoo import models, fields
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    x_serialnumber = fields.Char('Serial Number')
