# -*- coding: utf-8 -*-

from dataclasses import field
from email.policy import default
from functools import total_ordering
from odoo import models, fields, api 
from datetime import datetime, timedelta
import random
import array
import base64

class batalla(models.Model):
    _name = 'dodgladiator.batalla'
    _description = 'dodgladiator.batalla'

    name = fields.Char()
    _sql_constraints = [ ('name_uniq','unique(name)','No se puede repetir el nombre')]

    player1 = fields.Many2one('res.partner', required=True)
    player2 = fields.Many2one('res.partner', required=True) 

    reino1 = fields.Many2one( 'dodgladiator.reinos' , required=True)
    reino2 = fields.Many2one( 'dodgladiator.reinos' , required=True)

    dodo1 = fields.Many2one( 'dodgladiator.dodo' , required=True)
    dodo2 = fields.Many2one( 'dodgladiator.dodo' , required=True)

    dodo1_nombre = fields.Char(string='Nombre', store=True, related='dodo1.name')
    dodo1_image = fields.Image(string='Foto', store=True, related='dodo1.image_dodo')                      
    dodo1_salud = fields.Integer(string='Salud', store=True, related='dodo1.salud')
    dodo1_ataque = fields.Integer(string='Ataque', store=True, related='dodo1.ataque')

    dodo2_nombre = fields.Char(string='Nombre', store=True, related='dodo2.name')
    dodo2_image = fields.Image(string='Foto', store=True, related='dodo2.image_dodo')                      
    dodo2_salud = fields.Integer(string='Salud', store=True, related='dodo2.salud')
    dodo2_ataque = fields.Integer(string='Ataque', store=True, related='dodo2.ataque')


    start_date = fields.Datetime(default=lambda self: fields.Datetime.now())
    end_date = fields.Datetime(compute="_time_end")

    @api.depends('start_date')
    def _time_end(self):
        for record in self:
            data=fields.Datetime.from_string(record.start_date)
            data=data + timedelta(hours=1)
            record.end_date=fields.Datetime.to_string(data)


    time_battle = fields.Float(compute="_time_progres")

    ganador = fields.Many2one('res.partner',  readonly = True)

    batalla_finalizada = fields.Boolean(default=False)

    @api.depends('start_date')
    def _time_progres(self):
        for record in self:
            time_remaining = fields.Datetime.context_timestamp(self,record.end_date) - fields.Datetime.context_timestamp(self, datetime.now())
            time_remaining = time_remaining.total_seconds() / 60 / 60
            record.time_battle = (1 - time_remaining / 1) * 100

            if record.time_battle >= 100:
                record.time_battle = 100
                record.batalla_finalizada = True;
            else:
                record.time_battle = record.time_battle
                #record.end_date = Falses
    

    @api.model
    def calcular_batalla(self):
        batalla = self.filtered(lambda r: (r.time_battle < 1 and r.batalla_finalizada == True))
        ''' batalla = self.search([('time_battle','<',1) , ( 'batalla_finalizada', '=', True)]) '''

        print("adsfsashgjdhkdjshgfahdjhgfasgdhghgfsdfhjggfafsgdhjhgfadacsvdbytnbhdvthsvdst ystydsgsdfghsdfhsdfh")
                
        for s in batalla:
            if s.time_battle >= 100:

                ataque_dodo1 = s.dodo1_ataque / 100
                ataque_dodo2 = s.dodo2_ataque / 100

                vida_dodo1 = s.dodo1_salud / 100
                vida_dodo2 = s.dodo2_salud / 100

                total_dodo1 = ataque_dodo1 + vida_dodo1 / 2
                total_dodo2 = ataque_dodo2 + vida_dodo2 / 2


                print( ataque_dodo1, ataque_dodo2)

                if total_dodo1 > total_dodo2:
                    s.ganador = s.player1 
                if total_dodo1 < total_dodo2:
                    s.ganador = s.player2 

class batalla_wizard(models.TransientModel):
    _name = 'dodgladiator.batalla_wizard'
    _description = 'dodgladiator.batalla_wizard'

    name = fields.Char()
    state = fields.Selection([
        ('1', "Nombre batalla"),
        ('2', "Jugador 1"),
        ('3', "Jugador 2"),
                                                                                                                                     
      ], default='1')


    player1 = fields.Many2one('res.partner')
    player2 = fields.Many2one('res.partner') 

    reino1 = fields.Many2one( 'dodgladiator.reinos' )
    reino2 = fields.Many2one( 'dodgladiator.reinos' )

    dodo1 = fields.Many2one( 'dodgladiator.dodo' )
    dodo2 = fields.Many2one( 'dodgladiator.dodo' )



    def create_battle(self):

        if(len(self.player2) == 0):
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': 'Selecciona un Jugador',
                    'type': 'danger',  # types: success,warning,danger,info
                    'sticky': False
                }
            }
        if( len(self.reino2) == 0):
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': 'Selecciona un Reino',
                    'type': 'danger',  # types: success,warning,danger,info
                    'sticky': False
                }
            }
        if( len(self.dodo2) == 0):
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': 'Selecciona un Dodo',
                    'type': 'danger',  # types: success,warning,danger,info
                    'sticky': False
                }
            }

        if( len(self.player2) != 0 and len(self.reino2) != 0 and len(self.dodo2) != 0):
                
                
            if(self.player1 == self.player2):
                return {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'message': 'Son los mismos jugadores',
                            'type': 'danger',  # types: success,warning,danger,info
                            'sticky': False
                        }
                    }
            elif(self.reino1 == self.reino2):
                return {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'message': 'Son los mismos reinos',
                            'type': 'danger',  # types: success,warning,danger,info
                            'sticky': False
                        }
                    }
            elif(self.dodo1 == self.dodo2):
                return {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'message': 'Son los mismos dodos',
                            'type': 'danger',  # types: success,warning,danger,info
                            'sticky': False
                        }
                    }
            else:

                reserva = self.env['dodgladiator.batalla'].create({
                    'name': self.name,
                    'player1': self.player1.id,
                    'player2': self.player2.id,
                    'reino1': self.reino1.id,
                    'reino2': self.reino2.id,
                    'dodo1': self.dodo1.id,
                    'dodo2': self.dodo2.id
                })

                return {
                    'name': 'Reserves',
                    'view_type': 'form',
                    'view_mode': 'form',   # Pot ser form, tree, kanban...
                    'res_model': 'dodgladiator.batalla', # El model de destí
                    'res_id': reserva.id,       # El id concret per obrir el form
                # 'view_id': self.ref('wizards.reserves_form') # Opcional si hi ha més d'una vista posible.
                    'context': self._context,   # El context es pot ampliar per afegir opcions
                    'type': 'ir.actions.act_window',
                    'target': 'current',  # Si ho fem en current, canvia la finestra actual.
                }

    def next(self):
        if self.state == '1':
            print(self.name , "hasdsgfdsgasfjsdafjkfsdkljfgsjdgsdfjkgjksdfhgshdfgjksdfgshfdgjsfdjgds")
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

            if(len(self.player1) == 0):
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'message': 'Selecciona un Jugador',
                        'type': 'danger',  # types: success,warning,danger,info
                        'sticky': False
                    }
                }
            if( len(self.reino1) == 0):
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'message': 'Selecciona un Reino',
                        'type': 'danger',  # types: success,warning,danger,info
                        'sticky': False
                    }
                }
            if( len(self.dodo1) == 0):
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'message': 'Selecciona un Dodo',
                        'type': 'danger',  # types: success,warning,danger,info
                        'sticky': False
                    }
                }

            if( len(self.player1) != 0 and len(self.reino1) != 0 and len(self.dodo1) != 0):
                
                self.state = '3'
                

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
