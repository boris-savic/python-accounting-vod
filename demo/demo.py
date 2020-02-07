from datetime import datetime
from decimal import Decimal

from accounting_vod.core import VODExport, Document

export = VODExport(app_name='Olaii Backoffice', app_version='1.0', app_author='Olaii d.o.o.')


document_one = Document(document_type=Document.TYPE_TEMELJNICA,
                        market=Document.MARKET_HOME,
                        document_number='TEM-001-2020-01',
                        date_document=datetime.now().date(),
                        date_of_service=datetime.now().date(),
                        date_of_entry=datetime.now().date(),
                        date_issued_received=datetime.now().date(),
                        date_vat=None,
                        date_due=None,
                        description='Daily import example'
                        )

# Add partner to document one
partner = document_one.add_partner(code='00002', name='Company long name is placed here becase we need to demo d.o.o.', address='Address line 1', zip_code=1900, city='Ljubljana',
                                   country='SVN', tax_number='12345678', tax_payer=True)

document_one.add_journal_entry(entry_type='Ne_gre_v_knjigo', document_type='T', account_code='1091', cost_code='001', debit=Decimal('1050'),
                               currency_debit=Decimal('1050'), currency='EUR', partner=partner)
document_one.add_journal_entry(entry_type='Ne_gre_v_knjigo', document_type='T', account_code='2201', cost_code='001', credit=Decimal('1050'),
                               currency_credit=Decimal('1050'), currency='EUR', partner=partner)

export.add_document(document_one)

print(export.render_xml())
