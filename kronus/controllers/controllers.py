# -*- coding: utf-8 -*-
from odoo import http

# class KronusEmbarques(http.Controller):
#     @http.route('/kronus_embarques/kronus_embarques/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kronus_embarques/kronus_embarques/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kronus_embarques.listing', {
#             'root': '/kronus_embarques/kronus_embarques',
#             'objects': http.request.env['kronus_embarques.kronus_embarques'].search([]),
#         })

#     @http.route('/kronus_embarques/kronus_embarques/objects/<model("kronus_embarques.kronus_embarques"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kronus_embarques.object', {
#             'object': obj
#         })