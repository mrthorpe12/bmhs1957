import os

imagedir = r"C:\Users\max\Documents\GitHub\bmhs1957\images\events\birthday80"
imagenum = 1

for image in os.listdir(imagedir):
    # imagepath = os.path.join(imagedir, image)
    print(f'Image name is {image}')
    os.rename(os.path.join(imagedir, image),
              os.path.join(imagedir, f'birthday80_{imagenum}.jpeg'))
    print(f'New name is {image}\n')
    imagenum += 1
