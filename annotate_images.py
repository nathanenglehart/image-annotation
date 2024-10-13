import cv2
import pandas as pd
import os

# Nathan Englehart (Autumn, 2024)

######################
####### Config #######
######################

image_dir = '/media/data3/check_images'
csv_file = 'image_labels.csv'

######################
######################
######################

def annotate_images(image_dir):

    """ Annotates images to 0 or 1 for whether or not they contain an obect (modify for other purposes)

	image_dir::[String]
            Path to directory containing images to label

    """

    df = pd.DataFrame(columns=['image','label'])

    image_list = sorted(os.listdir(image_dir))
    current_index = 0

    while current_index < len(image_list):
        filename = image_list[current_index]

        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            current_index += 1
            continue

        img_path = os.path.join(image_dir, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Unable to open {filename}")
            current_index += 1
            continue

        cv2.imshow('Image', img)
        key = cv2.waitKey(0)

        if key == 48:  # '0'
            label = 0
            df.loc[len(df)] = [filename, label]
            current_index += 1
        elif key == 49:  # '1'
            label = 1
            df.loc[len(df)] = [filename, label]
            current_index += 1
        elif key == 98:  # 'b' to back
            if current_index > 0:
                df = df[:-1]  # remove last label entry
                current_index -= 1
                print("going back to the previous image")
            else:
                print("at the first image")
        elif key == 115:  # 's' to save
            df.to_csv(csv_file, index=False)
            print(f"saved progress to {csv_file}")
        else:
            print(f"skipping labal for {filename} due to invalid key press.")

        cv2.destroyAllWindows() # close image display

    counter = 0

    while(not complete):
        try:
            if(counter == 0):
                df.to_csv(csv_file, index = False)
		complete = True
            else:
                df.to_csv(csv_file, index = False)
                complete = True
        except: 
                counter = counter + 1 
    print(f"labels saved at {csv_file}")


annotate_images(image_dir = image_dir)

