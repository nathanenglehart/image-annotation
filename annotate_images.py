import cv2
import pandas as pd
import os

# Nathan Englehart (Fall, 2025)

######################
####### Config #######
######################

image_dir = '/home/nath/Documents/one_of_the_boys/accuracy_checker/sample'
csv_file = 'image_labels_1.csv'

######################
######################
######################

def annotate_images(image_dir, csv_file):

    """ Annotates images to 0 or 1 for whether or not they contain an object 

        image_dir::[string]
            Folderpath containing images to annotate 

        csv_file::[string]
            Filepath of csv to write to

    """

    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=['image', 'label'])

    image_list = sorted(os.listdir(image_dir))
    labeled_images = set(df['image'])
    current_index = 0

    while current_index < len(image_list):
        filename = image_list[current_index]
        
        if filename in labeled_images:
            current_index += 1
            continue

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
            df.loc[len(df)] = [filename, 0]
            current_index += 1
        elif key == 49:  # '1'
            df.loc[len(df)] = [filename, 1]
            current_index += 1
        elif key == 98:  # 'b' to back
            if current_index > 0:
                df = df[:-1]  # Remove last label entry
                current_index -= 1
                print("Going back to the previous image")
            else:
                print("Already at the first image")
        elif key == 115:  # 's' to save
            df.to_csv(csv_file, index=False)
            print(f"Progress saved to {csv_file}")
        else:
            print(f"Skipping label for {filename} due to invalid key press.")

        cv2.destroyAllWindows()

    df.to_csv(csv_file, index=False)
    print(f"Final labels saved at {csv_file}")

annotate_images(image_dir, csv_file)

