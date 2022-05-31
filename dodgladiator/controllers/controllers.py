# -*- coding: utf-8 -*-
# from odoo import http


# class Dodgladiator(http.Controller):
#     @http.route('/dodgladiator/dodgladiator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dodgladiator/dodgladiator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dodgladiator.listing', {
#             'root': '/dodgladiator/dodgladiator',
#             'objects': http.request.env['dodgladiator.dodgladiator'].search([]),
#         })

#     @http.route('/dodgladiator/dodgladiator/objects/<model("dodgladiator.dodgladiator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dodgladiator.object', {
#             'object': obj
#         })
