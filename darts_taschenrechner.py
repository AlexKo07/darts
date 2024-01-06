game = True
score = 501

def darts_calculator():
    global score
    print("score: 501")
    while game == True:
        
         x = int(input("type in your score"))
         if x <= 180 and x >= 0 and score >= 0:  # subtrahiert den score und verhindert, dass über 180 gescored wird
              score -= x 
         else:
              x =  int(input("Error. type in your score"))
              if x<= 180 and x>= 0 and score >= 0:
                  score -= x
         if score < 0 or score == 1:
             print("no score")
             score += x
         
         print(f"Score: {score}")    
        
        # alle Finishwege     
        
        
         if score == 170:
             print("T20,T19,Bull")
         elif score == 167:
             print("T20,T20,Bull")    
         elif score == 164:
             print("T20,T18,Bull")
         elif score == 161:
             print("T20,T17,Bull")
         elif score == 160:
             print("T20,T20,D20")
         elif score == 158:
             print("T20,T20,D19")
         elif score == 157:
             print("T20,T19,D20")
         elif score == 156:
             print("T20,T20,D18")
         elif score == 155:
             print("T20,T19,D19")
         elif score == 154:
             print("T20,T18,D20")
         elif score == 153:
             print("T20,T19,D18")
         elif score == 152:
             print("T20,T20,D16")
         elif score == 151:
             print("T20,T17,D20")
         elif score == 150:
             print("T20,T18,D18") 
         elif score == 149:
             print("T20,T19,D16")
         elif score == 148:
             print("T20,T20,D14")
         elif score == 147:
             print("T20,T17,D18")
         elif score == 146:
             print("T20,T18,D16")
         elif score == 145:
             print("T20,T15,D20")
         elif score == 144:
             print("T20,T20,D12")
         elif score == 143:
             print("T20,T17,D16")
         elif score == 142:
             print("T20,BULL,D16")
         elif score == 141:
             print("T20,T19,D12")
         elif score == 140:
             print("T20,T20,D10")
         elif score == 139:
             print("T20,T19,D11")
         elif score == 138:
             print("T20,T18,D12")
         elif score == 137:
             print("T20,T19,D10")
         elif score == 136:
             print("T20,T20,D8")
         elif score == 135:
             print("T20,T17,D12")
         elif score == 134:
             print("T20,T14,D16")
         elif score == 133:
             print("T20,T19,D8")
         elif score == 132:
             print("BULL,BULL,D16")
         elif score == 131:
             print("T20,T17,D10")
         elif score == 130:
             print("T20,T20,D5")
         elif score == 129:
             print("T19,T16,D9")
         elif score == 128:
             print("T18,T14,D16")
         elif score == 127:
             print("T20,T17,T8")
         elif score == 126:
             print("T19,T19,D6")
         elif score == 125:
             print("Bull,T20,D20")
         elif score == 124:
             print("T20,T14,D11")
         elif score == 123:
             print("T19,T16,D9")
         elif score == 122:
             print("T18,T18,D7")
         elif score == 121:
             print("T20,T11,D14")
         elif score == 120:
             print("T20,20,D20")
         elif score == 119:
             print("T19,T12,D13")
         elif score == 118:
             print("T20,18,D20")
         elif score == 117:
             print("T20,17,D20")
         elif score == 116:
             print("T20,16,D20")
         elif score == 115:
             print("T20,15,D20")
         elif score == 114:
             print("T20,14,D20")
         elif score == 113:
             print("T20,13,D20")
         elif score == 112:
             print("T20,12,D20")
         elif score == 111:
             print("T20,11,D20")
         elif score == 110:
             print("T20,10,D20")
         elif score == 109:
             print("T20,9,D20")
         elif score == 108:
             print("T20,8,D20")
         elif score == 107:
             print("T20,7,D20")
         elif score == 106:
             print("T20,6,D20")
         elif score == 105:
             print("T20,5,D20")
         elif score == 104:
             print("T20,4,D20")
         elif score == 103:
             print("T20,3,D20")
         elif score == 102:
             print("T20,2,D20")
         elif score == 101:
             print("T20,1,D20")
         elif score == 100:
             print("T20,D20")
         elif score == 99:
             print("T19,2,D20")
         elif score == 98:
             print("T20,D19")
         elif score == 97:
             print("T19,D20")
         elif score == 96:
             print("T20,D18")
         elif score == 95:
             print("T19,D19")
         elif score == 94:
             print("T18,D20")
         elif score == 93:
             print("T19,D18")
         elif score == 92:
             print("T20,D16")
         elif score == 91:
             print("T17,D20")
         elif score == 90:
             print("T18,D18")#
         elif score == 89:
             print("T19,D16")
         elif score == 88:
             print("T16,D20")
         elif score == 87:
             print("T17,D18")
         elif score == 86:
             print("T18,D16")
         elif score == 85:
             print("T15,D20")
         elif score == 84:
             print("T20,D12")
         elif score == 83:
             print("T17,D16")
         elif score == 82:
             print("BULL")
         elif score == 81:
             print("T19,D12")
         elif score == 80:
             print("T20,D10")
         elif score == 79:
             print("T19,D11")
         elif score == 78:
             print("T18,D12")
         elif score == 77:
             print("T19,D10")
         elif score == 76:
             print("T20,D8")                                                                    
         elif score == 75:
             print("T17,D12")
         elif score == 74:
             print("T14,D16")
         elif score == 73:
             print("T19,D8")
         elif score == 72:
             print("T16,D12")
         elif score == 71:
             print("T17,D10")
         elif score == 70:
             print("T18,D8")
         elif score == 69:
             print("T19,D6")
         elif score == 68:
             print("T20,D4")
         elif score == 67:
             print("T17,D8")
         elif score == 66:
             print("T10,D18")             
         elif score == 65:
             print("T15,D10")
         elif score == 64:
             print("T8,D20")                                                                            
         elif score == 63:
             print("T13,D12")
         elif score == 62:
             print("T10,D16")
         elif score == 61:
             print("25,D18") 
         elif score == 60:
            print("20,D20")
         elif score == 59:
             print("19,D20")
         elif score == 58:
             print("18,D20")
         elif score == 57:
             print("17,D20")
         elif score == 56:
             print("16,D20")
         elif score == 55:
             print("15,D20")
         elif score == 54:
             print("14,D20")
         elif score == 53:
             print("13,D20")
         elif score == 52:
             print("12,D20")
         elif score == 51:
             print("11,D20")
         elif score == 50:
             print("10,D20")


         if score == 0:
             print("Glückwunsch, du hast das Leg abgeschlossen")
             exit()
    
if __name__ == "__main__":
    darts_calculator()
