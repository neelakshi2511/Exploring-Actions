def add_two_nums(num1 , num2):
  return num1 + num2 
def test_add_two_nums():
  assert add_two_nums(1 , 2) == 3
  assert add_two_nums(1 , -1) == 0
  assert add_two_nums(5 , 10) == 15
