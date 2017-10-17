# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
#    Rubén Bravo <rubenred18@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': "Bank account for payments of customers in sale orders",
    'description': '''Adds field "Bank account of payments" in form view of
    customers and sale orders. Allows to indicate the bank account of the
    company to which the customer probably makes the payment.
    ''',
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'category': 'sale',
    'version': '1.0.2',
    'depends': ['sale'],
    'data': [
        'views/partner_view.xml',
        'views/sale_order_view.xml',
    ],
    'demo': [
    ],
}
