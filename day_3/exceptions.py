class MyException(Exception):
  
  def __init__(self, message) -> None:
    super().__init__(message)
    self.message = message
    
  def __str__(self):
    return f"MyException: {self.message}"
  
def sum(a, b):
    try:
        total = a + b 
        print(total)
        return total 
    except Exception as e:
        raise e 
        # raise MyException("Invalid input")      
      
    
if __name__ == "__main__":
  sum(5, "x")