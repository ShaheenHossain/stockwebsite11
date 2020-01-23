# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.http import request
from datetime import datetime, timedelta, date
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from odoo.tools.float_utils import float_round

class ProductProduct(models.Model):
    _inherit = 'product.product'

    cart_qty = fields.Integer(compute='_compute_cart_qty')
    old_lot = fields.Datetime(string="Fecha y hora del control de calidad", compute='_compute_old_lot')

    def _compute_cart_qty(self):
        website = request and getattr(request, 'website', None)
        if not website:
            return
        cart = website.sale_get_order()
        for product in self:
            product.cart_qty = sum(cart.order_line.filtered(lambda p: p.product_id.id == product.id).mapped('product_uom_qty')) if cart else 0

    def _compute_old_lot(self):
        website = request and getattr(request, 'website', None)
        if not website:
            return

        location = request.env['ir.config_parameter'].sudo().get_param('website_warehouse_stock_ept.location_id')
        for product in self:
            lots = request.env['stock.quant'].sudo().search(
                [('location_id', 'child_of', int(location)), ('product_id', '=', product.id)])
            old_lot = date(2100, 12, 5).strftime(DATETIME_FORMAT)
            for lot in lots:
                if lot.life_date:
                    old_lot = min(old_lot, lot.life_date)
            if old_lot == date(2100, 12, 5).strftime(DATETIME_FORMAT):
                old_lot = False
            product.old_lot = old_lot

    def _compute_quantities(self):
        website = request and getattr(request, 'website', None)
        if not website:
            super(ProductProduct, self)._compute_quantities()
        else:

            res = self._compute_quantities_dict(self._context.get('lot_id'), self._context.get('owner_id'),
                                                self._context.get('package_id'), self._context.get('from_date'),
                                                self._context.get('to_date'))
            for template in self:
                rounding = template.uom_id.rounding
                template.qty_available = res[template.id]['qty_available']
                template.virtual_available = float_round(
                    res[template.id]['qty_available'] - res[template.id]['outgoing_qty'], rounding)
                template.incoming_qty = res[template.id]['incoming_qty']
                template.outgoing_qty = res[template.id]['outgoing_qty']
