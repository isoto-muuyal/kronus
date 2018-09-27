# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from openerp import models, fields, api, _
from openerp.exceptions import ValidationError
import logging
# class appprueba(models.Model):
#     _name = 'appprueba.appprueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class kronus_cotizacion(models.Model):
    """ The summary line for a class docstring should fit on one line.

    Fields:
      name (Char): Human readable name which will identify each record.

    """

    _name = 'kronus.embarques.cotizacion'
    _description = u'kronus_cotizacion'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(
        string='Name',
        required=True,
        readonly=True,
        index=True,
        default=None,
        help=False,
        size=50,
        translate=True
    )
    cliente = fields.Many2one(
    	'res.partner',
        string='Cliente',
        required=False,
        
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Divisa',
        required=True,
    )
    contacto = fields.Many2one(
    	'res.partner',
        string='Contacto',
        required=False,
        readonly=False,
        
    )
    tengo_embarcador = fields.Boolean(
        string='Tengo Embarcador',
        default= True
    )
    tengo_consignatario = fields.Boolean(
        string='Tengo Consignatario',
        default= True
    )
    consignatario = fields.Many2one(
   	    'res.partner',
   	    string='Consignatario',
   	)
    pais_origen = fields.Many2one(
   	    'res.country',
   	    string='Pais de Origen',
   	)
    estado_origen = fields.Many2one(
   	    'res.country.state',
   	    string='Estado de Origen',
   	)
    ciudad_origen = fields.Many2one(
   	    'res.country.state.city',
   	    string='Ciudad de Origen',
   	)
    pais_destino = fields.Many2one(
   	    'res.country',
   	    string='Pais Destino',
   	)
    estado_destino = fields.Many2one(
   	    'res.country.state',
   	    string='Estado Destino',
   	)
    ciudad_destino = fields.Many2one(
   	    'res.country.state.city',
   	    string='Ciudad destino',
   	)
    fecha_recoleccion = fields.Date(
   	    string='Fecha de Recolección Estimada'
   	)
    fecha_entrega = fields.Date(
   	    string='Fecha de Entrega Estimada'
   	)
    vehiculo = fields.Many2one(
   	    'kronus.embarques.vehiculo',
   	    string='Vehiculo',
   	)
    embarcador = fields.Many2one(
        'res.partner',
        string='Embarcador',
    )
    ruta = fields.Char(
   		compute='_compute_ruta',
   	  string='Ruta',
   	  readonly=True, 
   	   store=False,
   	)
    # sale_order_line = fields.One2many(
    #     'kronus.embarques.sale.line', 
    #     'cotizacion12_id', 
    #     string="Orden de ventas", 
    #     copy=True
    # )



    @api.depends('ciudad_origen','ciudad_destino')
    def _compute_ruta(self):
   		for cotizacion in self:
   			cotizacion.ruta = "%s%s%s" % (cotizacion.ciudad_origen.name or '', '-', cotizacion.ciudad_destino.name or '')

    
#falta completar el acomplamiento de los campos con las vistas
