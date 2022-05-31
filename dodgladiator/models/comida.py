# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api
from datetime import datetime, timedelta
import random
import array
import base64


class comida(models.Model):
    _name = 'dodgladiator.comida'
    _descripcion = 'dodgladiator.comida'

    """ player = fields.Many2one('res.partner') """


    name = fields.Char(default='Comida')


    def _calcular_curacion_comida(self):
        valor_comida = random.randrange(50,83)
        return valor_comida

    curacion = fields.Integer(default=_calcular_curacion_comida, readonly = True)


    def _get_imagenes_comida(self):
            imagenescomida = random.choice(self.env['dodgladiator.imagenescomida'].search([]).ids)
            #imagenescomida = 0
            print(imagenescomida)
            return imagenescomida
        
    image = fields.Many2one('dodgladiator.imagenescomida', default=_get_imagenes_comida)
    image_comida = fields.Image(related='image.image', max_width=50,
                               max_height=50)

    player = fields.Many2one('res.partner', 'comida')


    @api.model
    def crear_comida(self):
        self.create({'name': 'Comida', 'curacion': self._calcular_curacion_comida })


    
    
        
