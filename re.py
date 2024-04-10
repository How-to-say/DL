import os
import cv2 as cv
save_path="./final.txt"
def txtchange():
    num =1
    error=0
    with open(save_path, 'w') as f1:
        while True:
            img_path=r'C:\Users\ashu\Desktop\picture\img\\'+str(num)+'.jpg'
            label_path=r'C:\Users\ashu\Desktop\picture\label\\'+str(num)+'.txt'
            image = cv.imread(img_path)
            x0=image.shape[1]
            y0=image.shape[0]
            if not os.path.exists(label_path) and error<1500:
                num+=1
                error+=1
                continue
            elif not os.path.exists(label_path) or error>=1500:
                break
            with open(label_path) as f:
                print("open label"+str(num))
                data=f.readline().split(' ')
                x1=float(data[1]) * x0
                y1=float(data[2]) * y0
                w1=float(data[3]) * x0
                h1=float(data[4].strip()) * y0
                
            x=round(x1 - w1/2,4)
            y=round(y1 - h1/2,4)
            w=round(w1,4)
            h=round(h1,4)
            string1=str(x)+','+str(y)+','+str(w)+','+str(h)+'\n'
            f1.write(string1)
            num+=1

if __name__ =="__main__":
    txtchange()
