from source.helpers.csv_helper import CSVHelper
from source.domain.supplier_priority import SupplierPriority
from source.services.supplier_priority_service import SupplierPriorityService
from source.domain.supplier_stock import SupplierStock
from source.services.supplier_stock_service import SupplierStockService
import csv
import os

def main():
  order_lists = CSVHelper.get_data_from_file("./source/Input_order_lists.csv")
  supplier_priority = CSVHelper.get_data_from_file("./source/Input_supplier_priority.csv")
  supplier_stock = CSVHelper.get_data_from_file("./source/Input_supplier_stock.csv")

  sps = SupplierPriorityService()
  for priority_raw in supplier_priority:
    sku = priority_raw['SKU']
    del priority_raw['SKU']
    short_cut = priority_raw['T\xc3\xaan vi\xe1\xba\xbft t\xe1\xba\xaft']
    del priority_raw['T\xc3\xaan vi\xe1\xba\xbft t\xe1\xba\xaft']

    priority_list = priority_raw
    priority = SupplierPriority(sku, priority_list, short_cut)
    sps.add_priority(sku, priority)

    sss = SupplierStockService(sps)

  for stock_raw in supplier_stock:
    sku = stock_raw['SKU']
    del stock_raw['SKU']

    suppliers = stock_raw
    stock = SupplierStock(sku, suppliers)
    sss.add_stock(sku, stock)

  sss.process_order_list(order_lists)
  failed = sss.get_orders_error()
  success = sss.get_orders_success()
  headers = failed[0].keys()

  with open('./result/error_order.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    for each in failed:
      values = each.values()
      writer.writerow(values)

  with open('./result/success_order.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    for each in success:
      values = each.values()
      writer.writerow(values)

if __name__ == '__main__':
  main()