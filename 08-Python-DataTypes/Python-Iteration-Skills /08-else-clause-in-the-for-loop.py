#------------------------------------------------------------------------
# else clause in the for loop.
#------------------------------------------------------------------------

# It should be noted that it’s not the most intuitive technique to use, 
# as many people don’t even know the existence of the else clause with 
# the for loop.

#------------------------------------------------------------------------

def place_group_order(ordered_items):
  menu_items = ['beef','pork','chicken','sausage']
  for name, item in ordered_items.items():
    if item not in menu_items:
      print(f"Your group order can't be served, because {name}'s':{item} isn't available")
      break
  else:
    print("Your group ordered can be served.")

print("Group01")
grp01_items ={"Sam":"beef","Ben":"tuna","Joe":"chicken"}
place_group_order(grp01_items)

print("Group02")
grp01_items ={"Sara":"beef","dave":"pork","rita":"chicken"}
place_group_order(grp01_items)




