import math as m

class Math:
     """
     Class that adapts python math module methods
     """
     @staticmethod
     def logarithm(x):
         return m.log(x)

     @staticmethod
     def logarithm2(x):
         return m.log2(x)

     @staticmethod
     def logarithm(x, base):
         return m.log(x, base)

if __name__ == '__main__':
     # Test the adapter execution
     mat = Math()
     print(f'The logarithm to the natural base of 2 is: {mat.logarithm(2)}')
     print(f'The logarithm in base 2 of 32 is: {mat.logarithm2(32)}')