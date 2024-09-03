def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = f"{num1:04d}"
        num2 = f"{num2:04d}"
        num4 = f"{num3:04d}"


        final = ""
        for i in range(4):
                final += min(num1[i], num2[i], num3[i])
        
        return final