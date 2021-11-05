nums = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 
        10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
        17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 
        60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}
    
def one_to_hundred():   
    numbers = ''
    for i in range(1,100):
        if i < 21:
            numbers += nums[i]
        if i > 20 and i < 30:
            numbers += (nums[20]+nums[i%20])
        if i == 30: numbers += (nums[30])
        if i > 30 and i < 40:
            numbers +=(nums[30]+nums[i%30])
        if i == 40: numbers +=(nums[40])
        if i > 40 and i < 50:
            numbers +=(nums[40]+nums[i%40])
        if i == 50: numbers +=(nums[50])
        if i > 50 and i < 60:
            numbers +=(nums[50]+nums[i%50])
        if i == 60: numbers +=(nums[60])
        if i > 60 and i < 70:
            numbers +=(nums[60]+nums[i%60])
        if i == 70: numbers +=(nums[70])
        if i > 70 and i < 80:
            numbers +=(nums[70]+nums[i%70])
        if i == 80: numbers +=(nums[80])
        if i > 80 and i < 90:
            numbers +=(nums[80]+nums[i%80])
        if i == 90: numbers +=(nums[90])
        if i > 90 and i < 100:
            numbers +=(nums[90]+nums[i%90])
        if i == 100: numbers +=(nums[100])
    return numbers

total = 0
for i in range(0,11):
    if i == 0:
        total +=(len(one_to_hundred()))
    if i > 0 and i != 10:
        total +=((len(nums[i] + nums[100]) * 100) + len(one_to_hundred()) + (99 * len('and')))
    if i == 10:
        total +=(len('onethousand'))
print('The Total of All the Characters In The Words for the Numbers 1 to 1000 is: ', total)