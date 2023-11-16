import math


def get_intersection_rect(entity_1, entity_2):
    dx = entity_2.x - entity_1.x
    dy = entity_2.y - entity_1.y

    dw = (entity_2.width + entity_1.width) * 0.5
    dh = (entity_2.height + entity_1.height) * 0.5

    if abs(dx) >= dw or abs(dy) >= dh:
        return None

    x_borders = [entity_1.x - entity_1.width * 0.5, entity_1.x + entity_1.width * 0.5,
                 entity_2.x - entity_2.width * 0.5, entity_2.x + entity_2.width * 0.5]
    x_borders.sort()
    y_borders = [entity_1.y - entity_1.height * 0.5, entity_1.y + entity_1.height * 0.5,
                 entity_2.y - entity_2.height * 0.5, entity_2.y + entity_2.height * 0.5]
    y_borders.sort()

    return (x_borders[2] - x_borders[1], y_borders[2] - y_borders[1])


def normalized(vec):
    n = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
    return [vec[0]/n, vec[1]/n]


def sign(n):
    return -1 if n > 0 else 1


def rotate_vector(vec, ang):
    return [vec[0]*math.cos(ang)-vec[1]*math.sin(ang),
            vec[0]*math.sin(ang)+vec[1]*math.cos(ang)]


def inverse_lerp(v, iv, fv):
    return (v - iv) / (fv - iv)


def lerp(v, iv, fv):
    return iv + ((fv - iv) * v)
