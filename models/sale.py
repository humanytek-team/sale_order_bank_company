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

from openerp import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"    

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):

        super(SaleOrder, self).onchange_partner_id()

        values = dict()
        if self.partner_id.partner_bank_company_id:
            values['partner_bank_company_id'] = \
                self.partner_id.partner_bank_company_id.id
        self.update(values)

    partner_bank_company_id = fields.Many2one(
        'res.partner.bank',
        string='Bank account of payment',
        help='Allows to indicate the bank account of the company to which the '
            'customer probably makes the payments')
