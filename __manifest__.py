# -*- coding:utf-8 -*-
#
#
#  2022 Henderson Zambrano <zambranohender@gmail.com>.
#  
#
#

{
    "name": "Recepción",
    "version": "15.0.1",
    "author": "Henderson Zambrano <zambranohender@gmail.com>",
    "maintainer": 'Linux',
    "website": "https://github.com/hender88/recepcion",
    "license": "AGPL-3",
    "category": "Recepcion",
    "descripcion": """

Rececpción
=====================

Este modulo permite registrar los visitantes que ingresan a una Intitución:
    *

Creado
------------
* Henderson Zambrano Aguilera
""",

    "depends": ["base", "hr"],
    'external_dependencies': {},
    'data': [
        'security/security.xml',
        "security/ir.model.access.csv",
        "views/recepcion_view.xml",
       
    ],
    "demo": [],
    "test": [],
    'installable': True,
    'application': True,
}

