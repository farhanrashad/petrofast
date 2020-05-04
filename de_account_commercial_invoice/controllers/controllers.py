# -*- coding: utf-8 -*-
# from odoo import http


# class DeAccountCommercialInvoice(http.Controller):
#     @http.route('/de_account_commercial_invoice/de_account_commercial_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_account_commercial_invoice/de_account_commercial_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_account_commercial_invoice.listing', {
#             'root': '/de_account_commercial_invoice/de_account_commercial_invoice',
#             'objects': http.request.env['de_account_commercial_invoice.de_account_commercial_invoice'].search([]),
#         })

#     @http.route('/de_account_commercial_invoice/de_account_commercial_invoice/objects/<model("de_account_commercial_invoice.de_account_commercial_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_account_commercial_invoice.object', {
#             'object': obj
#         })
