# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api
import random
import array
import base64


class player(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_player = fields.Boolean(default = False)
    reino = fields.One2many('dodgladiator.reinos', 'player')


    

    dinero = fields.Integer(default="1", readonly=True)

    comida = fields.One2many('dodgladiator.comida', 'player')

    dodo_fallecido = fields.Many2many('dodgladiator.dodo' , compute='_dodos_fallecidos')

    
    player1 = fields.One2many('dodgladiator.batalla', 'player1')
    player2 = fields.One2many('dodgladiator.batalla', 'player2')

    dodo = fields.Many2one('dodgladiator.dodo', compute='_mejor_dodo' )
    


    def _mejor_dodo(self):
        for s in self:
            s.dodo = False
            dodos = s.reino.dodo.sorted(key=lambda dodo: dodo.ataque , reverse=True)
            print(dodos)
            s.dodo = dodos[0]



    def _dodos_fallecidos(self):
        for s in self:
            dodoF = self.env['dodgladiator.dodo'].search([ ( 'salud' ,'=', 0 ) ]).ids
            print(dodoF)
            s.dodo_fallecido = dodoF
                



    ''' @api.model
    def crear_dinero(self):
        for s in self.search([]):

            if(len(s.dodo) > 0):
                dinero = s.dinero + 15;
                print("D0")
                s.write({'dinero': dinero})
                print(dinero)

            if(len(s.dodo) > 5):
                dinero = s.dinero + 20;
                print("D1")
                s.write({'dinero': dinero})
                print(dinero)

            if(len(s.dodo) > 10):
                dinero = s.dinero + 25;
                print("D2")
                s.write({'dinero': dinero})
                print(dinero)

            if(len(s.dodo) > 15):
                dinero = s.dinero + 30;
                print("D3")
                s.write({'dinero': dinero})
                print(dinero) '''
            


    def create_survivor(self):
        for p in self:
            """ template = random.choice(self.env['negocity.character_template'].search([]).mapped(lambda t: t.id))
            city = random.choice(self.env['negocity.city'].search([]).mapped(lambda t: t.id))
            survivor = self.env['negocity.survivor'].create({'player': p.id, 'template': template, 'city': city})
            for i in range(0,random.randint(0,1)):
                survivor.assign_random_car() """
    
    def button_update_players_progress(self):
        for p in self:
            return 0;