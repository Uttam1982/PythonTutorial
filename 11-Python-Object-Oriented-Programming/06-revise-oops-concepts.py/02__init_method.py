class Pizza:
  #class attribute
  info= "This is a pizza class"

  def __init__(self, type_):
    self.type_ = type_


#instantiate the pizza class:
obj = Pizza("Veggie")
print(obj.info)
print(f"I want {obj.type_} pizza")