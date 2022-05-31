# -*- coding: utf-8 -*-

from dataclasses import field
from odoo import models, fields, api
import random
import array
import base64

class reinos(models.Model):
    _name = 'dodgladiator.reinos'
    _description = 'dodgladiator.reinos'

    player = fields.Many2one('res.partner' )

    name = fields.Char()
    comedor = fields.Integer(default="0")
    description = fields.Text()

    dodo = fields.One2many('dodgladiator.dodo', 'reino')


    reino1 = fields.One2many( 'dodgladiator.batalla', 'reino1')
    reino2 = fields.One2many( 'dodgladiator.batalla', 'reino2')



    def añadir_dodos(self):
        numMax = 25
        for record in self:
            record.comedor = record.comedor + numMax


class reino_wizard(models.TransientModel):
    _name = 'dodgladiator.reino_wizard'
    _description = 'dodgladiator.reino_wizard'

    name = fields.Char()
    state = fields.Selection([
        ('1', "Nombre reino"),
        ('2', "Informacion Reino"),
        ('3', "Añadir Dodos"),                                                                                                                          
      ], default='1')

    description = fields.Text()
    dodo1 = fields.Many2many('dodgladiator.dodo')

    def create_reino(self):

        if(len(self.name) == 0):
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': 'Selecciona un Nombre',
                    'type': 'danger',  # types: success,warning,danger,info
                    'sticky': False
                }
            }
        if( len(self.dodo1) == 0):
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': 'Selecciona el primer dodo',
                    'type': 'danger',  # types: success,warning,danger,info
                    'sticky': False
                }
            }

        
        reserva = self.env['dodgladiator.reinos'].create({
            'name': self.name,
            'description': self.description,
            'dodo': self.dodo1.ids
        })
        
        return {
            'name': 'Reserves',
            'view_type': 'form',
            'view_mode': 'form',   # Pot ser form, tree, kanban...
            'res_model': 'dodgladiator.reinos', # El model de destí
            'res_id': reserva.id,       # El id concret per obrir el form
        # 'view_id': self.ref('wizards.reserves_form') # Opcional si hi ha més d'una vista posible.
            'context': self._context,   # El context es pot ampliar per afegir opcions
            'type': 'ir.actions.act_window',
            'target': 'current',  # Si ho fem en current, canvia la finestra actual.
        }

    def next(self):
        
        if self.state == '1':
            if self.name != False:
                self.state = '2'
            else:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'message': 'Selecciona un Nombre',
                        'type': 'danger',  # types: success,warning,danger,info
                        'sticky': False
                    }
                }
        elif self.state == '2':
            self.state = '3'
            return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
            }
        
        elif self.state == '3':
            return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
            }

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

            