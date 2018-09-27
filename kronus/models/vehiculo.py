from openerp import fields, models

class kronus_embarques(models.Model):
	_name = 'kronus.embarques.vehiculos'

	name = fields.Char(string="Nombre del vehiculo", size=256, required=True)