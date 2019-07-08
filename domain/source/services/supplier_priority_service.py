
class SupplierPriorityService:
  def __init__(self):
    self.priority_dict = {}

  def add_priority(self, sku_code, priority):
    self.priority_dict[sku_code] = priority

  def get_priority(self, sku_code):
    return self.priority_dict[sku_code]

  def have_sku(self, sku_code):
    return False if sku_code not in self.priority_dict else True