
class SupplierPriority:
  def __init__(self, sku_code, priority_dict, short_cut):
    self.sku_code = sku_code
    self.supplier_dict = {}
    self.short_cut = short_cut

    self._add_suppliers(priority_dict)
  
  def _add_supplier(self, supplier_name, priority):
    try:
      priority_int = int(priority)
    except ValueError as e:
      priority_int = None
    finally:
      if priority_int is not None:
        self.supplier_dict[supplier_name] = priority_int

  def _add_suppliers(self, priority_dict):
    for key in priority_dict.keys():
      self._add_supplier(key, priority_dict[key])

  def get_order_supplier(self):
    order_supplier = []
    priority_list =  self.supplier_dict.values()
    priority_list.sort()

    for priority in priority_list:
      for key, value in self.supplier_dict.items():
        if self.supplier_dict[key] == priority:
          order_supplier.append(key)

    return order_supplier