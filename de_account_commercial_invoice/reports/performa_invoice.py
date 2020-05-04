from odoo.exceptions import UserError

from odoo import models, api, fields, _

class JobOrderreport(models.AbstractModel):
    _name= 'report.de_account_commercial_invoice.performa_invoice'
    _description = 'performa commercial invoice model'

    @api.model
    def _get_report_values(self, decides, data=None):
        docs=self.env['account.move'].browse(decides[0])
        invoices = self.env['account.move.line'].search([('move_id', '=', decides[0])])
        # if invoices:
        performa_invoice_list = []
        for i in invoices:
            vals = {
                'product_id': i.product_id,
                'name': i.name,
                'quantity': i.quantity,
                'price_unit': i.price_unit,
                'price_subtotal': i.price_subtotal
                }
            performa_invoice_list.append(vals)
        return{
              'doc_model': 'account.move',
              'data': data,
              'docs': docs,
              'performa_invoice_list': performa_invoice_list,
              }
        # else:
        #     print('test')
        #     raise UserError("There is not any line item in that invoice")



