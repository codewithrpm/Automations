import requests

# URL of the image you want to download
image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6Px4dG6-UEusJDNSl1xixioBkbLTg926TpA&s"

# Send a GET request to the image URL
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open a file in binary write mode
    with open("downloaded_image.jpg", "wb") as file:
        # Write the content of the response to the file
        file.write(response.content)
    print("Image downloaded successfully.")
else:
    print(f"Failed to download image. Status code: {response.status_code}")


# import requests
# from PIL import Image
# from io import BytesIO
# r = requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6Px4dG6-UEusJDNSl1xixioBkbLTg926TpA&s")
# i = Image.open(BytesIO(r.content))
# fp = open("image.jpg", "wb")
# i.save(fp)
# fp.close()