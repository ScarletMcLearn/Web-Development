from googletrans import Translator
import time
import random

translator = Translator()


def trans_list(str_array):

    res = []

#     str_len = 0

#     for txt in str_array:
#         str_len = str_len + len(txt)



#     if (str_len >= 15000):
#         print('Too big!!! 15k Max!')
        
#         return

#     else:
    res.append(translator.translate(str_array, dest='bn'))



    # Wait for 5 seconds
    randy = random.randint(1, 5)

    print("Waiting for " + str(randy) + " seconds.")

    time.sleep(randy)
    
    return res
