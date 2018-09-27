# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from openerp import fields, models, api, _
from openerp.exceptions import ValidationError, UserError
import logging

class kronus_embarques(models.Model):
    _name = 'kronus.embarques.embarque'

    cotizacion = fields.Char(string='Cotización', store=True)
    currency_id = fields.Many2one('res.currency', string="Divisa", required=True)
    solicitud = fields.Date(string="Fecha de solicitud", required=True)
    cliente = fields.Many2one('res.partner', string="Cliente", domain=[('customer','=',True)], copy=True, required=True)
    contacto = fields.Many2one('res.partner', string="Contacto", domain="[('parent_id','=', cliente)]", required=True, copy=True)
    embarcador = fields.Many2one('res.partner', string="Embarcador", domain=[('embarcador','=',True)], copy=True, required=True)
    contacto_embarcador = fields.Many2one('res.partner', string="Contacto del embarcador", domain="[('parent_id','=', embarcador)]", required=True, copy=True)
    consignatario = fields.Many2one('res.partner', string="Consignatario",domain=[('consignatario','=',True)], copy=True, required=True)
    contacto_consignatario = fields.Many2one('res.partner', string="Contacto del consignatario", domain="[('parent_id','=', consignatario)]", required=True, copy=True)
    agente_aduanal = fields.Many2one('res.partner', string="Agente aduanal", domain=[('agente','=',True)], copy=True,)
    cruce = fields.Many2one('kronus.embarques.cruces', string="Cruce", copy=True,)
    #internacional = fields.Boolean(default='_default_internacional', store=False, readonly=True)
    recoleccion_estimada = fields.Date(string="Fecha de recolección estimada", copy=False)
    entrega_estimada = fields.Date(string="Fecha de entrega estimada", copy=False)
    recoleccion_real = fields.Date(string="Fecha de recolección real", copy=False)
    entrega_real = fields.Date(string="Fecha de entrega real", copy=False)
    vehiculo = fields.Many2one('kronus.embarques.vehiculos', string="Vehiculo", copy=True)
    chofer = fields.Char(string="Chofer del vehiculo", size=256, copy=True)
    placas = fields.Char(string="Placas del vehiculo", size=256, copy=True)
    ruta = fields.Char(compute='_compute_ruta', string="Ruta", readonly=True, store=False)
    evidencias = fields.Many2many("ir.attachment", string="Evidencias", copy=False, ondelete='cascade')

    #Servicios Adicionales Fields
    prepagado = fields.Char(string="Prepagado", size=256, copy=True)
    por_cobrar = fields.Char(string="Por cobrar", size=256, copy=True)
    seguro = fields.Char(string="Seguro", size=256, copy=True)
    garantizado = fields.Char(string="Garantizado", size=256, copy=True)
    rampa = fields.Char(string="Rampa hidr.", size=256, copy=True)
    maniobras = fields.Char(string="Maniobras", size=256, copy=True)
    state = fields.Selection([
    	('draft', 'Pendiente'),
    	('transit', 'En transito'),
    	('done', 'Entregado'),
    	('cancel', 'Cancelado'),
    	], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

    name = fields.Char(string='Número de embarque', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.multi
    def _compute_ruta(self):
    	for embarque in self:
    		embarque.ruta = "%s%s%s" % (embarque.embarcador_city.name or '', '-', embarque.consignatario_city.name or '')

	"""

	@api.model
	def _default_internacional(self):
		if self.consignatario_city and self.embarcador_city:
			return  self.consignatario_city.country_id != self.embarcador_city.country_id
		else:
			return False
	
	@api.multi
	def action_comenzar(self):
		self.write({'state' : 'transit'})

	@api.multi
	def action_finalizar(self):
		if self.cliente.pruebas and not self.evidencias:
			raise UserError(_('Para finalizar el embarque se debe contar con al menos una evidencia'))

		if self.recoleccion_real and self.entrega_real:
			success, message = self.validate_invoice_customer()
			if not success:
				raise UserError(_(message))
			success, message = self.validate_invoice_proveedor()
			if not success:
				raise UserError(_(message))
			invoice = self._create_invoice_customer()
			self._facturar_proveedores()
			self.write({'state' : 'done'})
		else:
			raise UserError(_('La fecha de recolección real, entrega real y/o evidencias deben ser agregadas'))
"""

