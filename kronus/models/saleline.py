# -*- coding: utf-8 -*-
import time
import logging
_logger = logging.getLogger(__name__)
from openerp import models, fields, api

class kronus_sale_line(models.Model):
	_name = 'kronus.embarques.sale.line'
	_description = 'Linea de orden de venta'

	@api.depends('product_qty', 'price_unit', 'taxes_id')
	def _compute_amount(self):
		for line in self:
			taxes = line.taxes_id.compute_all(line.price_unit, line.cotizacion_id.currency_id, line.product_qty, product=line.product_id)
			line.update({
				'price_tax': taxes['total_included'] - taxes['total_excluded'],
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})

	@api.multi
	@api.onchange('product_id')
	def product_id_change(self):

		if not self.product_id:
			return {'domain': {'product_uom': []}}

		vals = {}
		product = self.product_id.with_context()
		name = product.name_get()[0][1]
		if product.description_sale:
			name += '\n' + product.description_sale
		vals['name'] = name
		vals['product_qty'] = 1.0
		if product.standard_price:
			vals['price_unit'] = product.standard_price
		if product.taxes_id:
			vals['taxes_id'] = product.taxes_id
		self.update(vals)
		self._compute_amount()
		return {'domain': []}

	name = fields.Text(string='Descripción', required=True)
	product_qty = fields.Float(string='Cantidad', digits=(16,2), required=True)
	
	taxes_id = fields.Many2many('account.tax', string='Impuestos')
	product_uom = fields.Many2one('product.uom', string='Product Unit of Measure')
	product_id = fields.Many2one('product.product', string='Producto', change_default=True, required=True, domain=[('sale_ok','=',True)])
	price_unit = fields.Float(string='Unit Price', required=True, digits=(16,2))

	price_subtotal = fields.Monetary(string='Subtotal', store=True)
	price_total = fields.Monetary(string='Total', store=True)
	price_tax = fields.Monetary(string='Impuesto', store=True)

	cotizacion1_id = fields.Many2one('kronus.embarques.cotizacion', string='Referencia de cotización', ondelete='cascade', required=True, index=True, copy=False)
	
	currency_id = fields.Many2one(related='cotizacion_id.currency_id', store=True, string='Moneda', readonly=True)
	state = fields.Selection(related="cotizacion_id.state", string="Estado")

	vehiculo = fields.Many2one('kronus.embarques.vehiculos', string="Vehiculo")
