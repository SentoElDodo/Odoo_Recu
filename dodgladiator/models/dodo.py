# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
import random
import array
import base64

class dodo(models.Model):   
    _name = 'dodgladiator.dodo'
    _description = 'dodgladiator.dodo'



    def _value_nombre_dodo(self):
            nombres = ['Sevas','Manu','Javioso','Vicente','Fran','Manolo','Juaquin','Mireia','Lujan','Carles','Pancracio','Eric','Pepe', 'Luis', 'Antonio', 'Fernando','Andres','Enrique', 'Edgar', 'Paco', 'Pablo', 'Carlos', 'Maria', 'Lucia', 'Ana', 'Silvia', 'Carol', 'Sento', 'Rafa', 'Fran', 'Ignacio', 'Alex', 'Tomas', 'Alba']
            numdenombres = len(nombres);
            numaleatorio = random.randrange(numdenombres)
            name = nombres[numaleatorio]
            return name

    name = fields.Char(default=_value_nombre_dodo)
    _sql_constraints = [ ('name_uniq','unique(name)','No se puede repetir el nombre')] 

    name_fallecido = fields.Many2many('dodgladiator.dodo_fallecido', 'name')

    def _get_imagenes_dodo(self):
            imagenesdodos = random.choice(self.env['dodgladiator.imagenesdodos'].search([]).mapped(lambda t: t.id))
            print(imagenesdodos)
            return imagenesdodos
    
    image = fields.Many2one('dodgladiator.imagenesdodos', default=_get_imagenes_dodo)     
    image_dodo = fields.Image(related='image.image', max_width=200,
                               max_height=200)


    def _value_salud(self):
            salud = random.randrange(112,131)
            return salud

    salud = fields.Integer(default=_value_salud, readonly = True)
    



    def _value_ataque(self):
            ataque = random.randrange(15,37)
            return ataque

    ataque = fields.Integer(default=_value_ataque, readonly = True)
    description = fields.Text()
    datacreacion = fields.Date(default= lambda self: fields.Date.today() , readonly = True)


    level = fields.Integer(default="1", readonly=True)

    start_date = fields.Datetime()


    dodo1 = fields.One2many( 'dodgladiator.batalla', 'dodo1' )
    dodo2 = fields.One2many( 'dodgladiator.batalla', 'dodo2' )

    

    def prueba_data_1(self):
        data=fields.Datetime.from_string(self.start_date)
        print(data)
        data=data+timedelta(hours=3)
        self.end_date=fields.Datetime.to_string(data)




     
      
      



        




    """ def porcentaje_mejora(self): """
        

    def subir_lvl(self):
            for record in self:
                record.level = record.level + 1
                porcentaje = random.randrange(3,5)
                record.ataque = record.ataque * porcentaje
                record.salud = record.salud * porcentaje
 

            

    reino = fields.Many2one('dodgladiator.reinos', ondelete='set null')



       



    