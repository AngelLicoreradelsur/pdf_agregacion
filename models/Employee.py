# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class pdf_agregacion(models.Model):
#     _name = 'pdf_agregacion.pdf_agregacion'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Employee(models.Model):
        _name = 'hr.employee'
        _inherit = 'hr.employee'
        curriculum =  fields.Binary(string='Inserte Curriculum')
        num_social = fields.Char(size = 11, string = 'Número de seguro social')