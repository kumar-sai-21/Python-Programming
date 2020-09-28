file_obj_sow=open("sowpods.txt",)
file_obj_son=open("sonnet_words.txt")
sow_set={word.strip() for word in file_obj_sow.readlines()}
son_list={word.strip() for word in file_obj_son.readlines()}
file_obj_sow.close()
file_obj_son.close()
#import time
#tic = time.time()
for son in son_list:
    if son not in sow_set:
        print(son)
#print(time.time()-tic)
