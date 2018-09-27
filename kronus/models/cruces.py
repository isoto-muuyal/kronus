# -*- coding: utf-8 -*-

from openerp import models, fields, api

class kronus_cruces(models.Model):
	_name = 'kronus.embarques.cruces'

	name = fields.Char(string="Nombre", required=True)