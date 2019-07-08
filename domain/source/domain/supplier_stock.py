
class SupplierStock:
  def __init__(self, sku, supplier_dict):
    self.sku = sku
    self.supplier_dict = {}
    self.add_supplers(supplier_dict)

  def add_supplier_quantity(self, supplier, quantity):
    try:
      int_quantity = int(quantity)
    except ValueError as e:
      int_quantity = 0
    finally:
      if not self._have_supplier(supplier):
        self.supplier_dict[supplier] = int_quantity
      else:
        self.supplier_dict[supplier] = self.supplier_dict[supplier] + int_quantity

  def minus_supplier_quantity(self, supplier, quantity):
    # TODO refactor
    self.supplier_dict[supplier] = self.supplier_dict[supplier] - quantity

  def _have_supplier(self, supplier):
    return True if supplier in self.supplier_dict.keys() else False

  def add_supplers(self, supplier_dict):
    for key in supplier_dict.keys():
      self.add_supplier_quantity(key, supplier_dict[key])

  def supplier_is_valid(self, supplier, quantity):
    if self.supplier_dict[supplier] >= quantity: 
      return True
    return False