import cv2
import matplotlib.pyplot as plt
%matplotlib inline

cctv_image = cv2.imread('0744_04.jpg')


vehicle_classifier = cv2.CascadeClassifier('cascade.xml')


vehicles = vehicle_classifier.detectMultiScale(cctv_image, 1.1, 2, maxSize=(100,100))

print 'Vehicles detected: %d' % (len(vehicles))


for (x,y,w,h) in vehicles:
    cv2.rectangle(cctv_image, (x,y), (x+w, y+h),(255,0,0),2)

plt.figure(figsize=(9,9))
plt.axis('off')
plt.imshow(cv2.cvtColor(cctv_image, cv2.COLOR_BGR2RGB))

