import os
import os.path as osp


folder_1 = "image_sets"
folder_2 = "rgb_detections"

in_f1 = osp.join(folder_1,"train.txt")
in_f2 = osp.join(folder_1,"val.txt")
in_f3 = osp.join(folder_2,"rgb_detection_val.txt")
in_f4 = osp.join(folder_2,"rgb_detection_train.txt")

out_f1 = osp.join(folder_1,"train1.txt")
out_f2 = osp.join(folder_1,"val1.txt")
out_f3 = osp.join(folder_2,"rgb_detection_val1.txt")
out_f4 = osp.join(folder_2,"rgb_detection_train1.txt")

def alt(in_f,out_f):
    fin = open(in_f,"r")
    fout = open(out_f,"w")

    i=0
    for l in fin:
        if i%2==0:
            fout.write(l)
        i+=1


    fin.close()
    fout.close()

def alt_rgb(in_f,out_f):
    fin = open(in_f,"r")
    fout = open(out_f,"w")

    i=0
    last_i=None
    start=1
    for l in fin:

        cur_i = int(l.split(' ')[0].split('/')[-1].rstrip(".png"))

        if(start or (cur_i==last_i and i%2==0)):
            fout.write(l)

        elif(cur_i==last_i and i%2!=0):
            continue

        elif(cur_i!=last_i and i%2!=0):
            fout.write(l)
            i+=1

        else:
            i+=1


        last_i = cur_i
        start=0




    fin.close()
    fout.close()

if __name__=="__main__":
    alt(in_f1,out_f1)
    alt(in_f2,out_f2)

    alt_rgb(in_f3,out_f3)
    alt_rgb(in_f4,out_f4)
