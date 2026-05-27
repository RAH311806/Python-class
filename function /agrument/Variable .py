x = 100
 
 def show_Scope():
    y = 200
    print(f"Inside: x={x}, y={y}")

    def modify_global():
      global x 
      x = 999
      print(f"Modified x to {x}")

      show_scope()
      modify_gloal()
      print(f"Outside: x={x}")
      