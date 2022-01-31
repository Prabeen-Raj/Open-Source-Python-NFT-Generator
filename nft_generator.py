from PIL import Image
import random
import time
import os
i = 0
# overlay bg and face

while True:
    r1 = random.randint(1,26)
    r2 = random.randint(0,5)
    img1 = Image.open(r"b"+str(r1)+".PNG")
    img2 = Image.open(r"f"+str(r2)+".PNG")
    img1.paste(img2, (0,0), mask = img2)
    img1.save("n1.PNG")
    time.sleep(1)

    # to overlay eyes with n1
    r3 = random.randint(1,18)
    img3 = Image.open(r"n1.PNG")
    img4 = Image.open(r"eyes"+str(r3)+".PNG")
    img3.paste(img4, (0,0), mask = img4)
    img3.save("n2.PNG")
    os.remove("n1.PNG")
    time.sleep(1)

    # to overlay nose with n2
    r4 = random.randint(1,9)
    img5 = Image.open(r"n2.PNG")
    img6 = Image.open(r"nose"+str(r4)+".PNG")
    img5.paste(img6, (0,0), mask = img6)
    img5.save("n3.PNG")
    os.remove("n2.PNG")
    time.sleep(1)

    r5 = random.randint(1,22)
    img7 = Image.open(r"n3.PNG")
    img8 = Image.open(r"mouth"+str(r5)+".PNG")
    img7.paste(img8, (0,0), mask = img8)
    img7.save(str(i)+"a.PNG")
    i +=1
    os.remove("n3.PNG")

    if (i==1000):
        break





