import numpy as np


def rotate_1024x768_to_400x400(np_image: np.ndarray) -> np.ndarray:
    """
    Resize and crop a 1024x768 RGB image to a 400x400 grayscale image,
    and transpose it

    Args:
    - np_image (np.ndarray): input image as a 3D NumPy array
                             of shape (768, 1024, 3) with RGB channels

    Returns:
    - np.ndarray: cropped and transposed grayscale image as a 3D NumPy
                array of shape (400, 400, 1), or None if an error occurs

    Raises:
    - ValueError: if the input image is None, has an invalid shape,
                  or does not match the required dimensions
    """
    try:
        if np_image is None:
            raise ValueError("Image is None")
        if len(np_image.shape) != 3:
            raise ValueError("Image must be a 3D array")
        if np_image.shape[2] != 3:
            raise ValueError("Image must have 3 channels (RGB)")
        if not (np_image.shape[0] == 768 or np_image.shape[1] == 1024):
            raise ValueError("Image size must be 1024x768")

        # Converts the image to grayscale using standard luminance weights
        gray_np_image = np.dot(np_image[..., :3], [0.299, 0.587, 0.114])
        # # Converts the image to grayscale by averaging the RGB channels
        # gray_np_image = np.mean(np_image, axis=2)

        # Define cropping starting points
        start_x = (gray_np_image.shape[1] - 574)
        start_y = (gray_np_image.shape[0] - 668)

        # Crop the grayscale image to a 400x400
        cropped_np_image = gray_np_image[
            start_y:start_y + 400,
            start_x:start_x + 400]

        # Transpose, convert to uint8, and reshape for the output
        cropped_np_image = np.transpose(cropped_np_image)
        cropped_np_image = cropped_np_image.astype(np.uint8)

        print(f'New shape after slicing: {cropped_np_image.shape}')

        return cropped_np_image
    except ValueError as e:
        print(f'ValueError: zoom(): {e}')
        return None
