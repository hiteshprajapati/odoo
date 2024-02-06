# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'view/estate_property_views.xml',
        'view/estate_menus.xml'
    ],
    'application': True,
    'license': 'LGPL-3',
}
