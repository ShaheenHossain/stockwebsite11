# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stocks By Location',
    'version': '11.0.0.6',
    'category': 'Warehouse',
    'sequence': 14,
    'price': '25',
    'currency': "EUR",
    'summary': 'This plugin helps to show stock balance of different location on product level.',
    'description': """
    -Stock Balance by Location
    -Stock Quantity by location
    -Location based stock
    -Display Product Quantity based on stock.
    -Warehouse stock based on location
    -Stock Quantity based on location
    -Stock by location
    -Stock qty by location
    -Stock location


-Stock Balance por ubicación - Stock de cantidad por ubicación -Ubicación basada en la ubicación -Display Cantidad de producto en stock. - Stock de almacén basado en la ubicación - Cantidad de material basado en la ubicación -Stock por ubicación - Cantidad de material por ubicación - Ubicación de stock



-Stock Balance par Lieu -Stock Quantité par lieu - Stock basé sur l'emplacement -Afficher la quantité du produit en fonction du stock. - Stock d'entrepôt basé sur l'emplacement -Stock Quantité basée sur le lieu -Stock par emplacement -Stock quantité par emplacement -Stock emplacement
""",
    'author': 'BrowseInfo',
    'website': 'http://www.browseinfo.in',
    'images': [],
    'depends': ['base','sale','sale_management','stock'],
    'data': [
        'views/product.xml',
        'security/ir.model.access.csv',
        'report/stock_by_location_report.xml',
        'report/stock_by_location_report_view.xml',
        'report/stock_by_location_temp_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'live_test_url' : 'https://www.youtube.com/watch?v=QfN8iSDmUyo&feature=youtu.be',
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
