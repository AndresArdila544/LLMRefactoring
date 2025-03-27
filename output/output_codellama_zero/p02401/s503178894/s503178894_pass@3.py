import ast
while True:
   try:
      a = input()
      if "?" in a:
         break
      print(ast.literal_eval(a))
   except SyntaxError:
      pass