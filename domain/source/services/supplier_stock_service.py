from source.domain.supplier_stock import SupplierStock
from .supplier_priority_service import SupplierPriorityService

class SupplierStockService:
  def __init__(self, priority_service):
    self.priority_service = priority_service
    self.stocks = {}
    self.orders_errors = []
    self.orders_success = []

  def add_stock(self, sku, stock):
    self.stocks[sku] = stock

  def process_order_list(self, order_list):
    orders_payed, order_not_payed = self._divide_order_list(order_list)

    for order in orders_payed:
      sku_code = order['Lineitem SKU']

      if not self.priority_service.have_sku(sku_code):
        self.orders_errors.append(order)
        continue
      priority = self.priority_service.get_priority(sku_code)
      self.process_order(order, priority)

    for order in order_not_payed:
      sku_code = order['Lineitem SKU']
      if not self.priority_service.have_sku(sku_code):
        self.orders_errors.append(order)
        continue
      priority = self.priority_service.get_priority(sku_code)
      self.process_order(order, priority)


  def process_order(self, order, priority):   
    sku = order['Lineitem SKU']
    quantity = int(order['Quantity'])
    stock = self.stocks[sku]
    order_supplier = priority.get_order_supplier()

    for supplier in order_supplier:
      # import pdb;pdb.set_trace()
      supplier_is_valid = stock.supplier_is_valid(supplier, quantity)
      if supplier_is_valid == True:
        stock.minus_supplier_quantity(supplier, quantity)
        self.orders_success.append(order)
      else:
        self.orders_errors.append(order)

  def _divide_order_list(self, order_list):
    orders_payed = []
    order_not_payed = []

    for order in order_list:
      if order['Order Status'] == 'SHIPPING':
        orders_payed.append(order)
      else:
        order_not_payed.append(order)

    return orders_payed, order_not_payed

  def get_orders_success(self):
    return self.orders_success

  def get_orders_error(self):
    return self.orders_errors