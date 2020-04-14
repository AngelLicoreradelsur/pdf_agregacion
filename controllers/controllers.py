# -*- coding: utf-8 -*-
from odoo import http

# class PdfAgregacion(http.Controller):
#     @http.route('/pdf_agregacion/pdf_agregacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pdf_agregacion/pdf_agregacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pdf_agregacion.listing', {
#             'root': '/pdf_agregacion/pdf_agregacion',
#             'objects': http.request.env['pdf_agregacion.pdf_agregacion'].search([]),
#         })

#     @http.route('/pdf_agregacion/pdf_agregacion/objects/<model("pdf_agregacion.pdf_agregacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pdf_agregacion.object', {
#             'object': obj
#         })