import cv2
import csv
from more_itertools import unique_everseen
import pandas as pd
import os

# Check if attendance file exists, if not, create it
if not os.path.isfile('attend.csv'):
    da = pd.DataFrame(list(), columns=["Name", "Attend"])
    da.to_csv('attend.csv', index=False)

# Initialize the camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Initialize the QRCode detector
detector = cv2.QRCodeDetector()

while True:
    # Read a frame from the camera
    _, img = cap.read()
    img = cv2.resize(img, (400, 400))
    
    # Detect and decode QRCode
    data, bbox, _ = detector.detectAndDecode(img)

    # Check if there is a QRCode in the image
    if bbox is not None:
        bb_pts = bbox.astype(int).reshape(-1, 2)
        num_bb_pts = len(bb_pts)
        
        # Display the image with lines around the QRCode
        for i in range(num_bb_pts):
            cv2.line(img, tuple(bb_pts[i]), tuple(bb_pts[(i + 1) % num_bb_pts]), color=(255, 0, 0), thickness=2)
            
        if data:
            # Check if the QRCode data is in the data list
            with open('data_list.csv', "r") as f, open('attend.csv', "a") as f1:
                c = csv.reader(f)
                c1 = csv.writer(f1)
                flag = False
                for l, i in enumerate(c):
                    if i[0] == data:
                        print("Found " + "in " + str(l + 1))
                        flag = True
                        c1.writerow([data, "yes"])
                        break
                if not flag:
                    print("Not found")
    
    # Remove duplicate entries in the attendance file
    with open('attend.csv', "r") as y, open('attend2.csv', "w") as y2:
        y2.writelines(unique_everseen(y))
    
    # Read and update attendance file
    df = pd.read_csv('attend2.csv')
    df.to_csv('attend3.csv', index=False)
    
    # Display the result
    cv2.imshow("img", img)
    
    # Wait for 'q' key to quit and clean up files
    if cv2.waitKey(1) == ord("q"):
        os.remove('attend.csv')
        os.remove('attend2.csv')
        os.rename(r'attend3.csv', r'attend.csv')
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()