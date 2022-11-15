# -*- coding: utf-8 -*-


from odoo import tools
from odoo import api, fields, models
from odoo.tools.translate import _
from datetime import datetime, date
import math
import time





class visitantes(models.Model):

    _name = "recepcion.visitantes"
    _description = "Visitantes"
 
     
    name = fields.Char(string='Nombres', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    id_cedula = fields.Integer(string="Cedula", required=True)
    description = fields.Text(string='Job Description')
    nota = fields.Text('Nota', size=260)
    visitas_id = fields.One2many('recepcion.visitas', 'visitante_id', string='Visitas')
    nacionalidad = fields.Selection([('Colombiano', 'CC-'), ('Extrangero', 'E-'), ('Pasaporte', 'P-')], 'Nacionalidad', required=True)
   

    _sql_constraints = [
        ('cedula_uniq', 'unique(id_cedula)', 'Esta Cedula ya se Encuentra Registrada en el Sistema!'),
    ]




class visitas(models.Model):
    _name = 'recepcion.visitas'
     
    def _default_fecha(self):
        
        return datetime.now()
    
   
         
    
    visitante_id = fields.Many2one('recepcion.visitantes', string='Visitante')
    name = fields.Datetime('Entrada: Fecha-Hora', default=_default_fecha)
    hora_salida = fields.Datetime('Hora de Salida')
    department_id = fields.Many2one('hr.department', string='Unidad Administrativa a Visitar')
 
