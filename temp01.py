#建立一個名為check_password_strength的函式，接收一個password的字串
#規則一:檢查密碼長度是否大於等於8，如果是分數+1
#規則二:檢查密碼是否包含至少一個數字，如果是分數+1
#規則三:檢查密碼是否包含至少一個大寫字母，如果是分數+1
#規則四:檢查密碼是否包含至少一個小寫字母，如果是分數+1
#規則五:檢查密碼是否包含至少一個特殊字元(非英文字母及數字)，如果是分數+1
#最後根據總分回傳強度等級:0-2回傳"弱",3-4回傳"中",5回傳"強"

def check_password_strength(password):
    score = 0
    
    # 規則一: 檢查密碼長度是否大於等於8
    if len(password) >= 8:
        score += 1
    
    # 規則二: 檢查密碼是否包含至少一個數字
    if any(char.isdigit() for char in password):
        score += 1
    
    # 規則三: 檢查密碼是否包含至少一個大寫字母
    if any(char.isupper() for char in password):
        score += 1
    
    # 規則四: 檢查密碼是否包含至少一個小寫字母
    if any(char.islower() for char in password):
        score += 1
    
    # 規則五: 檢查密碼是否包含至少一個特殊字元(非英文字母及數字)
    if any(not char.isalnum() for char in password):
        score += 1
    
    # 根據總分回傳強度等級
    if score <= 2:
        return "弱"
    elif score <= 4:
        return "中"
    else:
        return "強"
print(check_password_strength("Password123!"))  # 強