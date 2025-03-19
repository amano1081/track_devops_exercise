def add(a, b, c=0):
    try:
        # a, b, c が数値型(整数もしくは小数)であることをチェック
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
            return -1
        
        # a, b, c が 0 ≦ a ≦ 10、0 ≦ b ≦ 10、0 ≦ c ≦ 10 を満たすかチェック
        if not (0 <= a <= 10 and 0 <= b <= 10 and 0 <= c <= 10):
            return -2
        
        return int(a + b) + int(c)
    except:
        return "error"
