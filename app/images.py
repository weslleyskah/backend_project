from dotenv import load_dotenv
from imagekitio import ImageKit
import os

# Load .env file
load_dotenv()

# Now get the environment variable
private_key = os.getenv("IMAGEKIT_PRIVATE_KEY")

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
)