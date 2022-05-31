# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
import array
import base64



class dodgladiator(models.Model):
    _name = 'dodgladiator.dodgladiator'
    _description = 'dodgladiator.dodgladiator'

    name = fields.Char()
    value = fields.Integer()
    edad = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.edad = float(record.value) / 100

    

    ''' @api.model
    def action_ataque(self,records):
        for i in records:
            print(i) '''

class imagenesdodos(models.Model):
    _name = 'dodgladiator.imagenesdodos'
    _description = 'dodgladiator.imagenesdodos'

    image = fields.Image(max_width=200, max_height=200)


class imagenescomida(models.Model):
    _name = 'dodgladiator.imagenescomida'
    _description = 'dodgladiator.imagenescomida'

    image = fields.Image(max_width=50, max_height=50)









    
