import cv2
import matplotlib.pyplot as plt


image = cv2.imread("face_noisy.jpg")

if image is None:
    print("Could not read the image")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

average = cv2.blur(image, (7, 7))
average_gray = cv2.cvtColor(average, cv2.COLOR_BGR2GRAY)
edges_average = cv2.Canny(average_gray, 50, 150)


median = cv2.medianBlur(image, 7)
median_gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
edges_median = cv2.Canny(median_gray, 50, 150)


gaussian = cv2.GaussianBlur(image, (7, 7), 0)
gaussian_gray = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
edges_gaussian = cv2.Canny(gaussian_gray, 70, 160)


average_rgb = cv2.cvtColor(average, cv2.COLOR_BGR2RGB)
median_rgb = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)
gaussian_rgb = cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB)


plt.figure(figsize=(12, 8))

plt.subplot(2, 4, 1)
plt.imshow(image_rgb)
plt.title("Original")
plt.axis("off")

plt.subplot(2, 4, 2)
plt.imshow(average_rgb)
plt.title("Average Blur")
plt.axis("off")

plt.subplot(2, 4, 3)
plt.imshow(median_rgb)
plt.title("Median Blur")
plt.axis("off")

plt.subplot(2, 4, 4)
plt.imshow(gaussian_rgb)
plt.title("Gaussian Blur")
plt.axis("off")

plt.subplot(2, 4, 5)
plt.imshow(edges_average, cmap="gray")
plt.title("Canny - Average")
plt.axis("off")

plt.subplot(2, 4, 6)
plt.imshow(edges_median, cmap="gray")
plt.title("Canny - Median")
plt.axis("off")

plt.subplot(2, 4, 7)
plt.imshow(edges_gaussian, cmap="gray")
plt.title("Canny - Gaussian")
plt.axis("off")

plt.tight_layout()
plt.show()