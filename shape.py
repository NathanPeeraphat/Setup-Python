def get_circle_area(radius):
    if radius < 0:
        return 0 
    return 22/7 * (radius ** 2)

def get_triangle_area(width, height):
    if width < 0 or height < 0:
        return 0 
    return 1/2 * width * height

def get_rectangle_area(width, length):
    if width < 0 or length < 0:
        return 0 
    return width * length

def get_box_area(width, length, height):
    if width < 0 or length < 0 or height < 0:
        return 0 
    return width * length * height