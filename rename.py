import os

imagedir = r"C:\Users\max\Documents\GitHub\bmhs1957\images\events\80thbirthday"
imagenum = 1

for image in os.listdir(imagedir):
    print(f'Image name is {image}')
    os.rename(os.path.join(imagedir, image),
              os.path.join(imagedir, f'80thbirthday_{imagenum}.jpeg'))
    # os.rename(image, f'80thbirthday_{imagenum}.jpeg')
    print(f'New name is {image}\n')
    imagenum += 1
