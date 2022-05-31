# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
import random
import array
import base64

class ranking(models.Model):   
    _name = 'dodgladiator.ranking'
    _description = 'dodgladiator.ranking'

    player = fields.Many2many('res.partner' , compute = '_mejor_player')
    dodo = fields.Many2one('dodgladiator.dodo')

    def _mejor_player(self):
        for s in self:
            s.player = False
            MejorDodo = self.env['res.partner'].search([]).filtered(lambda player: len(player.reino) > 0).sorted(key=lambda player: player.dodo.ataque)
            print(MejorDodo)
            s.player = MejorDodo